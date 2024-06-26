from turtle import Turtle
snake_squares = []
STARTING_POSITIONS=[(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_squares = []
        self.create_snake()
        self.head = self.snake_squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def reset_snake(self):
        for square in self.snake_squares:
            square.goto(2000,2000)
        self.snake_squares.clear()
        self.create_snake()
        self.head = self.snake_squares[0]

    def move_snake(self):
        for square_num in range(len(self.snake_squares) - 1, 0, -1):
            new_x = self.snake_squares[square_num - 1].xcor()
            new_y = self.snake_squares[square_num - 1].ycor()
            self.snake_squares[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_square(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.snake_squares.append(new_square)

    def extend(self):
        self.add_square(self.snake_squares[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





