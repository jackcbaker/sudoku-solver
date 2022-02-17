<template>
    <div v-bind:class="isInnerSquareEdge">
        <input class="entry" maxlength="1" size="1" v-model="cellEntry" />
    </div>
</template>

<script>
export default {
  components: {
  },
  props: ['boardSize', 'cellData'],
  data() {
    return {
      cellEntry: ""
    }
  },
  computed: {
    cellWidth: function() {
      return 100 / (this.boardSize) + '%'
    },
    isInnerSquareEdge: function() {
      return {
        'innerSquareBottom': [2, 5, 8].includes(this.cellData.row),
        'innerSquareTop': [0, 3, 6].includes(this.cellData.row),
        'innerSquareLeft': [0].includes(this.cellData.col),
        'innerSquareRight': [2, 5, 8].includes(this.cellData.col),
      }
    }
  },
  methods: {
  },
};
</script>

<style scoped>
  div {
    width: v-bind(cellWidth);
    height: 100%;
    background-color: white;
    border: 1px solid black;
  }

  div.innerSquareBottom {
    border-bottom: 5px solid black;
  }

  div.innerSquareTop {
    border-top: 5px solid black;
  }

  div.innerSquareRight {
    border-right: 5px solid black;
  }

  div.innerSquareLeft {
    border-left: 5px solid black;
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