"""
The letters of the alphabet can be constructed from a moderate number of basic elements,
like vertical and horizontal lines and a few curves.
Design an alphabet that can be drawn with a minimal number of basic elements and then write functions that draw the letters.

You should write one function for each letter, with names draw_a, draw_b, etc.,
and put your functions in a file named letters.py. You can download a “turtle typewriter” from http://thinkpython2.com/code/typewriter.py to help you test your code.
"""

import turtle
bob = turtle.Turtle()


def draw_a(t):
    t.lt(90)
    t.fd(100)
    t.lt(150)
    t.fd(100)
    t.lt(160)
    t.fd(100)


draw_a(bob)

turtle.mainloop()
