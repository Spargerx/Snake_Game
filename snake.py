import turtle as t
import time
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.can_turn = True
        
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.can_turn = True
        time.sleep(1)
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    
    def add_segment(self, position):
        new_segment = t.Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
            
    def extend(self):
        # add a new segment to the snake at the end of the snake
        self.add_segment(self.segments[-1].position())
               
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(STEP_SIZE)
        self.can_turn = True # allow turning after moving a step
        
        
    def up(self):
        if self.can_turn and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.can_turn = False #Prevent imidiate turn 
        
    def down(self):
        if self.can_turn and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.can_turn = False
        
    def left(self):
        if self.can_turn and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.can_turn = False
        
    def right(self):
        if self.can_turn and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.can_turn = False
            
