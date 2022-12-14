from turtle import Screen, Turtle
from paddle import Paddle, RightPaddle,LeftPaddle
from board import Board
from ball import Ball
import time

screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
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
    time.sleep(0.5)
    # check if ball hit the top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with paddles
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 40 and ball.xcor() > -330:
        print("left paddle!!")
        ball.bounce_x()

    #check if right player scored
    if ball.xcor() < -390:
        board.increases_score_r()
        ball.reset_ball()

    #check if right player scored
    if ball.xcor() > 390:
        board.increases_score_l()
        ball.reset_ball()
        
screen.exitonclick()