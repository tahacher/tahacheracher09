'snack  game'
import turtle
import time
import random

delay = 0.1
score = 0

#screen setup
win = turtle.Screen()
win.title("Snack Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

#Snack head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
head.goto(0, 100)


segments = []


#Mouvment function
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.sety(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.sety(x + 20)


#keyboard binding
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")


#Main game loop
while True:
    win.update()
    #collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or  head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0

    #collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)


        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        score += 10


    #move segment
    for i in range(len(segments)-1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    
    if segments:
        segments[0].goto(head.xcor(), head.ycor())


    move()
    time.sleep(delay)

