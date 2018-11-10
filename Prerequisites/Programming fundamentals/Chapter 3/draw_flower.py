# Draw a flower made of triangles

import turtle


def draw_flower():
    window = turtle.Screen()
    flower = turtle.Turtle()

    flower.color('medium purple')
    flower.shape('turtle')
    flower.width(2)
    flower.speed(100)

    def draw_triangles():
        for i in range(0, 3):
            flower.forward(100)
            flower.right(120)
            flower.forward(100)


    for j in range(0, 36):
        draw_triangles()
        flower.right(10)
    
    flower.right(90)
    flower.forward(340)

    window.exitonclick()




draw_flower()