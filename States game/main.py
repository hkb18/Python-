import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

### GET MOUSE COORDINATES
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's the another state's name?").title()

    if answer_state == "Exit":
        missing_states = [states for states in all_states if states not in guessed_states]
        # for states in all_states:
        #     if states not in guessed_states:
        #         missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)  # t.write(state_data.state.item())
