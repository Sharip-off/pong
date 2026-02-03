from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.screensize(800, 600, "black")
screen.title("Pong")

user_paddle = Paddle()
user_paddle.goto(350, 0)

screen.listen()

screen.onkey(user_paddle.go_up, "Up")
screen.onkey(user_paddle.go_down, "Down")

screen.exitonclick()