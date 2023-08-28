for l in range [2,8]:
    GRID_SIZE = l
Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int]
def check_win(board: Board) -> str | None:
    # Check rows win based on row[0]
    for row in range(GRID_SIZE):
        if all(board[row][col].startswith('X') and board[row][col] != EMPTY for col in range(GRID_SIZE)):
            if all(board[row][col][0] == 'X' for col in range(GRID_SIZE)):  # In the same column, regardless of whether it's a variable or anything else, the whole column should be the same.
                return 'X'  # 'X' wins
    
    # Check columns win based on col[0]
    for col in range(GRID_SIZE):
        if all(board[row][col].startswith('X') and board[row][col] != EMPTY for row in range(GRID_SIZE)):
            if all(board[row][col][0] == 'X' for row in range(GRID_SIZE)):
                return 'X'  # 'X' wins

    if all(board[i][i].startswith('X') and board[i][i] != EMPTY for i in range(GRID_SIZE)):
        if all(board[i][i][0] == 'X' for i in range(GRID_SIZE)):
            return 'X'
    
    # Check upper-right to lower-left diagonal
    if all(board[i][GRID_SIZE - 1 - i].startswith('X') and board[i][GRID_SIZE - 1 - i] != EMPTY for i in range(GRID_SIZE)):
        if all(board[i][GRID_SIZE - 1 - i][0] == 'X' for i in range(GRID_SIZE)):
            return 'X'
      #check 
    for row in range(GRID_SIZE):
        if all(board[row][col] == 'O' and board[row][col] != EMPTY for col in range(GRID_SIZE)):
            if all(board[row][col][0] == 'O' for col in range(GRID_SIZE)):
                return 'O'  # 'O' wins
    
    for col in range(GRID_SIZE):
        if all(board[row][col] == 'O' and board[row][col] != EMPTY for row in range(GRID_SIZE)):
            if all(board[row][col][0] == 'O' for row in range(GRID_SIZE)):
                return 'O'  # 'O' wins
    
    if all(board[i][i] == 'O' and board[i][i] != EMPTY for i in range(GRID_SIZE)):
        if all(board[i][i][0] == 'O' for i in range(GRID_SIZE)):
            return 'O'
    
    if all(board[i][GRID_SIZE - 1 - i] == 'O' and board[i][GRID_SIZE - 1 - i] != EMPTY for i in range(GRID_SIZE)):
        if all(board[i][GRID_SIZE - 1 - i][0] == 'O' for i in range(GRID_SIZE)):
            return 'O'
    
    return None  # No win
result = check_win([
    ['O1', 'O2', 'O3'],
    ['EMPTY', 'EMPTY', 'EMPTY'],
    ['EMPTY', 'EMPTY', 'EMPTY']
])
print(result)  # 'O'