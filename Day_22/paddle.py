from turtle import Turtle
UP = 90
DOWN = 270
DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def paddle_up(self):
        if self.ycor() < 290:
            new_y = self.ycor() + DISTANCE
            self.goto(self.xcor(), new_y)

    def paddle_down(self):
        if self.ycor() > -290:
            new_y = self.ycor() - DISTANCE
            self.goto(self.xcor(), new_y)