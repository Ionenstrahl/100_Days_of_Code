import turtle
import random
import colorgram

# 164 screen
tim = turtle.Turtle()
tim.shape("turtle")
tim.color("purple")
tim.speed(0)

# 165: quare
# for _ in range(4):
#    tim.forward(100)
#    tim.right(90)

# 167: dashed line
# for _ in range(10):
#    tim.forward(10)
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()

# 168: different shapes
# for edge in range(3,11):
#    tim.pencolor(edge*0.1,1-0.1*edge,1-0.1*edge)
#    for side in range(edge):
#        tim.forward(100)
#        tim.right(360/edge)

# 169: random walk
# tim.width(10)
# tim.speed = 0
# for _ in range(200):
#    ri = random.randint(0,4)
#    tim.setheading(90*ri)
#    tim.color(0.2*ri,0.2,1-0.2*ri)
#    tim.forward(30)

# 170: random RGB color
#turtle.colormode(255)

#def random_color():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    return r, g, b

#171: spirograph
#circle_num = 90
#circle_rad = 100
#for _ in range(circle_num):
#    tim.color(random_color())
#    tim.circle(circle_rad)
#    tim.right(360/circle_num)

#172: cologram.py
color_num = 14
colors = colorgram.extract('3510653-hollowknightbanner.jpg',color_num)
color_tuples = []
for i in range(color_num):
    rgb = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
    color_tuples.append(rgb)
print(color_tuples)

#173: Hirst Painting
turtle.colormode(255)
tim.penup()
dot_size = 20
dot_dist = 50
for y in range(10):
    for x in range(10):
        tim.color(color_tuples[random.randint(0,color_num-1)])
        tim.setx(dot_dist * x - 4.5*dot_dist)
        tim.sety(dot_dist * y - 4.5*dot_dist)
        tim.dot(dot_size)

# 164 screen
screen = turtle.Screen()
screen.exitonclick()
