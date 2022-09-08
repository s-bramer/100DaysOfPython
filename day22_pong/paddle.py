from turtle import Turtle

RIGHT_PADDLE_X = 380
LEFT_PADDLE_X = -380

class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+10)

    def move_down(self):
        self.goto(self.xcor(),self.ycor()-10)

class RightPaddle(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(RIGHT_PADDLE_X,0)  

class LeftPaddle(Paddle):
    def __init__(self) -> None:
        super().__init__()
        self.goto(LEFT_PADDLE_X,0)  