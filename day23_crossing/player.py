from turtle import Turtle
TURTLE_SPEED = 20

class Player(Turtle):
    """Player Class"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.setheading(90)
        self.reset_player()

    def move_up(self):
        """Moving the turtle up"""
        new_y = self.ycor()+TURTLE_SPEED
        self.goto(self.xcor(),new_y)
    
    def reset_player(self):
        print("Player reset!")
        self.goto(0,-280)



