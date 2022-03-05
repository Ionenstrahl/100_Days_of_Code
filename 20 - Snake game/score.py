from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):

    def __init__(self, size):
        super().__init__()
        self.score = 0
        self.high_score = int(Score.read_high_score())
        self.color("white")
        self.shape("classic")
        self.penup()
        self.shapesize(1)
        self.size = size
        self.goto(0, size//2-30)
        self.hideturtle()
        self.update_scoreboard(f"Score: {self.score} High Score:{self.high_score}")

    def increment(self):
        self.score +=1;
        self.clear()
        self.update_scoreboard(f"Score: {self.score} High Score:{self.high_score}")

    def update_scoreboard(self, text):
        self.write(text, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            Score.write_high_score(self.high_score)
        self.score = 0
        self.clear()
        self.goto(0, self.size // 2 - 30)
        self.update_scoreboard(f"Score: {self.score} High Score:{self.high_score}")

    def game_over(self):
        self.goto(0, 0)
        self.update_scoreboard("GAME OVER")

    @staticmethod
    def read_high_score():
        with open("high_score.txt") as file:
            return file.read()

    @staticmethod
    def write_high_score(high_score):
        with open("high_score.txt", mode="w") as file:
            file.write(str(high_score))