from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

class Snake:
    """This is the snake class"""
    def __init__(self) -> None:
        #self.length = 3
        self.pixel = 20
        self.segments = []
        self.create_snake()

    def move(self):
        """Moving the snake about"""
        for x in range(len(self.segments)-1,0,-1):
            new_x = self.segments[x-1].xcor()
            new_y = self.segments[x-1].ycor()
            self.segments[x].goto(new_x,new_y)
        self.segments[0].forward(self.pixel)    

    def create_snake(self):
        """Inital step to create starting snake"""
        for segment in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(segment)
            self.segments.append(new_segment)
    def up(self):
        """Moves the snake up"""
        self.segments[0].setheading(90)    
    def down(self):
        """Moves the snake down"""
        self.segments[0].setheading(270)
    def left(self):
        """Moves the snake left"""
        self.segments[0].setheading(180)   
    def right(self):
        """Moves the snake right"""
        self.segments[0].setheading(0)