"""
Drawing Ans Artsy Module
========================
"""

import turtle as _turtle
from colorama import (Fore, Back, Style, init)


"""
Turtle Stuffs
"""
def pick_turt_drag(turt: _turtle.Turtle):
    def dragging(x: float, y: float):
        turt.ondrag(None)
        turt.setheading(turt.towards(x, y))
        turt.goto(x, y)
        turt.ondrag(dragging)
    return dragging

def sandycanvas():
    # _turtle.begin_fill() # start the drawing
    ########################################
    screen = _turtle.Screen()
    frank = _turtle.Turtle('turtle')
    frank.speed("fastest")
    frank.ondrag(pick_turt_drag(frank))
    ########################################
    # _turtle.end_fill() # end the drawing
    # _turtle.done()
    screen.mainloop()