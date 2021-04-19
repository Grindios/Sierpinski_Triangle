from turtle import Turtle, Screen
import random
import turtle as turtle_module

turtle_module.colormode(255)

aposx = 300
aposy = 300
bposx = -300
bposy = 300
cposx = 0
cposy = -300

ax = -300
ay = -300
bx = 300
by = -300
cx = 0
cy = 300

point_A = turtle_module.Turtle()
rgb_colors = []
point_A.pensize(3)
point_A.speed(120)



cap = random.randint(500, 10000)

for i in range(1000000):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    roll = random.randint(1, 6)
    new_color = (r, g, b)
    rgb_colors.append(new_color)

    if roll == 1 or roll == 2:
        AX_Coord = point_A.xcor()
        AY_Coord = point_A.ycor()
        x = (AX_Coord - aposx) / 2
        y = (AY_Coord - aposy) / 2
        point_A.penup()
        point_A.goto(x, y)
        point_A.pendown()
        point_A.dot(2, "red")


    if roll == 3 or roll == 4:
        AX_Coord = point_A.xcor()
        AY_Coord = point_A.ycor()
        x = (AX_Coord - bposx) / 2
        y = (AY_Coord - bposy) / 2
        point_A.penup()
        point_A.goto(x, y)
        point_A.pendown()
        point_A.dot(2, "green")


    if roll == 5 or roll == 6:
        AX_Coord = point_A.xcor()
        AY_Coord = point_A.ycor()
        x = (AX_Coord - cposx) / 2
        y = (AY_Coord - cposy) / 2
        point_A.penup()
        point_A.goto(x, y)
        point_A.pendown()
        point_A.dot(2, "blue")






screen = Screen()
screen.exitonclick()