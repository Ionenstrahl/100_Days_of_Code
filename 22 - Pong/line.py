from turtle import Turtle

DASH_LENGTH = 2
GAP_LENGTH = 4
LINE_WIDTH = 5

class Line(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(LINE_WIDTH/22, LINE_WIDTH/22, 1)
        self.penup()
        self.hideturtle()
        self.check()
        self.goto(0, -screen_height/2)
        self.draw_dotted_line(screen_height)

    def draw_dotted_line(self, length):
        for i in range(0,int(length/LINE_WIDTH)):
            if i % (DASH_LENGTH + GAP_LENGTH) < DASH_LENGTH:
                self.stamp()
            self.sety(self.ycor() + LINE_WIDTH)

    def check(self):
        self.width(20)
        self.goto(310, 210)
        self.pendown()
        self.goto(-310, 210)
        self.goto(-310, -210)
        self.goto(310, -210)
        self.goto(310, 210)
        self.penup()