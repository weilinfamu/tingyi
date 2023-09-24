import turtle
import math

def polygon(radius, num_sides):

    side_length = radius * math.sin(math.pi / num_sides)
    angle = 360 / num_sides
    count = 0
    while count < num_sides:
        #repeat 
        turtle.forward(side_length)
        turtle.left(angle)
        count += 1
    #if ... we ran
    if __name__ == "__main__":
        polygon(100,7)
        turtle.done()
        
        
