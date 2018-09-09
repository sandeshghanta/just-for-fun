import random
import turtle
tu = turtle.Turtle()
turtle.colormode(255)
tu.hideturtle()
tu.speed(0)
x = 100
y = 121
z = 4
for i in range(y):
    r = random.randrange(0, 257, 10)
    g = random.randrange(0, 257, 10)
    b = random.randrange(0, 257, 10)
    tu.forward(x)
    tu.left(90)
    if (i % 4 == 0 and i != 0):
        tu.color(r, g, b)
        tu.penup()
        tu.forward(z)
        tu.left(90)
        tu.forward(z)
        tu.right(90)
        tu.pendown()

turtle.mainloop()

