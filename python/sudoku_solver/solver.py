from typing import List, Dict, Any

from ortools.sat.python import cp_model

from sudoku_solver.model import SudokuModel


class ForceOneSolution(cp_model.CpSolverSolutionCallback):
    """Force stop after first solution"""

    def __init__(self, variables, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)

    def on_solution_callback(self):
        self.StopSearch()


def solve_sudoku(board: List[Dict[str, Any]]):
    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = False
    model = SudokuModel()
    model.build(board=board)
    solver.Solve(model.cp_model)