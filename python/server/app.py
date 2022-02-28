import logging

import flask
from flask import request
from flask_cors import CORS

from sudoku_solver import validator


FRONTEND_URL = "http://127.0.0.1:8080"


app = flask.Flask(__name__)
CORS(app, origins=f"{FRONTEND_URL}")


@app.route("/solve", methods=["GET", "POST"])
def solve():
    """Solve the Sudoku with the given input"""
    if request.method == "GET":
        app.logger.info("getting...")
        response = flask.make_response("Solve request received :)")
        return response
    elif request.method == "POST":
        app.logger.info(request.json)
        validation = validator.validate_board(board=request.json, app_logger=app.logger)
        if not validation:
            return "Invalid board", 400
        return "Post received :)", 200
    else:
        response = flask.make_response("Request error", 500)
        return response


@app.route("/oops", methods=["GET"])
def oops():
    """Solve the Sudoku with the given input"""
    response = flask.make_response("Oops!", 500)
    return response
