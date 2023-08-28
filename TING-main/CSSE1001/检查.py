def get_player_move():
    while True:
        try:
            move = input('Enter your move: ')
            move_assemblies = move.split()

            if len(move_assemblies) == 1 and move_assemblies[0].upper() == 'H':
                print('HELP_MESSAGE')
                continue

            if len(move_assemblies) != 3 or \
               not move_assemblies[0].isdigit() or \
               not move_assemblies[1].isdigit() or \
               not move_assemblies[2].isdigit():
                print('Invalid move format. Please try again.')
                continue

            row = int(move_assemblies[0]) - 1
            col = int(move_assemblies[1]) - 1

            if not (0 <= row < 3 and 0 <= col < 3):
                print('Invalid row. Please try again.')
                continue

            pieces = int(move_assemblies[2])

            if not (1 <= pieces <= PIECES_PER_PLAYER):
                print('Invalid piece size. Please try again.')
                continue

            return (row, col, pieces)

        except ValueError:
            # Handle non-integer inputs
            print('Invalid input. Please enter a valid move.')
            continue
               
        
        
    
