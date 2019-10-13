import turtle

theta = 60
relative_angles = [0, theta, 360-theta, 0]

def gotoinitposition(tut):
    tut.hideturtle()
    tut.penup()
    tut.setx(-450)
    tut.pendown()
    tut.speed(0)

class Line:
    def __init__(self, parent_line=None, type=None):
        if not parent_line:
            self.length = 900
            self.angle = 0
        else:
            self.length = parent_line.length/3.0
            self.angle = parent_line.angle + relative_angles[type]

    def reproduce(self):
        return [Line(self, type) for type in range(4)]

    def draw(self, tut):
        tut.setheading(self.angle)
        tut.forward(self.length)


if __name__ == "__main__":
    tut = turtle.Turtle()
    gotoinitposition(tut)
    root = Line(None)
    lines = [root]
    max_iter = 6
    for iter in range(max_iter):
        new_lines = []
        for line in lines:
            new_lines += line.reproduce()
        lines = new_lines
    for line in lines:
        line.draw(tut)
    turtle.done()
