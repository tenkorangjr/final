"""
Name: Michael Tenkorang
Project: 8
Course: CS151
Section: A
Date: 26 November 2022
"""

import lsystem
import random
import turtle_interpreter


def main():
    """Draw an arrangement of the lsystems on turtle screen"""
    trees = []
    trees.append(lsystem.Lsystem("systemDL.txt"))
    trees.append(lsystem.Lsystem("systemEL.txt"))
    trees.append(lsystem.Lsystem("systemFL.txt"))

    sx = 800
    sy = 800
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    positions = [(-300, -200), (-50, -200), (150, -200)]

    for i in range(len(positions)):
        iterations = random.randint(3, 5)

        tstr = trees[i].buildString(iterations)

        terp.setWidth(2)
        terp.setColor((0.5, 0.4, 0.3))
        terp.place(positions[i][0], positions[i][1], 90)
        terp.drawString(tstr, random.randint(3, 5), 20)

    terp.hold()


if __name__ == "__main__":
    main()
