import turtle as t
import random

t.speed(1000)
t.bgcolor("black")
t.pensize(1)
colors = ["white", "gold"]

for i in range(100):
    t.lt(145)
    for j in range(5):
        n = random.choice(colors)
        t.color(n)
        t.fd(250)
        t.lt(150)
        t.hideturtle()

t.done()