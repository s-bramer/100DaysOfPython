from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_over = False
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while not game_over:
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300:
        screen.textinput("GAME OVER", "END")
        exit()




screen.exitonclick()