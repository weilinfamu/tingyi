import turtle

def rectangle(width,height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.setheading(0)
    turtle.exitonclick()

    #if ths is the main file, we run
if __name__ == "__main__":
    rectangle(500,100)
    turtle.exiton.click()
    turtle.update()
