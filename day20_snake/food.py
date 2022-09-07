import random
from turtle import Turtle

class Food(Turtle):
    """This is the snake food class"""
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.redraw()

#    def has_eaten(self,x_snake,y_snake):
#        """Checks whether snake head is on top of food"""
#        return self.food_x == x_snake and self.food_y == y_snake

#    def clear_table(self):
#        """Delete food once eaten"""
#        self.clear()

    def redraw(self):
        """Draw a new food item"""    
        food_x = random.randint(-13,13)*20
        food_y = random.randint(-13,13)*20
        self.goto(food_x, food_y)

