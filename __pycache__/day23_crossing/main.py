from turtle import Screen
from player import Player
import time

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    #create cars at random positions 
    #check if car has hit turtle
    #check if turtel has reached other side
            
screen.exitonclick()