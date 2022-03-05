from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")
DIST_TOP = 60
SCORE_TO_WIN = 10

class Score(Turtle):

    def __init__(self, x, screen_height, screen_width):
        super().__init__()
        self.score = 0
        self.screen_width = screen_width
        self.color("white")
        self.shape("classic")
        self.penup()
        self.shapesize(1)
        self.goto(x, screen_height/2-DIST_TOP)
        self.hideturtle()
        self.update_scoreboard(self.score)

    def increment(self):
        self.score += 1
        self.clear()
        self.update_scoreboard(self.score)

    def win(self):
        if self.xcor() > 0:
            self.goto(self.screen_width / 4, 0)
        else:
            self.goto(-self.screen_width / 4, 0)
        self.update_scoreboard("WIN")

    def lose(self):
        if self.xcor() > 0:
            self.goto(self.screen_width / 4, 0)
        else:
            self.goto(-self.screen_width / 4, 0)
        self.update_scoreboard("LOSE")

    def update_scoreboard(self, text):
        self.write(text, align=ALIGNMENT, font=FONT)

    def check_win(self):
        if self.score >= SCORE_TO_WIN:
            self.win()
            return True
        return False

