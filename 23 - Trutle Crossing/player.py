from turtle import Turtle
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
START_Y = -280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()

    def move(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def go_to_start(self):
        self.sety(START_Y)


