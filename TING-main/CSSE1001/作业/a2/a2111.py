
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
    """ 
    an abstract class for wall floor goal.
    """
    def is_blocking(self) -> bool:
        """Return True if this tile blocks movement, else False."""
        return False

    def get_type(self) -> str:
        """Return a string representing the type of this tile."""
        return 'Abstract Tile'

    def __str__(self) -> str:
        """ ensure that the type of the tile is a string"""
        return self.get_type()

    def __repr__(self) -> str:
        """Return a string representation of this tile (used for debugging)."""
        return self.get_type()
    
class Floor(Tile):
    """
   Class for floor tiles in the game. 
   Players and crates can move onto them.
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
    and it is not blocking
    """
class Wall(Tile):
    """ 
    A class for wall tiles in the game is a subclass of Tile and
    They block movement
    """
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
        a string representing the type of this tile ('W')
        """
        return 'W'   
    def __str__(self):
        """ 
        get the type of the wall tile
        """
        return 'W' 
    
        

class Goal(Tile):
    """ 
    Class for goal tiles in the game. Crates must be pushed onto these to win
    """
    def is_blocking(self)->bool:
        return False
    """
    it is not blocking
    """
    def get_type(self) -> str:
        return 'G'
    """ 
    a string representing the type of this tile ('G')
    """
    
    def __init__(self):    
         # Initialize as unfilled
        self.filled = False
        self.unfilled = True
        """ 
        Initialize as unfilled
        """
    def unfill(self):
        """Unfill the goal, usually for an undo operation."""
        self.filled = False
        """
        the goal is unfilled used for undo.
        """

    def fill(self)->None:
        """ 
        Fill the goal tile.
        """
        self.filled = True # Fill the goal
        
    def is_filled(self)->bool:
        """ 
        Return whether the goal is filled based on self.filled
        """
        return self.filled       
    
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

#define the Entity class and its subclasses   
class Entity:  
    """ 
    An abstract class for 
    all entities in the game.
    """
    def __init__(self):
        """ 
        Initialize the entity
        """
        
    def get_type(self) -> str:
        """Returns a string representing the type of the entity."""
        return "Abstract Entity"
    def is_movable(self) -> bool:
        """Returns True if the entity is movable, False otherwise."""
        return False
    def __str__(self) -> str:
        return "Abstract Entity"
    def __repr__(self) -> str:
        return "Abstract Entity"
    
class Crate(Entity):
    """Class for crate entities in the game."""
    def __init__ (self, strength:int)->None:
        """
        call the parent initializer
        strength (int): The strength value of the crate (0 <= strength <= 9).
        
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
        #string version of strength
        return str(self.strength)   
    def is_movable(self)->bool:
        """ 
        Return True, as crates can be moved.
        """
        return True
    
 # Define the Potion class and its subclasses
class Potion:
    """A class representing a basic potion."""
    def __init__(self)->None:
        """Initialize a Potion object."""
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
        """Returns False, as basic potions are not movable."""
        return False
    def __repr__(self)->str:
        """Return a string representation of this potion."""
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
        """Return a string representing the type of this potion ('S')"""
        return 'S'
    def __repr__(self) -> str:
        """Return a string representation of this strength potion ('S')."""
        return 'S'
    def is_movable(self)->bool:
        """Return False, as strength potions are not movable."""
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
# Define the MovePotion and FancyPotion classes (similar to StrengthPotion)
class MovePotion(Potion):
    """ 
    a subclass of Potion and it can increase
    the moves of player
    """
    def __init__(self)->None:
        super(). __init__()
    def get_type(self)->str:
        """Return a string representing the type of this entity"""
        return 'M'
    def __repr__(self) -> str:
        """Return a string representation of this player entity ."""
        return 'M'
    def is_movable(self)->bool:
        """Return True if the player can make moves (moves > 0), else False."""
        return False
    def effect(self)->dict[str,int]:
        return {'moves': 5}
    """ 
    get the effect of the potion,providing additional 5 moves
    """
    def __str__(self) -> str:
        return self.get_type()
class FancyPotion(Potion):
    """A special kind of potion that provides multiple effects."""
    def __init__(self)->None:
        super(). __init__()
    def __repr__(self) -> str:
        return 'F'
    def get_type(self)->str:
        return 'F'
    def is_movable(self)->bool:
        """Returns False, as fancy potions are not movable."""
        return False
    def effect(self)->dict[str,int]:
        return {'strength': 2, 'moves': 2}
    """ 
    get the effect of the potion,providing additional 2 strength and 2 moves
    return: A dictionary containing the effects on strength and moves.
    """
    def __str__(self)->str:
        return self.get_type()
class Player:
    """
    The Player class represents the player character in the game.

    It maintains the player's current strength and remaining moves,
    and provides methods to modify these attributes.
    """
    #initialize an instance of Player
    def __init__(self, start_strength: int, moves_remaining: int)->None:   
        """
        player's initial strength and moves,
        and set the player is movable if moves_remaining > 0
        """                                       
        self.strength = start_strength 
        self.moves = moves_remaining
          
        """ 
        check if the player is movable
        """
    def is_movable(self)->bool:
        """ 
        check if the player is movable
        return: True if the player can move, False otherwise.
        """
        return self.moves > 0
    def get_type(self)->str:
        """Returns a string that represents the player entity."""
        return 'P' 
   
    def __repr__(self) -> str:
        return 'P'
    def __str__(self) -> str:
        return 'P'
    def get_strength(self)->int: 
        """
        Get the current strength of the player.
        :return: An integer representing player's current strength.
        """
        #return the strength of player
        return self.strength               
    def add_strength(self,amount:int)->None: 
        """
        Add strength to the player.
        param amount: The amount of strength to add.
        """
        #add strength to player
        self.strength += amount   
        #player's current moves
    def get_moves_remaining(self)->int:   
        """
        Get the number of moves remaining for the player.
        return: An integer representing the moves remaining.
        """
        return self.moves
    #add moves to player
    def add_moves_remaining(self,amount:int)->None:         
            """
            Add moves to the player.
            param amount: The amount of moves to add, can be negative.
            """
             #moves can be negative
            self.moves += amount                           
             #apply the effect of potion
    def apply_effect(self,potion_effect:dict[str,int])->None:     
            """
            Apply the effects of a potion to the player.
            param potion_effect: A dictionary containing the effects to apply.
            """
            if 'strength' in potion_effect:
               self.add_strength(potion_effect['strength'])
            if 'moves' in potion_effect:
               self.add_moves_remaining(potion_effect['moves'])
            
def convert_maze(game: list[list[str]]) -> tuple[Grid, Entities, Position]:
    """
    Converts the raw game maze to a more structured format.
    param game: A 2D list containing the raw maze information.
    return: A tuple consisting of the maze grid, entities dictionary, and player position.
    """
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
                # Checks if the character is a digit
            elif i.isdigit():  
                 if 1 <= int(i) <= 9:
                    entities[(row_idx, col_idx)] = Crate(int(i))
                    # Use Floor for the space where Crate is
                    grid_row.append(Floor())  

                
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
                # Set player position
                player_position = (row_idx, col_idx)  
                grid_row.append(Floor())
         # Append each grid_row to grid at the end of the inner loop
        grid.append(grid_row) 

    return grid, entities, player_position

                
            
       

class SokobanModel:
    """ 
    in order to store and undo, some variables need to be create including 
    self.prev_crate_position,self.prev_moved_crate_position,  self.prev_potion_position,
    self.prev_player_position,self.player_last_moves
    """
    def __init__(self, maze_file:str)->None:
        """
        Initialize the Sokoban model by reading the maze file.
        param maze_file: The file path for the maze configuration.
        """
        raw_maze, player_stats = read_file(maze_file)
        self.maze,self.entities,self.player_position = convert_maze(raw_maze)
        #the previous position of crate
        self.prev_crate_position = None      
          #the previous position of crate that has been moved
        self.prev_moved_crate_position = None
        #the previous position of potion
        self.prev_potion_position = None      
        self.prev_player_position = None
         # a list of player's remaining strength and remaining moves
        self.player = Player(player_stats[0],player_stats[1])                
        self.player_last_moves = None     
        self.prev_potion_effect = None   
        self. last_strength= None
        self.potion_effects = {}
        
    def get_game_stats(self):   
        """ 
        Retrieve all the current game stats to be displayed.      
        return: A dictionary containing all the relevant game stats.
        """
        
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
        """
        Returns the current maze configuration.  
        return: The grid representing the maze.
        """
        return self.maze
    def get_entities(self)->Entities:
        """
        Returns the current entities in the maze.
        return: The dictionary of entities in the maze.
        """
        return self.entities   
    def get_player_position(self)->tuple[int,int]:
        """
        Returns the current position of the player in the maze.
        return: A tuple representing the player's row and column position.
        """
        return self.player_position       
    #get the current position of player               
    def get_player_moves_remaining(self)->int: 
        """
        Returns the number of moves remaining for the player.
        return: The number of moves remaining.
        """    
        return self.player.get_moves_remaining()                  
    def get_player_strength(self)->int:
        """
        Returns the current strength of the player.
        return: The strength of the player.
        """
        return self.player.get_strength()                 
      
    def attempt_move(self, direction: str) -> bool:
        """ 
        some of the basic condition before player moves
        """
          # Testify the move direction
        if direction not in DIRECTION_DELTAS:  
             #other directions that are invalid
            return False

        (row_offset, col_offset) = DIRECTION_DELTAS[direction]

        if self.player.get_moves_remaining() <= 0:
            return False
        # the original position of player
        (row, col) = (self.player_position[0], self.player_position[1])   
         # store the initial  player position
        self.prev_player_position = (row, col)   
        # the new position of player
        new_row, new_col = self.player_position[0] + row_offset, self.player_position[1] + col_offset 
        # Record the player position
        self.player_last_moves = (new_row, new_col)  
        self.player.add_moves_remaining(-1)
        # check border
        if not 0 <= new_row < len(self.maze) or not 0 <= new_col < len(self.maze[0]):
            return False

        # check the wall
        if isinstance(self.maze[new_row][new_col], Wall):
            return False

        # check the crate
        """ 
        crate_pos is the first crate's position and is also the removed crate's position latter on
        """
         #the name of first crate 
        crate_pos = self.entities.get((new_row, new_col))  
        
        if isinstance(crate_pos, Crate):
            #the previous position of crate
            self.prev_crate_position =  (new_row, new_col)   
            if self.player.get_strength() < crate_pos.get_strength():
                return False
            
            # check the boarder and some basic conditions
            if (
                not 0 <= new_row + row_offset < len(self.maze)
                or not 0 <= new_col + col_offset < len(self.maze[0])
                or isinstance(self.maze[new_row + row_offset][new_col + col_offset], Wall)
             ):

                return False
            """ 
             self.prev_crate_position is the first crate's position
             self.prev_moved_crate_position is the moved crate's position after the first position
            """
                #remove the crate
            self.entities.pop((new_row, new_col))
            #new crate on the new position
            self.entities[(new_row + row_offset, new_col + col_offset)] = crate_pos  
            #the previous position of crate that has been moved
            self.prev_moved_crate_position = (new_row + row_offset, new_col + col_offset)  
            self.player.add_moves_remaining(-1)
                #goal
            if isinstance(self.maze[new_row + row_offset][new_col + col_offset], Goal):
                """  
                check and fill goal
                """
                self.maze[new_row + row_offset][new_col + col_offset].fill()
                #remove the crate from the filled floor
                self.entities.pop((new_row + row_offset, new_col + col_offset))   
                # player's position
              
        """
        while get potion, you need delete it from the maze,record the effect of potion try to decrease latter on 
        self.prev_potion_position is the previous position of potion
        self.potion_effects as a {}
        """
        # potions
        potion = self.entities.get((new_row, new_col))
        if isinstance(potion, Potion):
            #store the potion effects into {},and potion.effect is also a documentary store strength and moves
            effect_dic = potion.effect()
            if 'strength' in effect_dic:
                self.player.add_strength(effect_dic['strength'])
            if 'moves' in effect_dic:
                self.player.add_moves_remaining(effect_dic['moves'])
            
            # Record the potion's effect at the current position, which is another {}
            self.potion_effects[(new_row, new_col)] = effect_dic
            
            # Update the previous potion position and store it into self.prev_potion_position
            self.prev_potion_position = (new_row, new_col) 
            
            # Apply the general effects of the potion (if any other attributes need to be affected)
            self.player.apply_effect(effect_dic)
            
            # Remove the potion from the entities since it has been consumed
            self.entities.pop((new_row, new_col))
            self.player.add_moves_remaining(-1)
            # all done
        self.player_position = (new_row, new_col)

        return True
    
    def undo(self)->None:
        """
       try to divide into three parts, player, crate and potion
        """ 
          # player
        if  self.prev_player_position:
                self.player_position = self.prev_player_position
                self.player.add_moves_remaining(+1) 
        # crate
        #crate on the previous position
        if self.prev_crate_position and self.prev_moved_crate_position:     
            #crate on the moved position
            last_crate = self.entities.pop(self.prev_moved_crate_position)    
            self.entities[self.prev_crate_position]= last_crate
            self.player.add_moves_remaining(+1) 
            """ 
            make the filled goal unfilled
            """
            if isinstance(self.maze[self.prev_moved_crate_position[0]][self.prev_moved_crate_position[1]], Goal):
              self.maze[self.prev_moved_crate_position[0]][self.prev_moved_crate_position[1]].unfill()     
        """ 
        Restore consumed potion:
        """ 
        # whether exist potion on the previous position
        if  self.prev_potion_position:      
             effect_dic = self.potion_effects.get(self.prev_potion_position)
             if effect_dic:
                if 'moves' in effect_dic:
                    self.player.add_moves_remaining(-effect_dic['moves'])     
                if 'strength' in effect_dic:
                    self.player.add_strength(-effect_dic['strength'])
                    self.potion_effects[self.prev_potion_position].pop()
            
            

            

        """
        Reset the recorded previous state for crate and potion:
        """
        self.prev_crate_position = None
        self.prev_crate_moved_position = None
        self.prev_potion_position = None
        
    def has_won(self) -> bool:
        """Checks if the player has won the game."""
        for row in self.maze:
            for i in row:
                if isinstance(i, Goal) and not i.is_filled():
                    return False
        return True                    
    def has_lost(self) -> bool:
        """Checks if the player has lost the game."""
        if self.player.get_moves_remaining() < 1:
            return True
        return False

class Sokoban:
    """The main class that controls the Sokoban game logic and display."""
    def __init__(self, maze_file:str)->None:
      """
        Initialize the Sokoban game with a specified maze file.
        maze_file (str): The path to the file containing the maze layout and player stats.
      """
      self.model = SokobanModel(maze_file)   
      self.view = SokobanView()
      
    # Display the current state of the game.
    def display(self) -> None:
       """Display the current state of the game."""
       game_stats = self.model.get_game_stats()  
       # Calling display_game with correct arguments
       self.view.display_game(game_stats['maze'], game_stats['entities'], game_stats['player_position'])
       self.view.display_stats(game_stats['player_moves_remaining'], game_stats['player_strength'])
       
        # Display you win or you lost.
    def play_game(self) -> None:
        """Play the Sokoban game until a win or loss condition is met."""
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
