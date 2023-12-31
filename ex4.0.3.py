"""
3. Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon.
Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
"""

import turtle

bob = turtle.Turtle()


def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)


polygon(bob, 15, 50)

turtle.mainloop()
