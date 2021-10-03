import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()
already_guessed = []


while len(already_guessed) < 50:
    answer_state = screen.textinput(title=f"{len(already_guessed)}/50 States Correct",
                                        prompt="What's another state's "
                                               "name?                              ").title()

    if answer_state == "Exit":
        missing_states = [state for state in data_list if state not in already_guessed]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if answer_state in data_list:

        already_guessed.append(answer_state)
        states_write = turtle.Turtle()
        states_write.hideturtle()
        states_write.penup()
        state_data = data[data.state == answer_state]
        states_write.goto(int(state_data.x), int(state_data.y))
        states_write.write(answer_state)


