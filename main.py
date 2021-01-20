import turtle as t
import random

turtle_obj = t.Turtle()
s = t.Screen()

#  Change color mode for random RGB colors
t.colormode(255)

#  Direction angles
directions = [0, 90, 180, 270]

turtle_obj.speed('fastest')
# Adjust pensize
turtle_obj.pensize(1)


def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk():
    for _ in range(500):
        random_color = random_color_generator()
        turtle_obj.color(random_color)
        turtle_obj.forward(30)
        turtle_obj.setheading(random.choice(directions))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle_obj.color(random_color_generator())
        turtle_obj.circle(100)
        turtle_obj.setheading(turtle_obj.heading() + size_of_gap)


random_walk()

s.exitonclick()
