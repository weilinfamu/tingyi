"""
Simple GUI programming exercise to demonstrate component layout
and event handling.
"""

__copyright__ = "Copyright 2018, University of Queensland"


import tkinter as tk
from tkinter import messagebox

class SampleApp(object) :
    def __init__(self, master) :
        self._master = master
        master.title("Hello!")
        master.minsize(430, 200)
        #colour buttons
        self._lbl = tk.Label(master, text="Choose a button",
                             bd=5,
                             relief='solid')
        self._lbl.pack(side=tk.TOP,
                       expand = True)

          #colour frame
        colour_frame = tk.Frame(master,
                                bd=5,
                                relief='solid')
        colour_frame.pack(side=tk.BOTTOM,
                          pady=10,
                          fill=tk.X
                          )
        colour_lbl = tk.Label(colour_frame,
                              text="Choose the colour to:",
                             )
        colour_lbl.pack(side=tk.LEFT)
        self._colour_entry = tk.Entry(colour_frame)
        self._colour_entry.pack(side=tk.LEFT,
                          fill=tk.X,
                          expand=True)

        colour_btn = tk.Button(colour_frame,
                               text ="Change it",
                               command=self.change_colour)
        colour_btn.pack(side=tk.LEFT)
                                

        btn_frame = tk.Frame(master,
                             bd=5,
                             relief='solid')
        btn_frame.pack(side=tk.BOTTOM,
                       pady=10)


        blue_btn = tk.Button(btn_frame,
                              text="Change to Blue", 
                             command=self.change_blue)
        blue_btn.pack(side=tk.LEFT)

        green_btn = tk.Button(btn_frame,
                              text="Change to Green", 
                              command=self.change_green)
        green_btn.pack(side=tk.RIGHT)
    def change_colour(self) :
        colour = self._colour_entry.get()
        try:self._lbl.config(text="This label is " + colour,
                         bg=colour)
       
        except: tk.TclError
        messagebox.showerror("Invalid colour", colour + " is not a valid colour")


    def change_blue(self) :
        self._lbl.configure(text='This label is blue',
                            bg='SteelBlue1')
    def change_green(self) :
       self._lbl.configure(text='This label is green',
                            bg='medium spring green')
        
if __name__ == "__main__" :
    root = tk.Tk()
    app = SampleApp(root)
    root.mainloop()
