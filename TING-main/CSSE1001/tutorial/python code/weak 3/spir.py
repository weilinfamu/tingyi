import turtle
def spiral(num_lines, step_size):
    distance = step_size   #initialize distance with step_size-=[p]
    for i in range(num_lines):
        turtle.forward(distance)
        turtle.left(90)
        if i % 2 == 1:
            distance += step_size 
        
#if this is the main file we ran
if __name__ == "__main__":
    turtle.shape("turtle")
    spiral(20,20)
    turtle.exitonclick()
        
    
    