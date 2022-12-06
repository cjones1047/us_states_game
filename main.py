import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
game_title = "Guess the State"
correct_guesses = []

new_state = turtle.Turtle()
new_state.penup()
new_state.hideturtle()
new_state.speed("normal")

df = pandas.read_csv("50_states.csv")

while game_is_on:
    answer_state = screen.textinput(title=game_title, prompt="What's another state's name?").title()
    state_row = df[df["state"] == answer_state]
    if len(state_row) > 0:
        state_name = state_row.state.item()
        new_state.goto(state_row.x.item(), state_row.y.item())
        new_state.write(state_name, align="left", font=("Arial", 8, "normal"))
        correct_guesses.append(state_name)
        game_title = f"{len(correct_guesses)}/50 States Correct"
