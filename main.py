import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
game_title = "Guess the State"
correct_guesses = 0

df = pandas.read_csv("50_states.csv")

while game_is_on:
    answer_state = screen.textinput(title=game_title, prompt="What's another state's name?").title()
    state_row = df[df["state"] == answer_state]
    print(state_row)
