<template>
  <div class="container">
    <div class="alertContainer">
      <span class="alerts">
      </span>
      <button class="alerts">OK</button>
    </div>
    <div class="board">
      <div class="row" v-for="row in board" :key="row.rowNum">
        <base-cell
          v-for="entry in row.rowEntries"
          :key="entry.coord"
          :cellData=entry
          :boardSize=boardSize
          @update-cell="updateCellValue"
        >
        </base-cell>
      </div>
    </div>
    <div class="toolbar">
      <button
        @click="solveBoard"
        class="bottomButtons"
        v-bind:class="{solving: isSolving}"
      >
        {{ solveButtonText }}
      </button>
      <button @click="resetBoard" class="bottomButtons resetButton">
        Reset
      </button>
    </div>
  </div>
</template>

<script>
import BaseCell from "./components/BaseCell.vue"
export default {
  components: {
    BaseCell
  },
  data() {
    return {
      boardSize: 9,
      board: this.initialiseBoardData(9),
      solveButtonText: "Solve",
      solveStatus: "No solve request made",
      solverURL: "http://127.0.0.1:5000",
      errors: ""
    };
  },
  computed: {
    cellWidth: function() {
      return 100 / (this.boardSize) + '%'
    },
    isSolving: function() {
      if (this.solveButtonText != "Solve") {
        return true
      } else {
        return false
      }
    }
  },
  methods: {
    initialiseBoardRow(boardSize, rowNum) {
      let output = {
        "rowNum": rowNum,
        "rowEntries": Array(boardSize).fill(0).map(
          (_, colNum) => (
            {'row': rowNum, 'col': colNum, 'coord': [rowNum, colNum], 'value': ""}
          )
        )
      }
      return output
    },
    initialiseBoardData(boardSize) {
      let output = Array(boardSize).fill(0).map(
        (_, rowNum) => this.initialiseBoardRow(boardSize, rowNum)
      )
      return output
    },
    async solveBoard() {
      let solveRoute = "/solve"
      let solveResponse = undefined
      if (this.solveButtonText == "Solve") {
        this.solveButtonText = "Solving..."
      }
      try {
        solveResponse = await fetch(
          `${this.solverURL}${solveRoute}`,
          {
            method: "POST",
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.board)
          }
        )
      } catch (error) {
        // Catch e.g. a 404
        console.log(error.message)
        this.solveButtonText = `Solve error`
        return
      }
      console.log(solveResponse.ok)
      if (!solveResponse.ok) {
        this.solveButtonText = `Solve error: ${solveResponse.status}`
      } else {
        let output_board = await solveResponse.text()
        this.solveButtonText = "Solve successful"
        console.log(this.board)
        this.board = JSON.parse(output_board)
      }
    },
    updateCellValue(enteredValue, cellData) {
      this.board[cellData.row].rowEntries[cellData.col].value = enteredValue
      console.log(this.board[cellData.row].rowEntries[cellData.col])
    },
    resetBoard() {
      this.board = this.initialiseBoardData(this.boardSize)
      this.solveButtonText = "Solve"
      this.errors = ""
    }
  },
};
</script>

<style scoped>
  div.container {
    padding-top: 3vmin;
    margin: auto;
    width: 84vmin;
  }

  div.board {
    width: 80vmin;
    height: 80vmin;
    background-color: rgb(8, 146, 8);
    padding: 2vmin;
  }

  div.row {
    margin: auto;
    width: 100%;
    height: v-bind(cellWidth);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  button.bottomButtons {
    background-color: orange;
    border: none;
    color: white;
    padding: 1vmin;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 4vmin;
    margin-top: 1.5vmin;
    height: 8vmin;
    width: 40%;
    cursor: pointer;
    border-radius: 8px;
    transition-duration: .4s;
    border: 4px solid orange;
  }

  button.bottomButtons:hover {
    background-color: rgb(250, 207, 127);
    color: gray;
  }

  button.solving {
    background-color: rgb(250, 207, 127);
    cursor: default;
    color: gray;
  }

  button.resetButton {
    margin-right: 0;
    margin-left: auto;
    float: right;
  }

  div.toolbar {
    width: 100%;
    display: flex;
  }

  div.alertContainer {
    margin: auto;
    margin-bottom: 3vmin;
    width: 50vmin;
    height: 4vmin;
    padding: 0;
  }

  span.alerts {
    width: 89%;
    height: 100%;
    border-radius: 8px;
    background: #fab7b2;
    border: 2px solid #a40d02;
    margin: 0;
    padding: 0;
    display: inline-block;
  }

  button.alerts {
    border-radius: 3px;
    background: #a40d02;
    padding: 0;
    width: 10%;
    height: 100%;
    margin: 0;
    float: right;
    border: 2px solid #a40d02;
    color: white;
  }

  button.alerts:hover {
    background-color: #fab7b2;
    color: gray;
  }
</style>