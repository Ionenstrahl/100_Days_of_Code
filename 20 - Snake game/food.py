import random
from turtle import Turtle


class Food:

    def __init__(self, size, snake_segments):
        self.size = size
        self.pos = self.create_random_position(snake_segments)
        self.food = Turtle(shape="turtle")
        self.food.color("white")
        self.food.penup()
        self.food.speed("fastest")
        self.food.goto(self.pos)

    def check_for_hungry_snake(self, snake_segments):
        if snake_segments[0].xcor() == self.food.xcor() and snake_segments[0].ycor() == self.food.ycor():
            self.repositioning(snake_segments)
            return True
        return False

    def repositioning(self, snake_segments):
        self.pos = self.create_random_position(snake_segments)
        self.food.goto(self.pos)

    def create_random_position(self, snake_segments):
        on_snake = True
        while on_snake:
            x_random = -self.size//2 + 20 * random.randint(1,self.size//20-1)
            y_random = -self.size//2 + 20 * random.randint(1,self.size//20-1)
            for segment in snake_segments:
                if segment.xcor() == x_random or segment.ycor() == y_random:
                    continue
            on_snake = False
        return (x_random, y_random)