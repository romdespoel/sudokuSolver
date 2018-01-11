public class Board {


  int[][] board;

  public Board(String s) {

    board = new int[9][9];

    if(s.length() != 9*9 ){
      System.out.println("Your grid has the wrong amount of numbers.");
      System.exit(1);
    }

    int index = 0;

    for (int y = 0; y < 9; y++) {
      for (int x = 0; x < 9; x++) {
        board[y][x] = Integer.parseInt(s.substring(index, index + 1));
        index++;

      }
    }
  }


  public void print() {
    System.out.println("______________________");

    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[i].length; j++) {

        System.out.print(board[i][j] + " ");
        if (j % 3 == 2) {
          System.out.print("| ");
        }
      }
      System.out.println();
      if ((i + 1) % 3 == 0) {
        System.out.println("______________________");
      }

    }
  }

  private boolean checkBox(int row, int col, int num) {
    row = row - (row % 3);
    col = col - (col % 3);

    for (int x = 0; x < 3; x++) {
      for (int y = 0; y < 3; y++) {

        if (board[row + x][col + y] == num) {
          return false;
        }

      }
    }

    return true;
  }

  private boolean checkCol(int col, int num) {

    for (int row = 0; row < 9; row++) {
      if (board[row][col] == num) {
        return false;
      }
    }
    return true;
  }

  private boolean checkRow(int row, int num) {

    for (int col = 0; col < 9; col++) {
      if (board[row][col] == num) {
        return false;
      }
    }
    return true;
  }

  private void next(int row, int col) {

    if (col < 8) {
      solve(row, col + 1);
    } else {
      solve(row + 1, 0);
    }
  }

  public void start(){
    solve(0, 0);
  }

  private void solve(int row, int col) {

    if (row > 8) {
      print();

    } else if (board[row][col] != 0) {
      next(row, col);

    } else {
      for (int i = 1; i < 10; i++) {
        if (checkBox(row, col, i) && checkRow(row, i) && checkCol(col, i)) {
          board[row][col] = i;
          next(row, col);
        }
      }
      board[row][col] = 0;
    }
  }


}
