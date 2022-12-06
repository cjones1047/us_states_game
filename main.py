import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_title = "Guess the State"
correct_guesses = []

new_state = turtle.Turtle()
new_state.penup()
new_state.hideturtle()
new_state.speed("normal")

df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=game_title, prompt="What's another state's name?").title()
    state_row = df[df["state"] == answer_state]
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in correct_guesses]
        missed_states_df = pandas.DataFrame(missed_states)
        missed_states_df.to_csv("missed_states.csv")
        break
    if len(state_row) > 0:
        state_name = state_row.state.item()
        new_state.goto(state_row.x.item(), state_row.y.item())
        new_state.write(state_name, align="left", font=("Arial", 8, "normal"))
        correct_guesses.append(state_name)
        game_title = f"{len(correct_guesses)}/50 States Correct"

# write states not guessed to csv
# missed_states = {
#     "state": [],
#     "x": [],
#     "y": []
# }
#
# for state in df["state"]:
#     if state not in correct_guesses:
#         x_cor = df[df["state"] == state].x.item()
#         y_cor = df[df["state"] == state].y.item()
#         missed_states["state"].append(state)
#         missed_states["x"].append(x_cor)
#         missed_states["y"].append(y_cor)
#
