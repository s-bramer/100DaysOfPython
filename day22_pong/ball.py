from turtle import Turtle
BALL_SPEED = 2
BALL_DIRECTION = 45

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__() 
        self.shape("circle")
        self.color("red")
        self.penup()
        self.setheading(BALL_DIRECTION)

    def move(self):
        self.forward(BALL_SPEED)
    
#if ball.xcor() > 390 or ball.xcor() < -390 or ball.ycor() > 290 or ball.ycor() < -290:

    def bounce(self, wall):
        """Change direction of ball when wall hit"""
        #hitting the right border
        if wall == "right":
            if self.heading() == 45:
                self.setheading(135)
            else:
                self.setheading(225)
        #hitting the left border
        if wall == "left":
            if self.heading() == 135:
                self.setheading(45)
            else:
                self.setheading(315)
        #hitting the top
        if wall == "top":
            print("hit the top")
            if self.heading() == 45:
                print("change direction")
                self.setheading(315)
            else:
                self.setheading(225)
        #hitting the bottom      
        if wall == "bottom":
            if self.heading() == 315:
                self.setheading(45)
            else:
                self.setheading(135)

