from turtle import Turtle
POSITION = 270
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(x=0, y=POSITION)
        self.score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score}", align= ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1    
        self.update_scoreboard()
        
    def game_over(self):
        self.setposition(0,0)
        self.write(arg="GAME OVER", align= ALIGNMENT, font=FONT)
        