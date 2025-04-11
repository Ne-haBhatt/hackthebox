def read_sudoku():
    board = []
    for _ in range(100):
        row = [c for c in input().strip() if c in '123456789.']
        if len(row) != 9: 
            continue
        board.append(row)
        if len(board) == 9:
            break
    return board
def is_valid(board, r, c, num):
    return all(num != board[r][i] for i in range(9)) and \
          all(num != board[i][c] for i in range(9)) and \
          all(num != board[r//3*3 + i//3][c//3*3 + i%3] for i in range(9))
def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                for num in '123456789':
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        if solve(board):
                            return True
                        board[r][c] = '.'
                return False
    return True
def print_sudoku(board):
    print("+-------+-------+-------+")
    for i, row in enumerate(board):
        print(f"| {' '.join(row[:3])} | {' '.join(row[3:6])} | {' '.join(row[6:])} | ")
        if i % 3 == 2: print("+-------+-------+-------+")
board = read_sudoku()
solve(board)
print_sudoku(board)
