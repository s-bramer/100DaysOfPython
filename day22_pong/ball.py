from turtle import Turtle
BALL_SPEED = 10
BALL_DIRECTION = 45

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__() 
        self.shape("circle")
        self.color("red")
        self.penup()
        self.setheading(BALL_DIRECTION)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
    
    def reset_ball(self):
        self.goto(0,0)
        self.x_move *= -1


