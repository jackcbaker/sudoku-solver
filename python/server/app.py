import logging

import flask
from flask import request, jsonify
from flask_cors import CORS

from sudoku_solver import validator, solver


FRONTEND_URL = "http://localhost:8080"


app = flask.Flask(__name__)
CORS(app, origins=f"{FRONTEND_URL}")


@app.route("/solve", methods=["POST"])
def solve():
    """Solve the Sudoku with the given input"""
    if request.method == "POST":
        board = request.json
        app.logger.info("Requested board: %s", board)
        validation = validator.validate_board(board=board, app_logger=app.logger)
        if not validation:
            return "Invalid board", 400
        output_board = solver.solve_sudoku(board=board, app_logger=app.logger)
        # If output_board is None there was a problem with solve
        if output_board is None:
            return "Error solving board", 500
        return jsonify(output_board), 200
    else:
        response = flask.make_response("POST requests only", 400)
        return response


@app.route("/oops", methods=["GET"])
def oops():
    """Solve the Sudoku with the given input"""
    response = flask.make_response("Oops!", 500)
    return response


if __name__ == '__main__':
    app.run(debug=True)