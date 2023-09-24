def play_game(self)->None:
        while True:
            # Always display the current game state at the start of the loop.
            self.display()

            # Check win/loss conditions after displaying the current state.
            if self.model.has_won():
                print("You won!")
                return

            if self.model.has_lost():
                print("You lost!")
                return

            move = input("Enter move: ")

            if move == 'q':
                return
            elif move == 'u':
                self.model.undo()
            else: 
                if not self.model.attempt_move(move):
                    print('Invalid move\n')

