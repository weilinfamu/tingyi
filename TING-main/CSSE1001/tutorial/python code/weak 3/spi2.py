import turtle
def spiral(num_lines,step_size):
    distance = step_size
    for i in range(num_lines):
        turtle.forward((i // 2 + 1) * distance)
        turtle.left(90)
if __name__ == "__main__":
    turtle.shape("turtle")
    spiral(20,20)
    turtle.exitonclick()
    
        
    

