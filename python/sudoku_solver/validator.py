from typing import List, Dict, Any
import logging


def validate_board(board: List[Dict[str, Any]], app_logger: logging.Logger):
    app_logger.info("Validating board...")
    if not check_entries(board, app_logger):
        return False
    if not check_rows(board, app_logger):
        return False
    if not check_columns(board, app_logger):
        return False
    if not check_inner_square(board, app_logger):
        return False
    return True


def check_entries(board: List[Dict[str, Any]], app_logger: logging.Logger):
    """Check entries are all from 1-9"""
    for row in board:
        for cell in row['rowEntries']:
            validation = cell['value'] in [""] + [str(i) for i in range(1, 10)]
            if not validation:
                app_logger.info(
                    "Cell (%s, %s) contains the invalid entry %s",
                    cell['row'],
                    cell['col'],
                    cell['value']
                )
                return False
    return True


def check_rows(board: List[Dict[str, Any]], app_logger: logging.Logger):
    """Check the rows all contain distinct values"""
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
    """Check the columns all contain distinct values"""
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


def check_inner_square(board: List[Dict[str, Any]], app_logger: logging.Logger):
    """Check each inner square contains values that are all distinct"""
    board_size = len(board)
    if board_size != 9:
        app_logger.error("Only implemented for board size 9")
    inner_squares = {}
    for inner_square in range(board_size):
        inner_squares[inner_square] = []
    for row in board:
        for cell in row['rowEntries']:
            if cell['value'] != '':
                inner_square_number = get_inner_square(cell)
                inner_squares[inner_square_number].append(cell['value'])
    for inner_square, inner_square_entries in inner_squares.items():
        # Check they're all different
        all_different = len(set(inner_square_entries)) == len(inner_square_entries)
        if not all_different:
            app_logger.info(
                "Inner square number '%s' invalid on board with entries %s",
                inner_square_number,
                inner_square_entries
            )
            return False
    return True


def get_inner_square(cell: Dict[str, Any]):
    """Get the inner sudoku square number of a particular cell"""
    square_number = (int(cell['row']) // 3) * 3
    square_number += int(cell['col']) // 3
    return square_number
