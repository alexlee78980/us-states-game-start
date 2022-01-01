from turtle import Screen, Turtle
import pandas

screen = Screen()
turtle = Turtle()
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
turtle_move = Turtle()
turtle_move.penup()
turtle_move.hideturtle()
states_cords = pandas.read_csv("50_states.csv")
correct = 0
while correct != 50:
    name = screen.textinput(title= f"Guess the States {correct}/50", prompt="What's another state's name?")
    cords = states_cords[states_cords.state == name.title()]
    print(cords)
    if not cords.empty:
        turtle_move.goto(int(cords.x), int(cords.y))
        turtle_move.write(name.title())
        correct += 1
turtle_move.goto(-100, 0)
turtle_move.write("Congratulations, you guessed all 50 states!!!")

screen.exitonclick()