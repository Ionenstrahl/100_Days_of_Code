import turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = int(20)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, screen_size):
        self.segments = []
        self.screen_size = screen_size
        for position in START_POS:
            self.create_segment(position)
        self.head   = self.segments[0]
        self.throat = self.segments[1]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        #self.head.forward(MOVE_DIST)
        #self.head.goto(int(self.head.xcor()), int(self.head.ycor()))
        print(str(self.head.xcor()) + " " + str(self.head.ycor()))
        if self.head.heading() == UP:
            self.head.goto(self.head.xcor(), self.head.ycor() + MOVE_DIST)
        elif self.head.heading() == RIGHT:
            self.head.goto(self.head.xcor() + MOVE_DIST, self.head.ycor())
        elif self.head.heading() == DOWN:
            self.head.goto(self.head.xcor(), self.head.ycor() - MOVE_DIST)
        elif self.head.heading() == LEFT:
            self.head.goto(self.head.xcor() - MOVE_DIST, self.head.ycor())

    def set_direction(self, key):
        if key == "w":
            self.direction = "north"
        if key == "d":
            self.direction = "east"
        if key == "s":
            self.direction = "south"
        if key == "a":
            self.direction = "west"

    # controls
    def head_north(self):
        if int(self.head.ycor()) == int(self.throat.ycor()):
            self.head.setheading(UP)

    def head_east(self):
        if int(self.head.xcor()) == int(self.throat.xcor()):
            self.head.setheading(RIGHT)

    def head_south(self):
        if int(self.head.ycor()) == int(self.throat.ycor()):
            self.head.setheading(DOWN)

    def head_west(self):
        if int(self.head.xcor()) == int(self.throat.xcor()):
            self.head.setheading(LEFT)

    def create_segment(self,  pos = None):
        if pos is None:
            x_pos = self.segments[len(self.segments) - 1].xcor()
            y_pos = self.segments[len(self.segments) - 1].ycor()
            pos = (x_pos, y_pos)
        new_segment = turtle.Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def collides_with_wall(self):
        if  self.head.xcor() <= -self.screen_size//2 or \
            self.head.xcor() >=  self.screen_size//2 or \
            self.head.ycor() <= -self.screen_size//2 or \
            self.head.ycor() >=  self.screen_size//2:
            return True
        return False

    def collides_with_snake(self):
        for segment in self.segments[1:]:
            if segment.xcor() == self.head.xcor() and segment.ycor() == self.head.ycor():
                return True
        return False

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        for position in START_POS:
            self.create_segment(position)
        self.head   = self.segments[0]
        self.throat = self.segments[1]
