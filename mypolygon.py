
import turtle
import math
bob = turtle.Turtle()
alice = turtle.Turtle()
  

def square(t, length):
    # Рисует квадрат с length(длиной сторон)
    for i in range(4):
        t.fd(length)
        t.lt(90)



def polyline(t, n, length, angle):
    """Рисует n отрезков с заданной длинной lenght и углами angle (в градусах) между ними.
         t - это черепашка """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """Рисует многоугольник с n количеством сторон и lenght длиной сторон"""
    angle = 360.0 / n
    polyline(t, n, length, angle)   

def circle(t, r):
    """Рисует круг r радиуса"""
    arc(t, r, 360)

def arc(t, r, angle):
    """Рисует дугу с заданным радиусом и углом.
    t: Черепаха
    r: радиус
    angle: угол, образованный дугой, в градусах."""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1s
    step_length = arc_length / n 
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

circle(bob, 30)
circle(alice, 100)
)
turtle.mainloop()