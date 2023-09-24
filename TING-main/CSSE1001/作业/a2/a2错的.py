
from a2_support import *
Grid 
Entities 
Position 
# Tile constants
WALL 
FLOOR 
GOAL 
FILLED_GOAL 

# Entity constants
CRATE 
PLAYER 
STRENGTH_POTION
MOVE_POTION 
FANCY_POTION 

# Movement constants
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'

DIRECTION_DELTAS = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1),
}



# Write your classes here

     
class Tile:
    def is_blocking(self) -> bool:
        return False

    def get_type(self) -> str:
        return 'Abstract Tile'

    def __str__(self) -> str:
        return self.get_type()

    def __repr__(self) -> str:
        return self.get_type()
    
class Floor(Tile):
    """
    A class for floor tiles in the game is a subclass of Tile and 
    can be moved onto by the player and crates.
    """
    def is_blocking(self) -> bool:
     """
     check if the floor is blocking 
     and set it is not blocking
     """
     return False
    def __repr__(self):
        return ' '
    """ 
    get the representation of the floor
    """

    def get_type(self) -> str:
        return ' '
    """ 
    get the type of the floor
    """
    def __str__(self) -> str:
        return ' '
    """get the type of the floor tile
    """
class Wall(Tile):
    """ 
    A class for wall tiles in the game is a subclass of Tile and
    cannot be moved onto by the player and crates."""
    def is_blocking(self) -> bool:
        return True
    """ 
    it is blocking
    """
    def __repr__(self):
        return 'W'
    """ 
    get the representation of the wall
    """
    def get_type(self) -> str:      
        #being represent as 'W'
        """ 
        get the type of the wall
        """
        return 'W'   
    def __str__(self):
        """ 
        get the type of the wall tile
        """
        return 'W' 
    
        

class Goal(Tile):
    """ 
    A class for goal tiles in the game is a subclass of Tile and it is the condition of winning the game.
    """
    def is_blocking(self)->bool:
        return False
    """
    it is blocking
    """
    def get_type(self) -> str:
        return 'G'
    """ 
    get the type of the goal
    """
    
    def __init__(self):     # Initialize as unfilled
        self.filled = False
        """ 
        Initialize as unfilled
        """
    def unfill(self):
        self.filled = False
        """
        Unfill the goal
        """

    def fill(self)->None:
        self.filled = True # Fill the goal
        """ 
        Fill the goal
        """
    def is_filled(self)->bool:
        return self.filled       # Return whether the goal is filled based on self.filled
    """ 
    Return whether the goal is filled based on self.filled
    """
    def __str__(self):
        return 'X' if self.filled else 'G'
    """ 
    get the type of the goal tile
    """
    
    def __repr__(self) -> str:
        """
        get the representation of the goal
        """
        return self.__str__()


    """ 
    An abstract class for 
    all entities in the game.
    """
class Entity:  
    def __init__(self):
        """ 
        Initialize the entity
        """
        self.movable = False
    def get_type(self) -> str:
        
        return "Abstract Entity"
    def is_movable(self) -> bool:
        return self.movable
    def __str__(self) -> str:
        return "Abstract Entity"
    def __repr__(self) -> str:
        return "Abstract Entity"
class Crate(Entity):
    def __init__ (self, strength:int)->None:
        """
        call the parent initializer
        """
        super(). __init__()
        if 0 <= strength <= 9:
            self.strength = strength
            """ 
           the crates value is between 0 and 9
            """
    def get_strength(self)->int:
        """ 
        try to set the strength of the crate that player need to push   
        """
        return self.strength
        
    def __repr__(self)->str:
        """ 
        get the representation of the crate
        """
        return str(self.strength)
        
    def get_type(self)->str:
        """ 
        get the type of the crate
         """
        return 'C'
       
    def __str__(self)->str:
        return str(self.strength)   #string version of strength
    def is_movable(self)->bool:
        """ 
        check if the crate is movable
        """
        return True
class Potion:
    def __init__(self)->None:
        super(). __init__()
        """ 
        call the parent initializer
        """
    def get_type(self)->str:
        """ 
        get the type of the potion
        """
        return 'Potion'
    def is_movable(self)->bool:
        return False
    def __repr__(self)->str:
        return self.get_type()
    
    def effect(self)->dict[str,int]:
        """ 
        get the effect of the potion, 
        and each str should  be respective to its value
        """
        return {}
class StrengthPotion(Potion):
    """ 
    a subclass of Potion and it can increase 
    the strength of player
    """
    def __init__(self)->None:
        super(). __init__()
        """ 
        call the parent initializer
        """
    def get_type(self)->str:
        return 'S'
    def __repr__(self) -> str:
        return 'S'
    def is_movable(self)->bool:
        return False
    """ 
    check if the potion is movable
    """
    def effect(self)->dict[str,int]:
        return {'strength': 2}
    """ 
    get the effect of the potion,providing additional 2 strength
    """
    def __str__(self) -> str:
        return self.get_type()
class MovePotion(Potion):
    """ 
    a subclass of Potion and it can increase
    the moves of player"""
    def __init__(self)->None:
        super(). __init__()
    def get_type(self)->str:
        return 'M'
    def __repr__(self) -> str:
        return 'M'
    def is_movable(self)->bool:
        return False
    def effect(self)->dict[str,int]:
        return {'moves': 5}
    """ 
    get the effect of the potion,providing additional 5 moves
    """
    def __str__(self) -> str:
        return self.get_type()
class FancyPotion(Potion):
    def __init__(self)->None:
        super(). __init__()
    def __repr__(self) -> str:
        return 'F'
    def get_type(self)->str:
        return 'F'
    def is_movable(self)->bool:
        return False
    def effect(self)->dict[str,int]:
        return {'strength': 2, 'moves': 2}
    """ 
    get the effect of the potion,providing additional 2 strength and 2 moves
    """
    def __str__(self)->str:
        return self.get_type()
class Player:
    def __init__(self, start_strength: int, moves_remaining: int)->None:   #initialize an instance of Player
        """
        player's initial strength and moves,
        and set the player is movable if moves_remaining > 0"""                                       
        self.strength = start_strength
        self.moves = moves_remaining
        self.movable = moves_remaining > 0    # is that false? just to check in gradescope.
       
    def is_movable(self)->bool:
        """ 
        check if the player is movable
        """
        return self.movable
    def get_type(self)->str:
        return 'P'              #being represent as 'P'
    def __repr__(self) -> str:
        return 'P'
    def __str__(self) -> str:
        return 'P'
    def get_strength(self)->int:            #the current  strength of player
        return self.strength               #return the strength of player
    def add_strength(self,amount:int)->None: 
        self.strength += amount                 #add strength to player
    def get_moves_remaining(self)->int:   #player's current moves
        return self.moves
    def add_moves_remaining(self,amount:int)->None:         #add moves to player
         
        self.moves + amount
      
    def apply_effect(self,potion_effect:dict[str,int])->None:      #apply the effect of potion
          
            if 'strength' in potion_effect:
               self.add_strength(potion_effect['strength'])
            if 'moves' in potion_effect:
               self.add_moves_remaining(potion_effect['moves'])
            
def convert_maze(game: list[list[str]]) -> tuple[Grid, Entities, Position]:
    grid = []
    entities = {}
    player_position = ()

    for row_idx, row in enumerate(game):
        grid_row = []
        for col_idx, i in enumerate(row):
            if i == 'W':
                grid_row.append(Wall())
            elif i == ' ':
                grid_row.append(Floor())
            elif i == 'G':
                grid_row.append(Goal())
            elif i.isdigit():  # Checks if the character is a digit
                 if 1 <= int(i) <= 9:
                    entities[(row_idx, col_idx)] = Crate(int(i))
                    grid_row.append(Floor())  # Use Floor for the space where Crate is

                
            elif i == 'S':
                entities[(row_idx, col_idx)] = StrengthPotion()
                grid_row.append(Floor())
            elif i == 'M':
                entities[(row_idx, col_idx)] = MovePotion()
                grid_row.append(Floor())
            elif i == 'F':
                entities[(row_idx, col_idx)] = FancyPotion()
                grid_row.append(Floor())
            elif i == 'P':
                player_position = (row_idx, col_idx)  # Set player position
                grid_row.append(Floor())

        grid.append(grid_row)  # Append each grid_row to grid at the end of the inner loop

    return grid, entities, player_position

                
            
       

class SokobanModel:
    def __init__(self, maze_file:str)->None:
        raw_maze, player_stats = read_file(maze_file)
        self.maze,self.entities,self.player_position = convert_maze(raw_maze)
        self.previous_states = []
        
        
        self.player = Player(player_stats[0],player_stats[1])                 # a list of player's remaining strength and remaining moves
 
      
    def get_game_stats(self):
        game_stats = {
            'maze': self.get_maze(),
            'entities': self.get_entities(),
            'player_position': self.get_player_position(),
            'player_moves_remaining': self.get_player_moves_remaining(),
            'player_strength': self.get_player_strength(),
            'has_won': self.has_won(),
            'has_lost': self.has_lost()
            }
        return game_stats
         
    def get_maze(self)->Grid:
        return self.maze
    def get_entities(self)->Entities:
        return self.entities   
    def get_player_position(self)->tuple[int,int]:
        return self.player_position                      #get the current position of player
    def get_player_moves_remaining(self)->int:     
        return self.player.get_moves_remaining()                    #get the current moves of player
    def get_player_strength(self)->int:
        return self.player.get_strength()                  #get the current strength of player
      
    def attempt_move(self, direction: str) -> bool:
    
        if direction not in DIRECTION_DELTAS:
            return False

        (row_offset, col_offset) = DIRECTION_DELTAS[direction]

        if self.player.get_moves_remaining() <= 0:
            return False
        (row, col) = (self.player_position[0], self.player_position[1])
        new_row, new_col = self.player_position[0] + row_offset, self.player_position[1] + col_offset

        # check border
        if not 0 <= new_row < len(self.maze) or not 0 <= new_col < len(self.maze[0]):
            return False

        # check the wall
        if isinstance(self.maze[new_row][new_col], Wall):
            return False

        # check the crate
        Crate_new_pos = self.entities.get((new_row, new_col))   #the first crate on the new position
        
        if isinstance(Crate_new_pos, Crate):
           
            if self.player.get_strength() < Crate_new_pos.get_strength():
                return False
            
            # check the boarder and some basic conditions
            if (
                not 0 <= new_row + row_offset < len(self.maze)
                or not 0 <= new_col + col_offset < len(self.maze[0])
                or isinstance(self.maze[new_row + row_offset][new_col + col_offset], Wall)
             ):

                return False
                #goal is filled
            del self.entities[(new_row, new_col)]
            self.entities[(new_row + row_offset, new_col + col_offset)] = Crate_new_pos  #new crate on the new position
            if isinstance(self.maze[new_row + row_offset][new_col + col_offset], Goal):
                
                self.maze[new_row + row_offset][new_col + col_offset].fill()
                
                del self.entities[(new_row + row_offset, new_col + col_offset)]
                # player's position

        # potions
        potion = self.entities.get((new_row, new_col))
        if isinstance(potion, Potion):
            self.player.apply_effect(potion.effect())
            # get potions
            del self.entities[(new_row, new_col)]
           
            # all done

        self.player.add_moves_remaining(-1) 
        self.player_position = (new_row, new_col)
      
        return True
  
    
    def has_won(self) -> bool:
        for row in self.maze:
            for i in row:
                if isinstance(i, Goal) and not i.is_filled():
                    return False
        return True                    
    def has_lost(self) -> bool:
        if self.player.get_moves_remaining() < 1:
            return True
        return False

class Sokoban:
    def __init__(self, maze_file:str)->None:
      self.model = SokobanModel(maze_file)   
      self.view = SokobanView()
      
    # Display the current state of the game.
    def display(self) -> None:
       game_stats = self.model.get_game_stats()  
       # Calling display_game with correct arguments
       self.view.display_game(game_stats['maze'], game_stats['entities'], game_stats['player_position'])
       self.view.display_stats(game_stats['player_moves_remaining'], game_stats['player_strength'])
       
        # Display you win or you lost these hints.
    def play_game(self)->None:
        while True:
            # Check win/loss conditions after displaying the current state.
            if self.model.has_won():
                self.display()
                print("You won!")
                return

            if self.model.has_lost():
                print("You lost!")
                return
            self.display()
            move = input("Enter move: ")
            
          
            if move == 'q':
                return
            elif move == 'u':
                self.model.undo()
            else: 
                if not self.model.attempt_move(move):
                    print('Invalid move\n')


              

def main():
        
            
        
    game = Sokoban('maze_files/maze1.txt')

    game.play_game()
        
if __name__ == '__main__':
        main()
