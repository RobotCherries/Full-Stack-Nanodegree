# This is a program that draws a square

import turtle


def draw_square():
    window = turtle.Screen()

    brad = turtle.Turtle()
    brad.speed(15)
    brad.width(20)

    for i in range(0, 4):
        brad.forward(100)
        brad.right(90)

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('pink')
    angie.speed(5)
    angie.width(10)
    angie.circle(50)

    tyler = turtle.Turtle()
    tyler.shape('triangle')
    tyler.color('yellow')
    tyler.width(15)

    tyler.forward(100)
    tyler.right(120)
    tyler.forward(100)
    tyler.right(120)
    tyler.forward(100)

    window.exitonclick()


draw_square()
