from typing import List, Dict, Any
from sudoku_solver.constants import BOARD_SIZE

from sudoku_solver.solver import solve_sudoku
from sudoku_solver.validator import get_inner_square


class BoardOutput:
    """Store output board in a way that's easy to test"""

    def __init__(self, board: List[Dict[str, Any]]):
        self.rows = {row: [] for row in range(BOARD_SIZE)}
        self.columns = {column: [] for column in range(BOARD_SIZE)}
        self.inner_squares = {inner_square: [] for inner_square in range(BOARD_SIZE)}
        self.variables_by_coord = {}
        for row_entries in board:
            row = row_entries['rowNum']
            for column_entries in row_entries['rowEntries']:
                column = column_entries['col']
                self.rows[int(row)].append(column_entries['value'])
                self.columns[int(column)].append(column_entries['value'])
                self.inner_squares[int(get_inner_square(column_entries))].append(
                    column_entries['value']
                )
                self.variables_by_coord[row, column] = column_entries['value']


def build_board_from_triples(entries: List[int]) -> List[Dict[str, Any]]:
    """
    Build a board from a list of sparse triples
    """
    board = []
    for row in range(9):
        row_dict = {
            'rowNum': row,
            'rowEntries': []
        }
        for col in range(9):
            try:
                value = str(entries[(row, col)])
            except KeyError:
                value = ""
            row_dict["rowEntries"].append({
                'value': value,
                'row': row,
                'col': col,
                'coord': (row, col,)
            })
        board.append(row_dict)
    return board


def all_different(li: List[int]):
    return len(li) == len(set(li))


def test_sudoku_model():
    # Encode entries as dict of sparse triples: (row, column): value
    entries = {
        (1, 2): 9,
        (2, 2): 5,
        (5, 3): 8,
        (1, 1): 1,
        (8, 8): 4,
        (2, 3): 7,
    }
    board = build_board_from_triples(entries)
    output_board = solve_sudoku(board)
    test_board = BoardOutput(output_board)
    for _, row_entries in test_board.rows.items():
        assert all_different(row_entries)
    for _, col_entries in test_board.columns.items():
        assert all_different(col_entries)
    for _, inner_square_entries in test_board.inner_squares.items():
        assert all_different(inner_square_entries)
