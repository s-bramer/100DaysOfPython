from turtle import Screen, Turtle
from paddle import Paddle, RightPaddle,LeftPaddle
from board import Board
from ball import Ball
import time

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

board = Board()
right_paddle = RightPaddle()
left_paddle = LeftPaddle()
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "q")
screen.onkeypress(left_paddle.move_down, "a")


game_over = False

while not game_over:
    ball.move()
    screen.update()
    if ball.xcor() > 390:
        ball.bounce("right")
    elif ball.xcor() < -390:
        ball.bounce("left")
    elif ball.ycor() > 290:
        ball.bounce("top")
    elif ball.ycor() < -290:
        ball.bounce("bottom")
screen.exitonclick()