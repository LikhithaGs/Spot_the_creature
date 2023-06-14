import turtle
import pandas

screen = turtle.Screen()

screen.title("Spot the Creature Game")
image = "animals_image.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("animals.csv")
animal_list = data['Animals'].to_list()
animals = []
while len(animals) < 9:
    user_guess = screen.textinput(title="Welcome to spot Game",prompt="Guess the creature in the given Image..").title()
    if user_guess == 'Exit':
        break
    if user_guess in animal_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        animal_data = data[data.Animals == user_guess]
        t.goto(int(animal_data.x),int(animal_data.y))
        t.color("Black")
        t.write(user_guess,font=('Courier', 16, 'italic'))
