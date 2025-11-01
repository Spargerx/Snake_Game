import turtle as t
from snake import Snake
from food import Food
from scorecard import Scorecard
import time

SNAKE_LIMIT = 290

t.colormode(255)

screen = t.Screen()

screen.setup(width=600, height=600)
screen.bgcolor(12, 17, 36)
screen.title("Snake Game")
screen.tracer(0) # turns off the turtle animation

snake = Snake()
food = Food()
scorecard = Scorecard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    
game_is_on = True

while game_is_on:
    screen.update() # refreshes the screen
    time.sleep(0.15) # controls the speed of the Snake (lower the value , faster the snake)
    snake.move()
    
    # detect collision with food
    if snake.head.distance(food) < 15:
        scorecard.increase_score()
        snake.extend()
        food.refresh()
        
    # detect collision with wall
    if abs(snake.head.xcor()) > SNAKE_LIMIT or abs(snake.head.ycor()) > SNAKE_LIMIT:
        scorecard.reset()
        snake.reset()
        
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scorecard.reset()
            snake.reset()

screen.exitonclick()

