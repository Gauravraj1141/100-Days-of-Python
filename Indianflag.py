import turtle

def create_indian_flag():
    # Create the turtle
    t = turtle.Turtle()

    # Set the flag size
    t.pensize(5)

    # Set the flag colors
    t.color("#FF9933") # saffron
    t.begin_fill()
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

    t.color("white") # white
    t.begin_fill()
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()

    t.color("#228B22") # green
    t.begin_fill()
    for i in range(2):
        t.forward(250)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()

    t.forward(125)
    t.color("#000080") # Ashoka Chakra color
    t.begin_fill()
    t.circle(25)

    t.end_fill()
    t.color("")

    t.pencolor("")
    t.begin_fill()
    t.back(125)
    for i in range(1):
        t.left(90)
        t.pencolor("#000000")
        t.forward(100)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(500)
        t.left(90)
        t.forward(10)
        t.left(90)
        t.forward(400)
        t.left(180)
        t.forward(200)

        t.left(90)
        t.pencolor("")
        t.forward(200)

        t.pencolor("blue")

        t.write("JAI HIND", font=("Arial", 15, "bold"),align="right")
        t.right(90)
        t.forward(50)
        t.write("Gaurav Rajput", font=("Arial", 15, "bold"),align="right")
    t.end_fill()


create_indian_flag()
turtle.done()
