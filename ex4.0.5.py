"""
5. Make a more general version of circle called arc that takes an additional
parameter angle, which determines what fraction of a circle to draw. angle is in
units of degrees, so when angle=360, arc should draw a complete circle.
"""

import turtle
from math import pi

bob = turtle.Turtle()


def arc(t, r, angle):
    n = (2 * pi * r) / 360
    for i in range(angle):
        t.fd(n)
        t.lt(1)


arc(bob, 100, 180)

turtle.mainloop()
