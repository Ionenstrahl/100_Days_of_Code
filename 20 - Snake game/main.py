import turtle
from snake import Snake
from food import Food
from score import Score
SIZE = 440  # HAS TO BE DEVISIBLE BY 40

# initialize
screen = turtle.Screen()
screen.setup(width=SIZE, height=SIZE)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# snake_head = snake.SnakeHead(x_poy=0, y_pos=0, direction="east")
snake = Snake(SIZE)
food  = Food(SIZE, snake.segments)
score = Score(SIZE)

# gameplay loop

screen.listen()
screen.onkeypress(key="w", fun=snake.head_north)
screen.onkeypress(key="d", fun=snake.head_east)
screen.onkeypress(key="s", fun=snake.head_south)
screen.onkeypress(key="a", fun=snake.head_west)

key_pressed = False


game_on = True
while True:
    screen.update()
    turtle.time.sleep(0.1)
    if game_on:
        snake.move()
    if food.check_for_hungry_snake(snake.segments):
        snake.create_segment()
        score.increment()
    if snake.collides_with_wall() or snake.collides_with_snake():
        score.game_over()
        game_on = False
        turtle.time.sleep(2)
        snake.reset()
        score.reset()
        game_on = True


screen.exitonclick()

