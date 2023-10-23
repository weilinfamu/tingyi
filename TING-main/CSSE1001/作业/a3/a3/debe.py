import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable, Union
from model import SokobanModel, Tile, Entity
from a2_support import *
from a3_support import *
COIN = '$'


class FancyGameView(AbstractGrid):
    def __init__(self, master: tk.Frame | tk.Tk,\
                  dimensions: tuple [int,int], size:tuple[int,int],\
                    **kwargs) -> None:
          """Sets up the FancyGameView to be an AbstractGrid with the appropriate dimensions and size, 
            and creates an instance attribute of an empty dictionary to be used as an image cache."""
          super().__init__(master,dimensions,size=size,**kwargs)
          self._image_cache = {}

    def display(self,maze:Grid,entities:Entities,player_position:Position):
          """Clears the game view, then creates (on the FancyGameView instance itself) the images for
        the tiles and entities."""
          
          self.delete(tk.ALL) # Clear the game view
         # Loop through the maze and display tiles and entities
          for row in range(len(maze)): # Loop through the rows
               for col in range(len(maze[row])):
                  tile = maze[row][col]   #the location of the tile
                  if tile == WALL:
                       image_name = 'W'
                  elif tile == GOAL:
                       Image_name = 'G'
                  elif tile == FLOOR:
                       image_name = 'Floor'
                       
                       
                  image = get_image(image_name,self.get_cell_size(),self._image_cache)   # Get the image for the tile
                  self.create_image(self.get_midpoint(row,col),image=image)         # Create the image on the canvas

          "display entities"
          "if an entity is at a specific location, assume there's a Floor tile underneath it"

          for position, entity in entities.items():
               row, col = position
               if maze[row][col] == ' ':
                     floor_image = get_image(FLOOR, self.get_cell_size(), self._image_cache)
                     self.create_image(self.get_midpoint(position), image=floor_image)
                     # Render the entity on top of the FLOOR tile
                     if entity == MOVE_POTION:  # Assuming 'M' represents a potion
                         entity_image = get_image('M', self.get_cell_size(), self._image_cache)
                     elif entity == FANCY_POTION:  # Another type of potion
                         entity_image = get_image('F', self.get_cell_size(), self._image_cache)
                     elif entity == CRATE:  # Crate
                         entity_image = get_image('C', self.get_cell_size(), self._image_cache)
                     elif entity == COIN:  # Money or coin
                         entity_image = get_image('$', self.get_cell_size(), self._image_cache)
                     elif entity == STRENGTH_POTION:  # Strength potion
                         entity_image = get_image('S', self.get_cell_size(), self._image_cache)
                     elif entity == PLAYER:  # Player
                         entity_image = get_image('P', self.get_cell_size(), self._image_cache)
  
                    # ... add more entities as needed
                     self.create_image(self.get_midpoint(position), image=entity_image)


def play_game(root: tk.Tk, maze_file: str) -> None:
     """
     Play the Sokoban game.

     Parameters:
          - root (tk.Tk): The root window of the game.
          - maze_file (str): The file path of the maze to be loaded.

     Returns:
          None
     """
     game = ExtraFancySokoban(root, maze_file)
     root.mainloop()


def main() -> None:
    """ The main function. """
    pass  # Write your main code here
    
    
    root = tk.Tk()  # Create the root window
    play_game(root, 'coin_maze.txt')  # Start the game


if __name__ == "__main__":
    main()


