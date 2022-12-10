"""
Name: Michael Tenkorang
Project: 8
Course: CS151
Section: A
Date: 26 November 2022

Version 2
"""

import turtle


class TurtleInterpreter:
    def __init__(self, dx=800, dy=800):
        """Initialiser for the TurtleInterpreter"""
        turtle.setup(dx, dy)
        turtle.tracer(False)

    def drawString(self, dstring, distance, angle):
        """ Interpret the characters in string dstring as a series
        of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the
        angle (in degrees) for each right or left command. The list   
        of turtle supported turtle commands is:
        F : forward
        - : turn right
        + : turn left
        [ : save the turtle's heading and position
        ] : restore the turtle's heading and position
        < : save current color of the turtle
        g : sets turtle's color to green
        y : sets turtle's color to yellow
        r : sets turtle's color to red 
        L : draws a circular leaf
        """

        stack = []
        colorstack = []

        for char in dstring:
            if char == 'F':
                turtle.forward(distance)
            elif char == '-':
                turtle.right(angle)
            elif char == '+':
                turtle.left(angle)
            elif char == '[':
                stack.append(turtle.position())
                stack.append(turtle.heading())
            elif char == ']':
                turtle.penup()
                turtle.setheading(stack.pop())
                turtle.goto(stack.pop())
                turtle.pendown()

            # modified drawString to handle five additional characters in strings
            elif char == '<':
                colorstack.append(turtle.color()[0])
            elif char == '>':
                new_color = colorstack.pop()
                turtle.color(new_color)
            elif char == 'g':
                turtle.color((0.15, 0.5, 0.2))
            elif char == 'y':
                turtle.color((0.8, 0.8, 0.3))
            elif char == 'r':
                turtle.color((0.7, 0.2, 0.3))
            elif char == 'L':
                turtle.color((0.15, 0.5, 0.2))
                turtle.begin_fill()
                turtle.circle(3, 180)
                turtle.end_fill()
        turtle.update()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        turtle.hideturtle()

        # Close the window when users presses the 'q' key
        turtle.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        turtle.listen()

        # Have the turtle listen for a click
        turtle.exitonclick()

    def place(self, xpos, ypos, angle=None):
        """Function to position turtle and set angle"""
        self.goto(xpos, ypos)
        if angle:
            self.orient(angle)

    def orient(self, angle):
        """function to set the heading of the turtle"""
        turtle.setheading(angle)

    def goto(self, xpos, ypos):
        """function to set position of the turtle"""
        turtle.penup()
        turtle.goto(xpos, ypos)
        turtle.pendown()

    def setColor(self, c):
        """Set color of the turtle"""
        turtle.color(c)

    def setWidth(self, w):
        """Set the width of the turtle"""
        turtle.width(w)
