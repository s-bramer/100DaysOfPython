from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 30, 'bold')

class Board(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.draw_net()
        self.score_l = 0
        self.score_r = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,250)
        self.write(f"P1: {self.score_l}", move=False, align=ALIGNMENT, font= FONT)
        self.goto(100,250)
        self.write(f"P2: {self.score_r}", move=False, align=ALIGNMENT, font= FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=('Courier', 24, 'bold'))

    def draw_net(self):
        for y_pos in range(260, -310, -30):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.shapesize(stretch_len=0.3,stretch_wid=1)
            new_segment.penup()
            new_segment.goto(0,y_pos)

    def increases_score_r(self):
        self.score_r += 1
        self.update_score()

    def increases_score_l(self):
        self.score_l += 1
        self.update_score()