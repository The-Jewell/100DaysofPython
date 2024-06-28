# game where you enter a state name and it prints the name of the state on the map over its location. if you type
# "Exit" it will print out a list of the states you didnt guess

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()


def new_turtle_for_state(state_name):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    state_coord = state_data[state_data.state == answer_state.title()]
    new_turtle.goto(int(state_coord.x), int(state_coord.y))
    new_turtle.write(state_name)


correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's "
                                                                                              "name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        correct_guesses.append(answer_state)
        new_turtle_for_state(answer_state)









