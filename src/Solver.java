import java.util.Scanner;

public class Solver {

  private static Board getBoard(){
    System.out.println("With zeroes represent blank spaces,");
    System.out.println("enter a string of your current sudoku grid:");

    Scanner s = new Scanner(System.in);
    String input = s.nextLine();
    Board board = new Board(input);

    return board;
  }


  public static void main(String[] args) {

    Board board;
    Scanner s = new Scanner(System.in);
    String answer;

    do {
      board = getBoard();
      board.print();
      System.out.println("Is this your board? y/n");
      answer = s.nextLine();
    } while (!answer.equals("y"));

    s.close();
    System.out.println("Here is your solution:");
    board.start();
  }

}

