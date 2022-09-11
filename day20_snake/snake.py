from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    """This is the snake class"""
    def __init__(self) -> None:
        #self.length = 3
        self.pixel = 20
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
    
    def create_snake(self):
        """Inital step to create starting snake"""
        for segment in STARTING_POSITION:
            self.add_segements(segment)
    
    def move(self):
        """Moving the snake about"""
        for x in range(len(self.segments)-1,0,-1):
            new_x = self.segments[x-1].xcor()
            new_y = self.segments[x-1].ycor()
            self.segments[x].goto(new_x,new_y)
        self.head.forward(self.pixel)      

    def add_segements(self, position):
        """Adds segments to the snake body"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        """Extends snake by one segement (when food was eaten)"""
        self.add_segements(self.tail.position())
    
    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]
    
    def up(self):
        """Moves the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)    
    def down(self):
        """Moves the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        """Moves the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)   
    def right(self):
        """Moves the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)