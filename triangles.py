import turtle
def draw_triangle(brad):
    brad.color("blue", "green")
    brad.fill(True)

    brad.forward(300)
    brad.left(120)
    brad.forward(300)
    brad.left(120)
    brad.forward(300)
    brad.end_fill()
#jdjjdd    brad.color("blue", "white")
    brad.fill(True)
    brad.left(180)
    brad.forward(150)
    brad.right(60)
    brad.forward(150)
    brad.right(120)
    brad.forward(150)
    brad.right(120)
    brad.forward(150)
    brad.end_fill()

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(180)
    brad.forward(75)
    brad.right(60)
    brad.forward(75)
    brad.right(120)
    brad.forward(75)
    brad.right(120)
    brad.forward(75)
    brad.end_fill()

    brad.right(60)
    brad.forward(75)

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(120)
    brad.forward(75)
    brad.right(60)
    brad.forward(75)
    brad.right(120)
    brad.forward(75)
    brad.right(120)
    brad.forward(75)
    brad.end_fill()

    brad.right(60)
    brad.forward(75)

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(120)
    brad.forward(75)
    brad.right(60)
    brad.forward(75)
    brad.right(120)
    brad.forward(75)
    brad.right(120)
    brad.forward(75)
    brad.end_fill()


    brad.color("blue", "white")
    brad.fill(True)
    brad.left(180)
    brad.forward(37.5)
    brad.right(60)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.end_fill()

    brad.right(60)
    brad.forward(37.5)

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(120)
    brad.forward(37.5)
    brad.right(60)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.end_fill()

    brad.right(60)
    brad.forward(37.5)

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(120)
    brad.forward(37.5)
    brad.right(60)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.end_fill()

    brad.right(180)
    brad.forward(37.5)
    brad.left(60)
    brad.forward(75)

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(60)
    brad.forward(37.5)
    brad.left(120)
    brad.forward(37.5)
    brad.left(120)
    brad.forward(37.5)
    brad.end_fill()

    brad.left(60)
    brad.forward(75)

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(60)
    brad.forward(37.5)
    brad.left(120)
    brad.forward(37.5)
    brad.left(120)
    brad.forward(37.5)
    brad.end_fill()

    brad.left(180)
    brad.forward(37.5)

    brad.right(60)
    brad.forward(37.5)

    brad.left(120)
    brad.forward(37.5)
    brad.color("blue", "white")
    brad.fill(True)
    brad.right(60)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.end_fill()

    brad.left(180)
    brad.forward(37.5)
    brad.right(-60)
    brad.forward(75)

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(60)
    brad.forward(37.5)
    brad.left(120)
    brad.forward(37.5)
    brad.left(120)
    brad.forward(37.5)
    brad.end_fill()

    brad.right(-60)
    brad.forward(75)

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(60)
    brad.forward(37.5)
    brad.left(120)
    brad.forward(37.5)
    brad.left(120)
    brad.forward(37.5)
    brad.end_fill()

    brad.right(-60)
    brad.forward(37.5)

    brad.left(120)
    brad.forward(75 + 37.5)

    brad.color("blue", "white")
    brad.fill(True)
    brad.left(120)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.right(120)
    brad.forward(37.5)
    brad.end_fill()




def draw():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(6)
    draw_triangle(brad)
    window.exitonclick()
draw()
