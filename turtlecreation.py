import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
t.color("magenta", 'cyan')
screen.bgcolor('black')
t.shapesize(2.0, 2.0, 5)
screen.bgpic("galaxy.gif")
t.penup()
t.setpos(-1000, -800)
t.pendown()

#t.begin_fill()
t.speed(10)
turtle.tracer(0, 0)
angle = 0.05
for i in range(999909):
    t.forward(4)
    t.left(math.pow(angle, math.e))
    angle += 0.005
#t.end_fill()
turtle.update()
turtle.done()
