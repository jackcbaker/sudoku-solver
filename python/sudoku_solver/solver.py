from typing import List, Dict, Any

from ortools.sat.python import cp_model

from sudoku_solver.model import SudokuModel


def solve_sudoku(board: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Solve Sudoku board and return solved board"""
    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = False
    model = SudokuModel()
    model.build(board=board)
    solver.Solve(model.cp_model)
    model.is_solved = True
    return model.get_output_board(solver)