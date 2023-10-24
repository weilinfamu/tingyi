import tkinter as tk
from tkinter import messagebox, filedialog
from typing import Callable, Union
from model import SokobanModel, Tile, Entity
from a2_support import *
from a3_support import *
COIN = '$'
COIN_AMOUNT = 5
# Write your classes and functions here
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
                       image_name = 'G'
                  elif tile == 'X':
                       image_name = 'X'
                  elif tile == FLOOR:
                       image_name = 'Floor'
                  else:
                       continue

                       
                  image = get_image(image_name,self.get_cell_size(),self._image_cache)   # Get the image for the tile
                  self.create_image(self.get_midpoint(row,col),image=image)         # Create the image on the canvas

          "display entities"
          "if an entity is at a specific location, assume there's a Floor tile underneath it"

          for position, entity in entities.items():
               row, col = position
               if maze[row][col] == FLOOR:
                     floor_image = get_image('Floor', self.get_cell_size(), self._image_cache)
                     self.create_image(self.get_midpoint(position), image=floor_image)
                     # Render the entity on top of the FLOOR tile
                     entity_image = None

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
  
                     if entity_image:
                         self.create_image(self.get_midpoint(position), image=entity_image)

    def reset_cache_and_resize(self, new_dimensions: tuple[int,int]) -> None:
               """Clears the image cache and resizes the game view."""
               self._image_cache = {}
               self.set_dimensions(new_dimensions)
               self.clear()
               self.redraw()
     
              
     
class FancyStatsView(AbstractGrid):
     def __init__(self, master: tk.Tk | tk.Frame) -> None:
          #  # Set up the grid with 3 rows and 3 columns
          super().__init__(master, dimensions=(3, 3), size=(MAZE_SIZE+ SHOP_WIDTH,STATS_HEIGHT))

          #display the title in th top row and second column
          self.create_text(self.get_midpoint((0,1)),text="Player Stats",font=TITLE_FONT,anchor=tk.CENTER)

          "display the second line of stats for initial view"
          self.create_text(self.get_midpoint((1,0)),text="Moves remaining: ",font=FONT)
          self.create_text(self.get_midpoint((1,1)),text="Strength: ",font=FONT)
          self.create_text(self.get_midpoint((1,2)),text="Money: ",font=FONT)

     def draw_stats(self, move_remaining: int, strength: int, money: int) -> None:
          
          self.delete(tk.ALL)

          "Redraw the titles and 'static' stats"

          self.create_text(self.get_midpoint((0,1)),text="Player Stats",font=TITLE_FONT,anchor=tk.CENTER)
          self.create_text(self.get_midpoint((1,0)),text="Moves remaining: ",font=FONT)
          self.create_text(self.get_midpoint((1,1)),text="Strength: ",font=FONT)
          self.create_text(self.get_midpoint((1,2)),text="Money: ",font=FONT)



          "display the values in third line of stats"
          self.create_text(self.get_midpoint((2,0)),text=str(move_remaining),font=FONT)
          self.create_text(self.get_midpoint((2,1)),text=str(strength),font=FONT)
          self.create_text(self.get_midpoint((2,2)),text=str(money),font=FONT)



class Shop(tk.Frame):
      def __init__(self, master:tk.Frame)->None:
          super().__init__(master)
          "initial the title of the shop"
          
          self.title_label =tk.Label(self,text="Shop",font=TITLE_FONT)
          self.title_label.pack(pady=10)   #add some padding around the title
         
      def create_buyable_item(self, item: str, amount: int, callback: Callable[[],None])-> None:
          "create a new frame for the item"
          item_frame = tk.Frame(self)
          item_frame.pack(fill=tk.X, padx=10, pady=5)

          "create a label for the item"
          item_label = tk.Label(item_frame,text=f"{item} -(${amount})")
          item_label.pack(side=tk.LEFT, padx=10)

          "create a button to buy the item"
          buy_button = tk.Button(item_frame,text="Buy",command=callback)
          buy_button.pack(side=tk.LEFT, padx=10)

          

class FancySokobanView(tk.Frame):
     def __init__(self,master:tk.Tk, dimensions: tuple[int,int], size: tuple[int,int])->None:
          super().__init__(master)

          master.title("Extra Fancy Sokoban")   #set the title of the window

          "load the banner image and display it"

          self.banner_image = get_image("images/banner.png", (MAZE_SIZE + SHOP_WIDTH, BANNER_HEIGHT),)

          
          self.banner = tk.Label(self,image=self.banner_image)
          self.banner.pack(fill=tk.BOTH, expand=True)

          "instantiating and packing the three widgets"
          self.game_view = FancyGameView(self,dimensions,size)
          self.game_view.pack(pady=20)

          self.stats_view = FancyStatsView(self)
          self.stats_view.pack()

          self.shop = Shop(self)
          self.shop.pack()

     def display_game(self, maze: Grid, entities: Entities, player_position: Position) -> None:
          """
          Redraws the game view with the given maze, entities, and player position.

          Args:
               maze (Grid): The maze to display.
               entities (Entities): The entities to display.
               player_position (Position): The position of the player in the maze.
          """
          self.game_view.clear()
          self.game_view.display(maze, entities, player_position)


      
     def display_stats(self, moves_remaining: int, strength: int, money: int)->None:
          self.stats_view.clear()
          self.stats_view.draw_stats(moves_remaining,strength,money)


     " connect the buy_item_callback to the shop"
     def create_shop_items( self, shop_items: dict[str,int],button_callback:Callable[[str], None]| None = None)->None:
          "create a buyable item in the shop"
          for item_id, price in shop_items.items():
            if button_callback:
                callback = lambda item_id=item_id: button_callback(item_id)
            else:
                callback = None
                
            self.shop.create_buyable_item(item_id, price, callback)
                   

     def update_game_dimensions(self, new_dimensions: tuple[int,int])->None:
          self.game_view.reset_cache_and_resize(new_dimensions[1],new_dimensions[0])

     
class ExtraFancySokoban:
     

     """
     A class representing the controller for the Sokoban game.
     
     Args:
     root (tk.Tk): The root window of the game.
     maze_file (str): The file path of the maze to be loaded.
     """
     

     def __init__(self, root: tk.Tk, maze_file: str) -> None:
          self.root = root

          self.model = SokobanModel(maze_file)

          maze = self.model.get_maze()
          rows = len(maze)
          cols = len(maze[0])


          self.view = FancySokobanView(self.root,dimensions=(rows,cols),size=(MAZE_SIZE,MAZE_SIZE))

          # create the shop items
          shop_items = self.model.get_shop_items()   #get the shop items from the model
          self.view.create_shop_items(shop_items, self.buy_item_callback)
          self.redraw()

                    # Add a menu bar
          self.menu_bar = tk.Menu(root)
          root.config(menu=self.menu_bar)

          # Add a file menu
          # Add a 'File' menu to the menu bar
          self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
          self.file_menu.add_command(label="Save", command=self.save_game)
          self.file_menu.add_command(label="Load", command=self.load_game)
          self.menu_bar.add_cascade(label="File", menu=self.file_menu)

     def buy_item_callback(self,item_id:str):
          self.model.attempt_purchase(item_id)
          self.redraw()
     
     def redraw(self)->None:

          self.view.display_game(self.model.get_maze(),self.model.get_entities(),self.model._player_position)
          
          self.view.display_stats(self.model.get_player_moves_remaining(),self.model.get_player_strength(),self.model.get_player_money())
          
          
     def handle_keypress(self, event: tk.Event) -> None:
          """
          Handle the keypress event.

          Parameters:
               - event (tk.Event): The keypress event.

          Returns:
               None
          """
          move = event.keysym
          game_outcome = self.model.attempt_move(move)
          self.redraw()

          if game_outcome in ['win', 'lose']:
               message = 'You win!' if game_outcome == 'win' else 'You lose!'
               play_again = messagebox.askyesno(message, f'message, Play again?')
               
               if play_again:
                    self.model.reset()
                    self.redraw()
               else:
                    self.root.quit()

     def save_game(self):
          file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
          if not file_name:
               return
          with open(file_name, "w") as file:
              maze = self.model.get_maze()  # store the maze from the model
              for row in maze:
                   file.write("".join(str(row)) + "\n")   #write the maze to the file in str
          
     def load_game(self):
          file_name = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
          if not file_name:
               return
          with open(file_name, "r") as file:
              maze = [list(line.strip()) for line in file]
              self.model = SokobanModel(maze)
              self.model._player.add_money(-self.model._player.get_money())
              self.redraw()
              
def play_game(root: tk.Tk, maze_file: str) -> None:
     """
     Play the Sokoban game.

     Parameters:
          - root (tk.Tk): The root window of the game.
          - maze_file (str): The file path of the maze to be loaded.

     Returns:
          None
     """
     game  = ExtraFancySokoban(root, maze_file)
     root.mainloop()


def main() -> None:

      # 1. Construct the root tk.Tk instance
    root = tk.Tk()  # Create the root window
    play_game(root, 'a3\maze_files\maze1.txt')  # Start the game
     

if __name__ == "__main__":
    main()

