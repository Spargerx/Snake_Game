from turtle import Turtle
POSITION = 270
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(x=0, y=POSITION)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(arg=f"Score:{self.score}    High Score:{self.high_score}", align= ALIGNMENT, font=FONT)
        print(self.high_score)
        
    def reset(self):
        if self.score>=self.high_score:
            self.high_score=self.score
            with open("./data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1    
        self.update_scoreboard()
