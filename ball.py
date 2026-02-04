from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")

    def move(self):
        move_is_on = True
        while move_is_on:
            new_x = self.xcor()+10
            new_y = self.ycor()+8
            self.goto(new_x, new_y)
