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

while game_is_on:
    answer_state = screen.textinput(title=game_title, prompt="What's another state's name?").lower()
    print(answer_state)

turtle.mainloop()
