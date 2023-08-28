import turtle
def demo() :
    """ turtle demo"""
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(80)
    turtle.exitonclick()
    
def rectangle(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.setheading(0)


    #if this is the main file we ran
if __name__ == "__main__":
        rectangle(500,100)
        turtle.exitonclick()
        turtle.update()
