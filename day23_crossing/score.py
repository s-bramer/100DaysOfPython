from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 30, 'bold')

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.number = 1
        self.update_score()

    def update_score(self):
        print("Score updated!")
        self.clear()
        self.goto(-200,250)
        self.write(f"Level: {self.number}", move=False, align=ALIGNMENT, font= FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=('Courier', 24, 'bold'))

    def next_level(self):
        self.number += 1
        print(f"Level: {self.number}")
        self.update_score()