from turtle import *
from turtleBeads import *

def staticFish():
    fillcolor("yellow")
    begin_fill()
    drawEllipse(50, 2)
    end_fill()

    penup()
    fd(50)
    lt(90)
    fd(15)
    rt(90)
    pendown()
    fillcolor("black")
    begin_fill()
    drawCircle(10)
    end_fill()

    penup()
    rt(90)
    fd(15)
    rt(90)
    fd(150)
    lt(180)
    pendown()
    fillcolor("green")
    begin_fill()
    rt(150)
    fd(65)
    rt(120)
    fd(65)
    rt(120)
    fd(65)
    lt(30)
    end_fill()

    penup()
    fd(50)
    pendown()


def fish(bodyColor, tailColor, x, y, scale, angle):
    teleport(x, y)

    lt(angle)

    fillcolor(bodyColor)
    begin_fill()
    drawEllipse(50*scale, 2)
    end_fill()

    penup()
    fd(50*scale)
    lt(90)
    fd(15*scale)
    rt(90)
    pendown()
    fillcolor("black")
    begin_fill()
    drawCircle(10*scale)
    end_fill()

    penup()
    rt(90)
    fd(15*scale)
    rt(90)
    fd(150*scale)
    lt(180)
    pendown()
    fillcolor(tailColor)
    begin_fill()
    rt(150)
    fd(65*scale)
    rt(120)
    fd(65*scale)
    rt(120)
    fd(65*scale)
    lt(30)
    end_fill()

    penup()
    fd(50*scale)
    pendown()

    rt(angle)

def drawCanvas(width, height, color):
    teleport(0, 0)
    fillcolor(color)
    begin_fill()
    drawRectangle(width, height)
    end_fill()

# Picture
setupTurtle()
drawCanvas(800, 800, "cyan")
fish("yellow", "green", -175, 200, 1.5, 45)
fish("blue", "red", 100, 100, 0.5, -45)
fish("purple", "blue", -200, -200, 1, 0)
fish("orange", "purple", 150, -150, 1.5, -60)


input("Press enter to exit the program")
