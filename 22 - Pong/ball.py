from turtle import Turtle
import math
SIZE = 1
SPEED = 20
MAX_Y_SPEED = 14   #sqrt(0.5) =~ 0.7
PADDLE_BOUNCE_FACTOR = 0.5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(SIZE)
        self.penup()
        self.speed_y = MAX_Y_SPEED
        self.speed_x = self.calc_x_speed()

    def calc_x_speed(self):
        return math.sqrt(SPEED * SPEED - self.speed_y * self.speed_y)

    def move(self):
        self.setx(self.xcor() + self.speed_x)
        self.sety(self.ycor() + self.speed_y)

    def check_right_border(self, screen_width):
        if self.xcor() > screen_width / 2 - SIZE * 20 / 2:
            return True
        return False

    def check_left_border(self, screen_width):
        if self.xcor() < - screen_width / 2 + SIZE * 20 / 2:
            return True
        return False

    def check_border_bounce(self, screen_height):
        if abs(self.ycor()) > screen_height / 2 - SIZE * 20 / 2:
            self.bounce_from_border()

    def bounce_from_border(self):
        self.speed_y *= -1

    def bounce_from_paddle(self, paddle_pos_y):
        self.speed_y += PADDLE_BOUNCE_FACTOR * (self.ycor() - paddle_pos_y)
        if self.speed_y > MAX_Y_SPEED:
            self.speed_y = MAX_Y_SPEED
        if self.speed_y < -MAX_Y_SPEED:
            self.speed_y = -MAX_Y_SPEED
        self.speed_x = -self.calc_x_speed() * self.speed_x / abs(self.speed_x)

    def restart(self):
        self.setx(0)
        self.sety(0)
        self.speed_x *= -1

    def keep_in_middle(self):
        self.setx(0)
        self.sety(0)
        self.speed_y = 0
        self.speed_x = 0
