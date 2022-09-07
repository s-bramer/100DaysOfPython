from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_over = False

while not game_over:
    screen.update()
    snake.move()
    time.sleep(0.05)
    
    #detect collision with the FOOD
    if snake.head.distance(food) <15:
        food.redraw()
        score.score += 1
        score.update()
        snake.extend()

    #detect collision with the WALLS
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_over = True
    
    #detect collision with the snake body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_over = True 

screen.exitonclick()