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
timmy = Turtle()
# timmy.shape("turtle")
timmy.pensize(10)
timmy.speed("fastest")


def move_turtle(t_angle):
    timmy.forward(30)
    timmy.right(t_angle)


for _ in range(1000):
    timmy.color(random.choice(colours))
    move_turtle(random.choice(angles))

screen = Screen()
screen.exitonclick()
