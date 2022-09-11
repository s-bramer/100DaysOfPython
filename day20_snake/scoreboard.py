from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    """Class Scoreboard - inherits from Turtle"""
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("./day20_snake/data.txt", "r") as file:
            contents = file.read().split()[0]
        self.highscore = int(contents)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.update()
    
    def update(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font= FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./day20_snake/data.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update()
        