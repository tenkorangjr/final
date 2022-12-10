"""
Name: Michael Tenkorang
Course: CS 151
Section: A
Project: 6
Date: 27 October 2022
"""


import graphicsPlus as gr


def bicycle_init(x, y, scale=3, tyre_color="black"):
    """Draw a bicycle"""

    bike = []
    line_1 = gr.Line(gr.Point(x, y), gr.Point(x+3*scale, y))
    bike.append(line_1)

    line_2 = gr.Line(gr.Point(x, y), gr.Point(x-5*scale, y+15*scale))
    bike.append(line_2)

    line_3 = gr.Line(gr.Point(x-5*scale, y+15*scale),
                     gr.Point(x+20*scale, y+15*scale))
    bike.append(line_3)

    tyre_1 = gr.Circle(gr.Point(x-5*scale, y+20*scale), 5*scale)
    tyre_1.setFill(tyre_color)
    tyre_2 = gr.Circle(gr.Point(x+20*scale, y+20*scale), 5*scale)
    tyre_2.setFill(tyre_color)
    inner_1 = gr.Circle(gr.Point(x-5*scale, y+20*scale), 2*scale)
    inner_1.setFill("white")
    inner_2 = gr.Circle(gr.Point(x+20*scale, y+20*scale), 2*scale)
    inner_2.setFill("white")
    bike.append(tyre_1)
    bike.append(tyre_2)
    bike.append(inner_1)
    bike.append(inner_2)

    return bike


def background_init(x, y, scale):
    """Draw the background of the image"""

    main_back = []
    rec_1 = gr.Rectangle(
        gr.Point(x=x, y=y), gr.Point(x=x+600*scale, y=y+60*scale))
    rec_1.setFill(gr.color_rgb(224, 186, 81))
    main_back.append(rec_1)

    rec_2 = gr.Rectangle(
        gr.Point(x=x, y=y+60*scale), gr.Point(x=x+600*scale, y=y+75*scale))
    rec_2.setFill(gr.color_rgb(240, 144, 230))
    main_back.append(rec_2)

    rec_3 = gr.Rectangle(
        gr.Point(x=x, y=y+75*scale), gr.Point(x=x+600*scale, y=y+600*scale))
    rec_3.setFill(gr.color_rgb(230, 208, 158))
    main_back.append(rec_3)

    return main_back


def building_1_init(x, y, scale):
    """Draw buildings"""

    house = []
    roof = gr.Polygon(gr.Point(x, y), gr.Point(
        x+45*scale, y-45*scale), gr.Point(x+90*scale, y))
    roof.setFill("white")
    house.append(roof)

    build = gr.Rectangle(gr.Point(x, y), gr.Point(x+90*scale, y+75*scale))
    build.setFill("white")
    house.append(build)

    door = gr.Rectangle(gr.Point(x+30*scale, y+25*scale),
                        gr.Point(x+60*scale, y+75*scale))
    door.setFill("black")
    house.append(door)

    return house


def building_2_init(x, y, scale):
    """Draw farther building"""

    building = []
    roof = gr.Polygon(gr.Point(x, y), gr.Point(x+90*scale, y),
                      gr.Point(x+100*scale, y+25*scale), gr.Point(x, y+25*scale))
    roof.setFill("white")
    building.append(roof)

    body = gr.Rectangle(gr.Point(x, y+25*scale),
                        gr.Point(x+90*scale, y+60*scale),)
    body.setFill("white")
    building.append(body)

    window_positions = (((x+20*scale, y+30*scale), (x+30*scale, y+45*scale)), ((x+40*scale, y+30*scale),
                        (x+50*scale, y+45*scale)), ((x+60*scale, y+30*scale), (x+70*scale, y+45*scale)))
    windows = []
    for position in window_positions:
        window = gr.Rectangle(gr.Point(position[0][0], position[0][1]), gr.Point(
            position[1][0], position[1][1]))
        window.setFill("black")
        windows.append(window)

    for window in windows:
        building.append(window)

    return building


def draw(objlist, win):
    '''A for loop that draws each item in the given list of shapes'''

    for item in objlist:
        item.draw(win)


if __name__ == "__main__":

    window = gr.GraphWin("Social Realism", width=600, height=600)

    # back = background_init(0, 175, 1)
    # draw(back, window)
    # back = background_init(300, 175, 3)
    # draw(back, window)
    # back = background_init(40, 200, 2)
    # draw(back, window)

    # my_bicycle = bicycle_init(400, 200, 3)
    # draw(my_bicycle, window)
    # my_bicycle = bicycle_init(20, 100, 2)
    # draw(my_bicycle, window)
    # my_bicycle = bicycle_init(300, 50, 1)
    # draw(my_bicycle, window)

    # house = building_2_init(100, 60, 3)
    # draw(house, window)
    # house = building_2_init(0, 70, 4)
    # draw(house, window)
    # house = building_2_init(90, 80, 6)
    # draw(house, window)

    # house = building_1_init(100, 250, 2.5)
    # draw(house, window)
    # house = building_1_init(50, 200, 4)
    # draw(house, window)
    # house = building_1_init(40, 350, 1)
    # draw(house, window)

    window.getMouse()
    window.close()
