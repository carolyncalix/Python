from turtle import *
import math

# Name your Turtle.
tony = Turtle()
color = input("What color would you like?")
sides = input("How many sides do you want?")
# Set Up your screen and starting position.
setup(500,300)
xpos = 0
ypos = 0
tony.setposition(xpos, ypos)

### Write your code below:
tony.pencolor(color)
tony.pendown()

def shape(sides,steps):
    for shape in range(int(sides)):
        tony.forward(steps)
        tony.left(360/int(sides))
tony.begin_fill()
tony.fillcolor(color)
shape(sides,100)
tony.end_fill()
# Close window on click.
exitonclick()
