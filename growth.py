"""
Name: Michael Tenkorang
Project: 8
Course: CS151
Section: A
Date: 26 November 2022
"""

import turtle_interpreter
import lsystem


def main():
    """Function to draw the growth image on screen"""

    tree = lsystem.Lsystem("arr1.txt")

    sx = 800
    sy = 800
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    positions = [(-400, -200), (-150, -200), (250, -200)]

    for i in range(len(positions)):
        iterations = i+2

        tstr = tree.buildString(iterations)

        terp.setWidth(2)
        terp.setColor((0.5, 0.4, 0.3))
        terp.place(positions[i][0], positions[i][1], 90)
        terp.drawString(tstr, 20, 22.5)

    terp.hold()


# if __name__ == "__main__":
#     main()
