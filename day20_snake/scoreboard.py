from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    """Class Scoreboard - inherits from Turtle"""
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.update()
    
    def update(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font= FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=('Courier', 24, 'bold'))
        