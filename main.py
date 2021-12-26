sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def print_board(board):
    for i in range(9):
        for j in range(8):
            print(board[i][j], end="  ")
        print(board[i][8], end='\n')


def row_check(board, value, row):
    if value in board[row]:
        return False
        # print("repeating value found") \\ used for testing
    else:
        return True
        # print("you are free to add value") \\ used for testing


def column_check(board, value, column):
    for i in range(9):
        if value == board[i][column]:
            return False
            # return "value already exists" \\ used for testing
    return True
    # return"value is free to add" \\ used for testing


def cell_check(board, value, column, row):
    cell_row = row // 3
    cell_column = column // 3

    for i in range(cell_row*3, cell_row + 3):
        for j in range(cell_column*3, cell_column + 3):
            if value == board[i][j]:
                return False
                # return "value found" \\ used for testing
    return True
    # return "value was not found, put it there" \\ used for testing


def constraint_check(board, value, column, row):
    if row_check(board, value, row) and \
            column_check(board, value, column) and \
            cell_check(board, value, column, row):
        return True
    else:
        return False


def solve(board):
    empty_pos = find_empty(board)
    if not empty_pos:
        return True
    else:
        row, column = empty_pos

    for i in range(1, 10):
        if constraint_check(board, i, column, row):
            board[row][column] = i

            if solve(board):
                return True

            board[row][column] = 0


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


print_board(sudoku_board)

print("-------------------------")

solve(sudoku_board)

print_board(sudoku_board)
