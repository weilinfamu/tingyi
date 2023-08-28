import math
import turtle

def polygon(radius,num_sides):
    
    side_length = radius * math.sin(math.pi/ num_sides)
    angle = 360 / num_sides
  
    for count in range(num_sides):
        #repeat
        turtle.forward(side_length)
        turtle.left(angle)
        

#if this is the main file we ran
if __name__ == "__main__":
    polygon(300,100)
    
    
    
    