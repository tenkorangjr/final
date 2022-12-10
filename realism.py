"""
Name: Michael Tenkorang
Course: CS 151
Section: A
Project: 6
Date: 27 October 2022
"""

import complex_shapes as cs


def main():
    """Draw Social Realism scene"""

    window = cs.gr.GraphWin(
        "Michael's Social Realism Scene", width=600, height=600)
    window.setBackground(cs.gr.color_rgb(135, 206, 235))

    back = cs.background_init(0, 175, 1)
    cs.draw(back, window)

    house = cs.building_2_init(0, 70, 4)
    cs.draw(house, window)

    my_bicycle = cs.bicycle_init(400, 200)
    cs.draw(my_bicycle, window)

    house = cs.building_1_init(0, 250, 2.5)
    cs.draw(house, window)

    house_writing = cs.gr.Text(cs.gr.Point(110, 270), "POWER HOUSE")
    house_writing.draw(window)

    window.getMouse()
    window.close()


if __name__ == "__main__":
    main()
