def play_game(self)->None:
    while True:
        if self.model.has_won():
            self.display()
            print("You won!")
            return

        if self.model.has_lost():
            print("Detected loss condition")
            print("You lost!")
            break  # explicitly break out of the loop

        self.display()
        move = input("Enter move: ")

        if move == 'q':
            print("Exiting on user request")
            break
        elif move == 'u':
            self.model.undo()
        else: 
            if not self.model.attempt_move(move):
                print('Invalid move\n')
