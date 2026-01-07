import turtle
import pandas

# Set up screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Users/michelle/PycharmProjects/PythonProject1/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read data
data = pandas.read_csv("50_states.csv")
states_list = data.state.tolist()

# Track guessed states
guessed_states = []

# Create a turtle for writing state names
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("black")

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Guessed",
        prompt="What's another state's name?"
    )

    if answer_state is None:  # User clicked Cancel
        break

    answer_state = answer_state.title()

    if answer_state in states_list and answer_state not in guessed_states:
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

# Save states to learn
missing_states = [state for state in states_list if state not in guessed_states]
pandas.DataFrame(missing_states).to_csv("states_to_learn.csv", index=False)

screen.exitonclick()
