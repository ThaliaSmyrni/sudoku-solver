board = [
  [5,3,0, 0,7,0, 0,0,0],
  [6,0,0, 1,9,5, 0,0,0],
  [0,9,8, 0,0,0, 0,6,0],

  [8,0,0, 0,6,0, 0,0,3],
  [4,0,0, 8,0,3, 0,0,1],
  [7,0,0, 0,2,0, 0,0,6],

  [0,6,0, 0,0,0, 2,8,0],
  [0,0,0, 4,1,9, 0,0,5],
  [0,0,0, 0,8,0, 0,7,9],
]
def print_board(board):
    for i in range(9):
        print(board[i])

def is_in_row(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False

def is_in_col(board, col, num):
    for i in range(9):
        if board[i][col] == num:
            return True
    return False

def is_in_block(board, row, col, num):
    startRow = row - (row % 3)
    startCol = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if board[startRow + i][startCol + j] == num:
                return True
    return False

def is_valid(board, row, col, num):
    return not is_in_row(board, row, num) and not is_in_col(board, col, num) and not is_in_block(board, row, col, num)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve(board):
    empty = find_empty(board)
    if empty is None:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

if solve(board):
    print("Λύση:")
    print_board(board)
else:
    print("Δεν υπάρχει λύση.")