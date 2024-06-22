import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_racers = []
y_axis = 200

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=y_axis)
    turtle_racers.append(new_turtle)
    y_axis -= 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_racers:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()