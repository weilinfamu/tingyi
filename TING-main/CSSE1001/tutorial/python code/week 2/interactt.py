Python 3.11.4 (v3.11.4:d2340ef257, Jun  6 2023, 19:15:51) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

... import turtle
... 
... 
... def interact():
...     distance = int(input("please give a Distance: "))
...     direction = input("please give a direction")
...     
...     if direction == 'n':
...         turtle.setheading(0)
...         turtle.forward(distance)
...     elif direction == 's':
...         turtle.setheading(180)
...         turtle.forward(distance)
...     elif direction == 'w':
...         turtle.setheading(90)
...         turtle.forward(distance)
...     elif direction == 'e':
...         turtle.setheading(270)
...         turtle.forward(distance)
...     
...     #if this is the main file we ran
...     if __name__ == "__main__":
...         interact()
...         turtle.exitonclick()
SyntaxError: invalid syntax
... import turtle
... 
... 
... def interact():
...     distance = int(input("please give a Distance: "))
...     direction = input("please give a direction")
...     
...     if direction == 'n':
...         turtle.setheading(0)
...         turtle.forward(distance)
...     elif direction == 's':
... ...         turtle.setheading(180)
... ...         turtle.forward(distance)
... ...     elif direction == 'w':
... ...         turtle.setheading(90)
... ...         turtle.forward(distance)
... ...     elif direction == 'e':
... ...         turtle.setheading(270)
... ...         turtle.forward(distance)
... ...     
... ...     #if this is the main file we ran
... ...     if __name__ == "__main__":
... ...         interact()
... ...         turtle.exitonclick()
... SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> ... import turtle
... ... def interact():
... ...     distance = int(input("please give a Distance: "))
... ...     direction = input("please give a direction")
... ...     
... ...     if direction == 'n':
... ...         turtle.setheading(0)
... ...         turtle.forward(distance)
... ...     elif direction == 's':
... ...         turtle.setheading(180)
... ...         turtle.forward(distance)
... ...     elif direction == 'w':
... ...         turtle.setheading(90)
... ...         turtle.forward(distance)
... ...     elif direction == 'e':
... ...         turtle.setheading(270)
... ...         turtle.forward(distance)
... ...     
... ...     #if this is the main file we ran
... ...     if __name__ == "__main__":
... ...         interact()
... ...         turtle.exitonclick()
... SyntaxError: invalid syntax
SyntaxError: invalid syntax
