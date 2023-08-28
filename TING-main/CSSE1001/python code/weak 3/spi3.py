import turtle
def spiral(num_lines,step_size):
    distance = step_size
    for i in range (num_lines):
        turtle.forward(step_size)
        turtle.left(90)
        if i % 2 == 1:
            step_size += distance
          
              
if __name__ == "__main__":
    
    spiral(20,20)
    turtle.exitonclick()