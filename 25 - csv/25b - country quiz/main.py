import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
peter = turtle.Turtle()
peter.hideturtle()
peter.penup()

# not needed, as coords are already provided in "blank_states_img.gif"
#def get_mouse_click_coor(x, y):
#    print(x, y)
#turtle.onscreenclick(get_mouse_click_coor)

# load state data
data = pandas.read_csv("50_states.csv")
names = data["state"].to_list()

# game loop
guessed_states = 0
while guessed_states < 50:

    screen.title(f"{guessed_states}/50 U.S. States Game")
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    if answer_state is None:
        turtle.bye()
    elif answer_state == "exit":
        new_data = pandas.DataFrame(names)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        answer_state = answer_state.title()

    if answer_state in names:
        names.remove(answer_state)
        state = data[data.state == answer_state]
        peter.setx(int(state.x))
        peter.sety(int(state.y))
        peter.write(state.state.item(), align="center")
        guessed_states += 1

turtle.mainloop()
