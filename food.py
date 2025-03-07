import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")

    def move(self):
        self.goto(random.randint(-280, 280,), random.randint(-280, 280))
