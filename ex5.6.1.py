"""
Write a function called koch that takes a turtle and a length as parameters,
and that uses the turtle to draw a Koch curve with the given length.
"""

import turtle

bob = turtle.Turtle()


def koch(t, x):
    if x < 3:
        t.fd(x)
        return
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)
    t.rt(120)
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)


koch(bob, 1000)
turtle.mainloop()
