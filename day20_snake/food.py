import random
from turtle import Turtle

class Food:
    """This is the snake food class"""
    def __init__(self) -> None:
        self.food_x = random.randint(-13,13)*20
        self.food_y = random.randint(-13,13)*20
        self.food = Turtle("square")
        self.food.color("red")
        self.food.penup()
        self.food.goto(self.food_x, self.food_y)

    def has_eaten(self,x_snake,y_snake):
        """Checks whether snake head is on top of food"""
        return self.food_x == x_snake and self.food_y == y_snake

    def clear_table(self):
        """Delete food once eaten"""
        self.food.clear()
