from turtle import Turtle

class Player(Turtle):
    """Player Class"""
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def move_up(self):
        new_y = self.ycor()+10
        self.goto(self.xcor(),new_y)


