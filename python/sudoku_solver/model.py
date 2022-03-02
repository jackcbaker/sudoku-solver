from typing import List, Dict, Any

from ortools.sat.python import cp_model

from sudoku_solver import constants
from sudoku_solver.validator import get_inner_square

class SudokuModel:
    """Constraint programming model of sudoku board"""

    def __init__(self):
        # Containers to hold various combination of variables
        self.rows = {row: [] for row in range(constants.BOARD_SIZE)}
        self.columns = {col: [] for col in range(constants.BOARD_SIZE)}
        self.inner_squares = {inner_square: [] for inner_square in range(constants.BOARD_SIZE)}
        self.variables_by_coord = {}
        self.cp_model = cp_model.CpModel()

    def build(self, board: List[Dict[str, Any]]):
        """Build cp-model for sudoku"""
        self._generate_variables(board)
    
    def _generate_variables(self, board: List[Dict[str, Any]]):
        """Generate variables, fixing them if they are set already. Add to containers."""
        for row_dict in board:
            row = int(row_dict['rowNum'])
            for col_dict in row_dict['rowEntries']:
                col = int(col_dict['col'])
                var_current = self.cp_model.NewIntVar(
                    lb=1,
                    ub=constants.BOARD_SIZE,
                    name=f"Entry {row}, {col}"
                )
                self.variables_by_coord[(row, col,)] = var_current
                # Add variable to correct container
                self.rows[row] = var_current
                self.columns[col] = var_current
                self.inner_squares[get_inner_square(col_dict)] = var_current
                # If entry defined. Add as constraint.
                if col_dict['value'] != "":
                    self.cp_model.Add(var_current == int(col_dict['value']))
