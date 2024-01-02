"""
4. Write a function called circle that takes a turtle, t, and radius, r, as parameters
and that draws an approximate circle by calling polygon with an appropriate
length and number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference.
"""

import turtle
from math import pi

bob = turtle.Turtle()


def circle(t, r):
    n = (2 * pi * r) / 360
    for i in range(360):
        t.fd(n)
        t.lt(1)


circle(bob, 100)

turtle.mainloop()
