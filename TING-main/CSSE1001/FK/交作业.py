def num_hours() -> float:
    '''
    return the number of hours 
    estimated spent on this assignment.
    '''
    return 15.5

def generate_initial_pieces(num_pieces:int)->Pieces:
Pieces = [ ]
        for i in range (1,num_pieces+1):
            if num_pieces < 5 or num_pieces > 9:
                pass
            else:
                Pieces.append(i)
        return Pieces
    naught_pieces = Pieces 
    cross_pieces = Pieces
    =====================================
def initial_state():
    board = [['' for column in range(3)] for row in range(3)]
    return board
print(initial_state())
-------------------------------------
# Board: list[list[str]]
def place_piece(board: Board, player:str,\
     pieces_available: Pieces, move: Move) -> None:
    row,column,piece_size = move      #unpack the move, becoming mutable
    marker = player + str(piece_size)  
    board[row][column] = marker       #list[list[str]],place the piece on the board. 
    pieces_available.remove(piece_size) #remove the piece from the list of available pieces
    
    -----------------------------------------
naught_pieces.sort()
cross_pieces.sort()
naught_pieces.formatted = ','.join(str(naught_pieces))
cross_pieces.str = ','.join(str(cross_pieces))
print('O has:', naught_pieces.formatted)
print('X has:', cross_pieces.str)

for row in range(len(board)):  #len(board) is the number of rows
    for col in range(len(board[row])):   #len(board[row]) is the number of columns
        print(' ',board[row][col],end = '')  #print the content of the current cell (either a piece or empty space)
        if col < len(board[row]) - 1:  #通过len(board[row]) - 1 来让|线在出现在每一列的前面，最后一列不出现
            print('|',end = '')
            if col == len(board[row]) -1:         #if we are at the last column of the row, print a new line
     print()  #print a new line
    if row <= len(board) - 1:
        print('-' * (4 * len(board[row]) - 1))
        ----------------------------------------------
def process_move(move: str) -> tuple[int, int, int] | None:
    move_assemblies = move.split()
    
    if len(move) != 5 or len(move_assemblies) != 3 or \
       (move[1] != ' ' or move[3] != ' '): # 如果move的长度不是5或者move_assemblies的长度不是3，说明里面可能有space
        print('Invalid_Format_MESSAGE')
        return None
  
    row = int(move_assemblies[0]) - 1  # 第一个字符是不是一个有效的row，这里的move_assemblies[0]是一个str
    if not 0 <= row < 3:   # 如果row不在0-3之间
        print('Invalid_Row_MESSAGE')
        return None
      
    col = int(move_assemblies[2]) - 1  # 第二个字符是不是一个有效的col
    if not 0 <= col < 3:
        print('Invalid_Column_MESSAGE')
        return None
      
    pieces = int(move_assemblies[4])  # move的第5个字符是不是一个有效的piece
    if not 1 <= pieces <= PIECES_PER_PLAYER:
        print('Invalid_SIZE_MESSAGE')
        return None
        
    return row, col, pieces
----------------------------------------------
def get_player_move()->Move:
    while 1:
        move = input('Enter your move')
        if move.upper() == 'H':
            print('Enter a row, column and piece size in the format: row column size')
        if len(move) != 5 or len(move_assembles)!= 3 or \
           move[2] != ' ' and move[4] != ' ': #如果move的长度不是5 或者move_assembles的长度不是3,说明里面可能有space
          print ('Invalid_Format_MESSAGE. please try again')
          continue
        row = int(move_assembles[0]) - 1  #第一个字符是不是一个有效的row,这里的move_assembles[0]是一个str
        if not 0 <= row < 3:   #如果row不在0-3之间:
          print('Invalid_Row_MESSAGE. please try again')
          continue
      
        col = int(move_assembles[2]) - 1  #第二个字符是不是一个有效的col
        if not 0 <= col < 3:
            print('Invalid_Column_MESSAGE. please try again')
            continue
        
        pieces = int(move_assembles[4]) #move的第5个字符是不是一个有效的piece
        if not 1 <= pieces <= PIECES_PER_PLAYER:
            print('Invalid_SIZE_MESSAGE. please try again')
            continue
        row -= 1
        column -= 1
    Move == row,col,pieces
    return Move
----------------------------------------------
def check_move(board: Board, pieces_available: Pieces, move: Move) -> bool:
    row, column, piece_size == move 
    if piece_size in pieces_available: #and 且的关系，采用in-built
      if board[row][column]== '' or board[row][column][-1] < piece_size:  #board[row][column][-1]相当于是[x9] 或者[O9]中的9
          
    return False
      
    ----------------------------------------------
def check_win(board:Board)->str| None:
    #check rows win based on row[0][-1]
    for row in range(3):#检查1行不同的列
        if all(piece.startswith(board[row][0]) and piece != '' for piece in range(3)):  #单元格cell 可以表示确切的棋子
        if board[row][0][0][-1] == board [row][1][0][-1] == board[row][2][0][-1]:  #
            return board[row][0][0] #win 
    #check column win based on board[0][column]
    for col in range(3): #检查1列不同的行
        if all(piece.startswith(board[row][col][0])and piece != '' for piece in range(3)):
            if board[col][0][0][-1] == board[col][1][0][-1] == board[col][2][0][-1]:
                return board[col][0][0] #win
            
    return None #no win
----------------------------------------------
def check_win(board)->str| None:
    #check rows win based on row[0][-1]
    for row in range(3):#检查1行不同的列
      if all((str(piece)).startswith(board[row][0][0]) and piece != '' for piece in range(3)):  #单元格cell 可以表示确切的棋子
        if board[row][0][0][-1] == board [row][1][0][-1] == board[row][2][0][-1]:  #
         return board[row][0][0] #win 
    #check column win based on board[0][column]
    for col in range(3): #检查1列不同的行
      if all((str(piece)).startswith(board[row][col][0][0])and piece != '' for piece in range(3)):
          if board[col][0][0][-1] == board[col][1][0][-1] == board[col][2][0][-1]:
              return board[col][0][0] #win
          
    return None #no win
board = [['O1'], ['O2'], ['O3']], [['EMPTY'], ['EMPTY'], ['EMPTY']], [['EMPTY'], ['EMPTY'], ['EMPTY']]
check_win(board)
print(check_win(board))

----------------------------------------------
def check_stalemate(board:Board, naught_pieces:Pieces, cross_pieces:Pieces)->bool:
    for row in range(len(board)):
      for col in range(len(board[row])):
        if board[row][col] != '': #如果board[row][col]不是空的，那么就是True
          
            existing_pieces = board[row][col]   #board上已经存在的棋子
            #注意比较大小的应该是value,不能是string.
            existing_pieces_value = existing_pieces[-1] # 比如是X1那么它的值就是1
            if any(piece >= existing_pieces_value for piece in cross_pieces): #检查是否有比现有棋子大的棋子,这里的piece 是new marker.
                return True
            if any(piece >= existing_pieces_value for piece in naught_pieces): #检查是否有比现有棋子大的棋子,这里的piece 是new marker.
                return True
            
    return False
          
        
              