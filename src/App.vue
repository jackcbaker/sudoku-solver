<template>
  <div v-for="row in board" :key="row.rowNum">
    <li v-for="entry in row.rowEntries" :key="entry.coord">
      Entry {{ entry.coord }} has value {{ entry.value }}
    </li>
  </div>
</template>

<script>
// import TheBoard from "./components/TheBoard.vue"
export default {
  components: {
  },
  data() {
    return {
      board: this.initialiseBoardData(9),
      isSolving: false,
      solveButtonText: "Solve",
    };
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