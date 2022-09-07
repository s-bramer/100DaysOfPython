from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.update()
    
    def update(self):
        self.goto(0,280)
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 12, 'bold'))
        