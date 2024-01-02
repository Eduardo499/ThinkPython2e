"""
Write a function called snowflake that draws three Koch curves to make the outline of a snowflake.
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


def snowflake(t, x):
    for i in range(3):
        koch(t, x /3)
        t.rt(120)


snowflake(bob, 100)
turtle.mainloop()
