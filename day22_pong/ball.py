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
    
#if ball.xcor() > 390 or ball.xcor() < -390 or ball.ycor() > 290 or ball.ycor() < -290:

    def bounce_y(self):
        """Change direction of ball when wall hit"""
        print ("hit the top/bottom")
        self.y_move *= -1
    
    def bounce_x(self):
        """Change direction of ball when wall hit"""
        print ("hit the side")
        self.x_move *= -1


