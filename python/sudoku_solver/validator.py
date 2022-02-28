from typing import List, Dict, Any
import logging


def validate_board(board: List[Dict[str, Any]], app_logger: logging.Logger):
    app_logger.info("Validating board...")
    if not check_rows(board, app_logger):
        return False
    if not check_columns(board, app_logger):
        return False
    return True


def check_rows(board: List[Dict[str, Any]], app_logger: logging.Logger):
    for row in board:
        # Get nonempty squares
        squares = [
            entry['value'] for entry in row['rowEntries']
            if entry['value'] != ''
        ]
        # Check they're all different
        all_different = len(set(squares)) == len(squares)
        if not all_different:
            app_logger.info(
                "Row number '%s' invalid on board with entries %s",
                row['rowNum'],
                squares
            )
            return False
    return True


def check_columns(board: List[Dict[str, Any]], app_logger: logging.Logger):
    columns = {}
    for row in board:
        for square in row['rowEntries']:
            if square['value'] != '':
                try:
                    columns[square['col']].append(square['value'])
                except KeyError:
                    columns[square['col']] = [square['value']]
    for column_number, column_entries in columns.items():
        # Check they're all different
        all_different = len(set(column_entries)) == len(column_entries)
        if not all_different:
            app_logger.info(
                "Column number '%s' invalid on board with entries %s",
                column_number,
                column_entries
            )
            return False
    return True
