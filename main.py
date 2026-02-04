from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.screensize(800, 600, "black")
screen.title("Pong")
screen.tracer(0)


user_paddle = Paddle((350, 0))
ps_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()

screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    ball.move()

screen.exitonclick()