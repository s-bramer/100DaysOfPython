from turtle import Turtle
import random

COLORS = ["red","green","purple","violet","yellow","blue","brown","white"]

class Car:
    """This is the snake class"""
    def __init__(self):
        self.cars = []
        self.number_of_cars = 3
        self.create_car(self.number_of_cars)
        self.speed_multiplier = 2

    def move_cars(self):
        for x in range(len(self.cars)):
            self.cars[x].forward(self.cars[x].speed()*self.speed_multiplier)
    
    def create_car(self, number_of_cars):
        for number in range(number_of_cars):
            rand_x_position = random.randint(300,320)
            rand_y_position = random.randint(-25,25)*10
            rand_speed = random.randint(0,10)
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.speed(rand_speed)
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.goto(rand_x_position, rand_y_position)
            self.cars.append(new_car)

    def add_car(self):
        self.create_car(1)

    def level_up(self):
        print("Speed increased!")
        self.speed_multiplier += 0.2