

def solve_board(board):
    def check_box(row, col, num):
        row = row - (row % 3)
        col = col - (col % 3)
    
        for x in range(0, 3):
            for y in range (0, 3):
                if board[row + x][col + y] == num:
                    return False
        return True
    

    def check_col(col, num):
        for row in range(9):
            if board[row][col] == num:
                return False
        return True
    

    def check_row(row, num):
        for col in range(9):
            if board[row][col] == num:
                return False
        return True

    def do_checks(row, col, num):
        return check_row(row, num) and check_col(col, num) and check_box(row, col, num)


    def solve_next(row, col):
        if col < 8:
            solve(row, col + 1)
        else:
            solve(row + 1, 0)


    def solve(row, col):
        if row > 8 :
            print(board)
            return board
        elif board[row][col] != 0:
            solve_next(row, col)
        else:
            for num in range(1, 10):
                if do_checks(row, col, num):
                    board[row][col] = num
                    solve_next(row, col)
            board[row][col] = 0

    return solve(0,0)

    
def turn_into_board(arr):
    board = [[arr[x+9*y] for x in range(9)] for y in range(9)]
    return board


def main():
    board = turn_into_board([0, 0, 0, 6, 0, 4, 7, 0, 0, 
                             7, 0, 6, 0, 0, 0, 0, 0, 9,
                             0, 0, 0, 0, 0, 5, 0, 8, 0,
                             0, 7, 0, 0, 2, 0, 0, 9, 3,
                             8, 0, 0, 0, 0, 0, 0, 0, 5,
                             4, 3, 0, 0, 1, 0, 0, 7, 0, 
                             0, 5, 0, 2, 0, 0, 0, 0, 0,
                             3, 0, 0, 0, 0, 0, 2, 0, 8,
                             0, 0, 2, 3, 0, 1, 0, 0, 0])
    board = solve_board(board)


if __name__ == '__main__':
    main()
