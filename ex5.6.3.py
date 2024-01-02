"""
The Koch curve can be generalized in several ways.
See http://en.wikipedia.org/wiki/Koch_snowflake for examples and implement your favorite.
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
    t.rt(60)
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)
    t.rt(60)
    koch(t, x / 3)


def snowflake(t, x):
    for i in range(4):
        koch(t, x /3)
        t.rt(120)


snowflake(bob, 100)
turtle.mainloop()
