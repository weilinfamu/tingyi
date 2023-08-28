def generate_initial_pieces(num_pieces:int):
    pieces = [ ]
    if 5 < num_pieces < 9:
      for i in range (1,num_pieces+1):
        pieces.append(i)
      return pieces
-------------------------------------