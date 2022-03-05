import turtle
from paddle import Paddle
from line import Line
from score import Score
from ball import Ball

# TWEAKS
# - adust placement - left margin > right margin
#                   - top bounce border > bottom bounce border
#                   - paddle can go to far to bottom
# - precise the paddle bounce
# - make a restart button
# - enable arrow keys
# - adjust font
# - try dependency injection
# - refactor & beautify
# - make side bounce paddle possible


# Screen
SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400
FRAME_RATE = 60      #FPS

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
line = Line(SCREEN_HEIGHT)


# Paddles
RIGHT_UP   = "8"
RIGHT_DOWN = "5"
LEFT_UP    = "w"
LEFT_DOWN  = "s"
DIST_FROM_BORDER = 20
RIGHT_X = SCREEN_WIDTH // 2 - DIST_FROM_BORDER
LEFT_X = -SCREEN_WIDTH // 2 + DIST_FROM_BORDER

paddle_right = Paddle(RIGHT_X, SCREEN_HEIGHT)
paddle_left = Paddle(LEFT_X, SCREEN_HEIGHT)


# Score
DIST_FROM_CENTER = 50

score_right = Score(DIST_FROM_CENTER, SCREEN_HEIGHT, SCREEN_WIDTH)
score_left = Score(-DIST_FROM_CENTER, SCREEN_HEIGHT, SCREEN_WIDTH)


# Ball
ball = Ball()


# Game Loop
game_on = True
screen.listen()

screen.onkeypress(key=RIGHT_UP, fun=paddle_right.increment_movement)
screen.onkeypress(key=RIGHT_DOWN, fun=paddle_right.decrement_movement)
screen.onkeypress(key=LEFT_UP, fun=paddle_left.increment_movement)
screen.onkeypress(key=LEFT_DOWN, fun=paddle_left.decrement_movement)

screen.onkeyrelease(key=RIGHT_UP, fun=paddle_right.decrement_movement)
screen.onkeyrelease(key=RIGHT_DOWN, fun=paddle_right.increment_movement)
screen.onkeyrelease(key=LEFT_UP, fun=paddle_left.decrement_movement)
screen.onkeyrelease(key=LEFT_DOWN, fun=paddle_left.increment_movement)

while game_on:
    screen.update()
    turtle.time.sleep(1/FRAME_RATE)
    paddle_right.move()
    paddle_left.move()
    ball.move()

    if paddle_right.check_bounce(ball.pos()):
        ball.bounce_from_paddle(paddle_right.pos_y)
    if paddle_left.check_bounce(ball.pos()):
        ball.bounce_from_paddle(paddle_left.pos_y)

    ball.check_border_bounce(SCREEN_HEIGHT)

    if ball.check_right_border(SCREEN_WIDTH):
        score_left.increment()
        if score_left.check_win():
            ball.keep_in_middle()
            score_right.lose()
        else:
            ball.restart()
    elif ball.check_left_border(SCREEN_WIDTH):
        score_right.increment()
        if score_right.check_win():
            ball.keep_in_middle()
            score_left.lose()
        else:
            ball.restart()

screen.exitonclick()