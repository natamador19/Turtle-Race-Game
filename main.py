import random
from platform import win32_is_iot
from turtle import  Turtle,Screen


screen= Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet", prompt="Which color will win the rance? Enter a color: ")
print(user_bet)
colors=["red","orange","yellow","green","blue","purple"]
all_turtles=[]
is_race_on=False
position=[150,100,50,0,-50,-100]
for turtle_index in range (0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=position[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color= turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You ´ve won! The {winning_color} turtle is the winner!")
            else:
                print(f"You ´ve lost! The {winning_color} turtle is the winner!")
        rand_distance= random.randint(0,10)
        turtle.forward(rand_distance)








screen.exitonclick()


