from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_over = False
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while not game_over:
    snake.move()
    if food.has_eaten(snake.head.xcor(),snake.head.ycor()):
        #food.clear_table()
        food = Food()
        print("MUNCH MUNCH MUNCH!!")
    screen.update()
    time.sleep(0.2)
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        screen.textinput("GAME OVER", "END")
        exit()




screen.exitonclick()