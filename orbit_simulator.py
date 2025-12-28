# Simple Orbit Simulator using Turtle
# Concept: Circular orbital motion using basic trigonometry

import turtle
import math
import time

#Screen Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Orbit Simulator")
screen.tracer(0)   # smoother animation

#Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2)
sun.penup()
sun.goto(0, 0)

# Planet
planet = turtle.Turtle()
planet.shape("circle")
planet.color("cyan")
planet.shapesize(0.7)
planet.penup()

# -------------------- Info Display --------------------
info = turtle.Turtle()
info.hideturtle()
info.color("white")
info.penup()
info.goto(-300, 250)

# Orbit Parameters
radius = 150      # distance from sun
angle = 0         # starting angle
speed = 0.05      # speed of orbit

# -------------------- Update Info Text --------------------
def update_info():
    info.clear()
    circumference = 2 * math.pi * radius

    info.write(
        f"Radius: {radius}\n"
        f"Circumference: {circumference:.2f}\n"
        f"Speed: {speed:.2f}",
        font=("Arial", 12, "normal")
    )

#Radius Control Functions 
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

# Keyboard Binding
screen.listen()
screen.onkey(increase_radius, "Up")
screen.onkey(decrease_radius, "Down")
screen.onkey(increase_speed, "Right")
screen.onkey(decrease_speed, "Left")

# Orbit Loop
while True:
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)

    planet.goto(x, y)

    angle += speed
    update_info()
    screen.update()
    time.sleep(0.02)
