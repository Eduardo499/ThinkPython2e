"""
2; Add another parameter, named length, to square. Modify the body so length of
the sides is length, and then modify the function call to provide a second argument.
Run the program again. Test your program with a range of values for
length.
"""

import turtle

bob = turtle.Turtle()


def square(t, lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)


square(bob, 80)

turtle.mainloop()
