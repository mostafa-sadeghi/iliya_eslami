# for i in range(5):
#     print("hello")


# for n in range(5):
#     print(n, end="-")
#     print("hello")

import turtle

my_screen = turtle.Screen()
my_screen.bgcolor("cyan")
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(2)
my_turtle.color("red")
my_turtle.pensize(3)

sides = int(my_screen.textinput("info","How many Sides?"))

for i in range(sides):
    my_turtle.forward(150)
    my_turtle.left(360/sides)

turtle.done()

