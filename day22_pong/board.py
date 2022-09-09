from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')

class Board(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.update()
        self.draw_net()
        self.score_l = 0
        self.score_r = 0

    def update(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font= FONT)
    
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