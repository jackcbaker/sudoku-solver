from typing import List, Dict, Any
from copy import deepcopy

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
        self.output_board: List[Dict[str, Any]] = []
        self.cp_model = cp_model.CpModel()
        self.is_solved = False

    def build(self, board: List[Dict[str, Any]]):
        """Build cp-model for sudoku"""
        self._generate_variables(board)
        self._generate_constraints()

    def get_output_board(self, solver) -> List[Dict[str, Any]]:
        """Fetch output board from solved model"""
        output_board: List[Dict[str, Any]] = deepcopy(self.output_board)
        assert self.is_solved is True, "Model needs to be solved before fetching output"
        for row_dict in output_board:
            for col_dict in row_dict['rowEntries']:
                col_dict['value'] = solver.Value(col_dict['value'])
        return output_board

    def _generate_variables(self, board: List[Dict[str, Any]]):
        """Generate variables, fixing them if they are set already. Add to containers."""
        for row_dict in board:
            row = int(row_dict['rowNum'])
            output_row = {
                'rowNum': str(row),
                'rowEntries': []
            }
            for col_dict in row_dict['rowEntries']:
                col = int(col_dict['col'])
                var_current = self.cp_model.NewIntVar(
                    lb=1,
                    ub=constants.BOARD_SIZE,
                    name=f"Entry {row}, {col}"
                )
                self.variables_by_coord[(row, col,)] = var_current
                # Add variable to correct container
                self.rows[row].append(var_current)
                self.columns[col].append(var_current)
                self.inner_squares[get_inner_square(col_dict)].append(var_current)
                # If entry defined. Add as constraint.
                if col_dict['value'] != "":
                    self.cp_model.Add(var_current == int(col_dict['value']))
                # Setup output board
                output_dict = deepcopy(col_dict)
                output_dict['value'] = var_current
                output_row['rowEntries'].append(output_dict)
            self.output_board.append(output_row)

    def _generate_constraints(self):
        """Generate constraints from the variable containers"""
        for i in range(constants.BOARD_SIZE):
            self.cp_model.AddAllDifferent(self.rows[i])
            self.cp_model.AddAllDifferent(self.columns[i])
            self.cp_model.AddAllDifferent(self.inner_squares[i])
