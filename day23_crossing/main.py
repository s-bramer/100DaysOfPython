from turtle import Screen
from player import Player
from score import Level
from cars import Car
from datetime import datetime
import math
import time

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
cars = Car()
level = Level()
game_timer = 0
current_time = time.time()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_over = False


while not game_over:
    screen.update()
    time.sleep(0.1)
    cars.move_cars()
    game_time = time.time()
    if game_time - current_time >= 1:
        game_timer += int(game_time - current_time)
        cars.add_car()
        current_time = time.time()
        print(game_timer)

    #check if car has hit turtle
    for car in cars.cars:
        if car.distance(player) <20:
            print("hit")
            level.game_over()
            game_over = True

    #check if turtel has reached other side
    if player.ycor() > 250:
        print("next level")
        level.next_level()
        cars.level_up()
        player.reset_player()
            
screen.exitonclick()