from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(height=600, width=1100)


#question about the winner
user_winner = screen.textinput("Turtle Rice", "Who's gonna win? [red, orange, yellow, green, blue, purple]")


#create all turtles and place them
red    = Turtle()
orange = Turtle()
yellow = Turtle()
green  = Turtle()
blue   = Turtle()
purple = Turtle()

turtles= [red, orange, yellow, green, blue, purple]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
startY = [250, 150, 50, -50, -150, -250]

for i in range(6):
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].setx(-500)
    turtles[i].sety(startY[i])
    turtles[i].shape("turtle")

red.forward(1000)
red.right(90)
red.pendown()
red.forward(500)
red.right(90)
red.penup()
red.forward(980)
red.right(90)
red.forward(500)
red.right(90)
red.backward(20)


#move them
race_finished = False
winner = ""

def random_walk(turtle):
    dist = random.randint(-10,30)
    turtle.forward(dist)


def validate_winner(turtle):
    if turtle.xcor() >= 500:
        global race_finished, winner
        race_finished = True
        winner = turtle.pencolor()


while not race_finished:
    for i in range(6):
        turtles[i].speed(0)
        random_walk(turtles[i])
        validate_winner(turtles[i])


#return result
if user_winner == winner:
    print("Bravissimo, you did it. You crazy son!")
else:
    print(f"How did you come to believe {user_winner} would win? It was so obvious, that {winner} would make it!")

screen.exitonclick()

