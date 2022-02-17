<template>
  <div class="container">
    <div class="board">
      <div class="row" v-for="row in board" :key="row.rowNum">
        <div class="cell" v-for="entry in row.rowEntries" :key="entry.coord">
          <input class="entry" maxlength="1" size="1" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import TheBoard from "./components/TheBoard.vue"
export default {
  components: {
  },
  data() {
    return {
      boardSize: 9,
      board: this.initialiseBoardData(9),
      isSolving: false,
      solveButtonText: "Solve",
    };
  },
  computed: {
    cellWidth: function() {
      return 100 / (this.boardSize) + '%'
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
  },
};
</script>

<style scoped>
  div.container {
    padding-top: 5vmin;
  }

  div.board {
    margin: auto;
    width: 80vmin;
    height: 80vmin;
    background-color: chartreuse;
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


  div.cell {
    width: v-bind(cellWidth);
    height: 100%;
    background-color: white;
    border: 1px solid black;
  }

  input.entry {
    width: 80%;
    height: 80%;
    margin: 5%;
    border-color: white;
    font-size: 250%;
    text-align: center;
  }
</style>