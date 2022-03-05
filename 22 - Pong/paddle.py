from turtle import Turtle


SQUARE_SIZE = 20
SQUARE_NUM  = 4
PX_PER_MOVE = 20

class Paddle():

    def __init__(self, pos_x, screen_height):
        self.pos_x = pos_x
        self.pos_y = 0
        self.squares = []
        self.movement = 0
        self.screen_height = screen_height
        for i in range(0,SQUARE_NUM):
            self.create_square(i, pos_x)

    def create_square(self, i, x_pos):
        new_square = Turtle()
        new_square.color("white")
        new_square.penup()
        new_square.speed("fastest")
        new_square.shape("square")
        new_square.shapesize(SQUARE_SIZE/20,SQUARE_SIZE/20,1)
        new_square.setx(x_pos)
        new_square.sety( SQUARE_SIZE * (SQUARE_NUM-1) // 2 - SQUARE_SIZE * i )
        self.squares.append(new_square)

    def increment_movement(self):
        if self.movement < 1:
            self.movement += 1

    def decrement_movement(self):
        if self.movement > -1:
            self.movement -= 1

    def move(self):
        if int(self.movement) > 0:
            self.move_up()
        if int(self.movement) < 0:
            self.move_down()

    def move_up(self):
        top_square_y = self.squares[0].ycor()
        if top_square_y <= self.screen_height / 2 - (SQUARE_SIZE / 2 + PX_PER_MOVE):
            for square in self.squares:
                square.sety(square.ycor() + PX_PER_MOVE)
            self.pos_y += PX_PER_MOVE

    def move_down(self):
        bottom_square_y = self.squares[len(self.squares)-1].ycor()
        if bottom_square_y >= - self.screen_height / 2 + (SQUARE_SIZE / 2 + PX_PER_MOVE):
            for square in self.squares:
                square.sety(square.ycor() - PX_PER_MOVE)
            self.pos_y -= PX_PER_MOVE

    def check_bounce(self, pos):
        # radius paddle +~ radius ball
        min_bounce_dist = SQUARE_SIZE / 2 + SQUARE_SIZE / 2
        # x
        if abs(pos[0] - self.pos_x) < min_bounce_dist:
            # y
            for square in self.squares:
                if abs(pos[1] - square.ycor()) < min_bounce_dist:
                    print("bounce " + str(self.pos_x))
                    return True
        return False




