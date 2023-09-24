import turtle
def interact():
    distance = int(input("Distance:"))
   
    while True:
        direction = input("direction")
        if direction == "n":
            turtle.setheading(90)
            
        elif direction == "s":
            turtle.setheading(270)
           
        elif direction == "w":
            turtle.setheading(180)
            
        elif direction == "e":
            turtle.setheading(0)
            
        elif direction == "q":
            turtle.bye()
            break
        else:
            print("that\'s not a direction")
            continue

        turtle.forward(distance)
# if this is the main file we ran
if __name__ == "__main__":
    interact()
    turtle.exitonclick()
    
        
