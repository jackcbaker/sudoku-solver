<template>
  <div class="container">
    <div class="board">
      <div class="row" v-for="row in board" :key="row.rowNum">
        <base-cell v-for="entry in row.rowEntries" :key="entry.coord" :cellData=entry :boardSize=boardSize>
        </base-cell>
      </div>
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
</style>