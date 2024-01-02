import turtle, math

bob = turtle.Turtle()


def arc(t, r, angle):
    step = 2 * math.pi * r / 360
    for i in range(angle):
        t.fd(step)
        t.lt(1)


def flower(t, no_petals, len_petals, angle):
    for i in range(no_petals):
        for i in range(2):
            arc(t, len_petals, angle)
            t.lt(180 - angle)
        t.lt(360 / no_petals)


flower(bob, 40, 200, 30)

turtle.mainloo()
