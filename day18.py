import random
from turtle import Screen, Turtle

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]
angles = [90, 180, 270, 0]
timmy_the_turtle = Turtle()
# timmy.shape("turtle")
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")


def move_turtle(t_angle):
    timmy_the_turtle.forward(30)
    timmy_the_turtle.right(t_angle)


for _ in range(1000):
    timmy_the_turtle.color(random.choice(colours))
    move_turtle(random.choice(angles))

screen = Screen()
screen.exitonclick()
