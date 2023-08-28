import turtle
def interact():
    distance = int(input("Distance:"))
   
    while True:
        direction = input("direction")
        if direction == "n":
            turtle.setheading(90)
            turtle.forward(distance)
        elif direction == "s":
            turtle.setheading(270)
            turtle.forward(distance)
        elif direction == "w":
            turtle.setheading(180)
            turtle.forward(distance)
        elif direction == "e":
            turtle.setheading(0)
            turtle.forward(distance)
        elif direction == "q":
            turtle.bye()
            break
        else:
            print("that\'s not a direction")
        
# if this is the main file we ran
if __name__ == "__main__":
    interact()
    turtle.exitonclick()
    
        
