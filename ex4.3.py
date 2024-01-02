import turtle, math

bob = turtle.Turtle()


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def isosceles(t, r, center_angle, outside_angle, outside_side):
    t.fd(r)
    t.lt(180 + outside_angle)
    t.fd(outside_side)
    t.lt(180 + outside_angle)
    t.fd(r)


def polypie(t, n, r):
    center_angle = 360 / n
    outside_angle = (180 - center_angle) / 2
    outside_side = math.sqrt(2 * (r ** 2) - ((2 * (r**2)) * math.cos(center_angle * (math.pi/180))))
    for i in range(n):
        isosceles(t, r, center_angle, outside_angle, outside_side)
        t.rt(180 - 2 * center_angle)


polypie(bob, 5, 100)
turtle.mainloop()
