from turtle import Turtle
import random

END_X = 270
END_Y = 270

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("magenta")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.speed(0)
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-END_X, END_X)
        random_y = random.randint(-END_Y, END_Y)
        self.setposition(random_x, random_y)
