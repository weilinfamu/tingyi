board[row][column][第一个字符]
board[0] 是第一行，也就是 ['O1'] 这个列表。
board[0][0] 行  列  
board[0][0][0] 行 列  字符为x
#相当于 board[0][0][X]
也可以是board[0][0][0][-1] 行 列 字符串最后一个字符为1
第一行    board
for row in range(len(board))  # 相当于把len(board)看成一个数，比如说4，然后 范围就是0,1,2,3
len(board[row])  #board[row] 表示取出其中的第 row 行，然后 len(board[row]) 就返回这一行的长度
GRID_SIZE[0]表示 行数
GRID_SIZE[1]代表列书数， #第二个元素


