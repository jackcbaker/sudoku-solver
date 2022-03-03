from typing import List, Dict, Any

from sudoku_solver.solver import solve_sudoku


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
    solve_sudoku(board)
