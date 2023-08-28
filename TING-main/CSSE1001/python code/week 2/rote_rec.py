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

    def rotated_rectangle(width, height,angle):
        turtle.left(angle)
        #draw a rectangle
        rectangle(width,height)

    # if this is the main file we ran
    if __name__ == "__main__":
        rotated_rectangle(300,120,30)
        turtle.exitonclick()
