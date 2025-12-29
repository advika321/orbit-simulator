import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Orbit Simulator")
screen.tracer(0)   

sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2)
sun.penup()
sun.goto(0, 0)

planet = turtle.Turtle()
planet.shape("circle")
planet.color("cyan")
planet.shapesize(0.7)
planet.penup()

info = turtle.Turtle()
info.hideturtle()
info.color("white")
info.penup()
info.goto(-300, 250)

radius = 150      #distance from sun
angle = 0         #starting angle
speed = 0.05      #speed of orbit

def update_info():
    info.clear()
    circumference = 2 * math.pi * radius

    info.write(
        f"Radius: {radius}\n"
        f"Circumference: {circumference:.2f}\n"
        f"Speed: {speed:.2f}",
        font=("Arial", 12, "normal")
    )


def increase_radius():
    global radius
    radius += 10

def decrease_radius():
    global radius
    if radius > 30:
        radius -= 10

def increase_speed():
    global speed
    speed += 0.01

def decrease_speed():
    global speed
    if speed > 0.01:
        speed -= 0.01

screen.listen()
screen.onkey(increase_radius, "Up")
screen.onkey(decrease_radius, "Down")
screen.onkey(increase_speed, "Right")
screen.onkey(decrease_speed, "Left")

while True:
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)

    planet.goto(x, y)

    angle += speed
    update_info()
    screen.update()
    time.sleep(0.02)
