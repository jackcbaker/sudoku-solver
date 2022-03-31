# Full-stack sudoku solver. Vue, flask, OR-tools.

A simple, full-stack Sudoku solver, written to learn Vue, flask and joining the dots with OR-tools to creating full-stack optimisation applications.


## Installation

#### Frontend install

Make sure you have Node js installed. Then in the root of the repo run `npm install -d`.

#### Backend install

Make sure you have `python` and `python-poetry` installed.

`cd` to the `python/` subdirectory from the repo root. Run `poetry install`.


## Instructions for running in a development environment

#### Run frontend app

In the root of the repo run the following command in your terminal

```bash
npm run serve
```

#### Run backend app

This will boot the backend flask dev server.

`cd` to the `python/` subdirectory from the repo root. Run the following command in your terminal

```bash
poetry run python -m server.app
```


#### Navigate to the web app on your browser

In your browser of choice, open the url `http://localhost:8080`