from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")
screen = Screen()

def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_right():
    tim.right(1)


def move_left():
    tim.left(1)


def clear():
    #tim.home()
    #tim.penup()
    #tim.pendown()
    tim.setx(0)
    tim.sety(0)
    tim.seth(0)
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()