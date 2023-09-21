import turtle
import random
import time
myscreen = turtle.Screen()
myscreen.bgcolor('black')
myscreen.setup(600, 600)
myscreen.title("snake game")

snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("green")
snake_head.penup()
snake_head.speed("fastest")

snake_head.direction = ""

snake_food = turtle.Turtle()
snake_food.shape("circle")
snake_food.color("red")
snake_food.penup()
snake_food.speed("fastest")
x = random.randint(-270, 270)
y = random.randint(-270, 230)
snake_food.goto(x, y)


def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)


def go_up():
    snake_head.direction = "up"


def go_down():
    snake_head.direction = "down"


def go_left():
    snake_head.direction = "left"


def go_right():
    snake_head.direction = "right"


myscreen.listen()
myscreen.onkeypress(go_up, "Up")
myscreen.onkeypress(go_down, "Down")
myscreen.onkeypress(go_left, "Left")
myscreen.onkeypress(go_right, "Right")
myscreen.tracer(False)
score = 0
scoreboard = turtle.Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(0, 260)
scoreboard.speed("fastest")

scoreboard.ht()

running = True
while running == True:
    scoreboard.clear()
    scoreboard.write(f"Score: {score}", font=("arial", 22), align="center")
    myscreen.update()
    if snake_head.distance(snake_food) < 20:
        score += 1
        x = random.randint(-270, 270)
        y = random.randint(-270, 230)
        snake_food.goto(x, y)

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        score = 0
        snake_head.goto(0, 0)
        snake_head.direction = ""

    move()
    time.sleep(0.2)
