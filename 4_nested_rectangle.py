import turtle


def nested_rectangle():
    turtle.shape('turtle')
    x = 10
    for i in range(10):
        for j in range(4):
            turtle.forward(x)
            turtle.left(90)
        turtle.penup()
        turtle.left(180)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.pendown()
        x = x + 40

if __name__ == "__main__":
    nested_rectangle()
    while True:
        pass