from typing import List, Dict, Any
import logging

from ortools.sat.python import cp_model

from sudoku_solver.model import SudokuModel


def solve_sudoku(board: List[Dict[str, Any]], app_logger: logging.Logger) -> List[Dict[str, Any]]:
    """Solve Sudoku board and return solved board"""
    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = False
    model = SudokuModel()
    model.build(board=board)
    status = solver.Solve(model.cp_model)
    is_successful = (status == cp_model.FEASIBLE) or (status == cp_model.OPTIMAL)
    if is_successful:
        model.is_solved = True
        return model.get_output_board(solver)
    else:
        app_logger.error("Unable to solve board.")
        return None
