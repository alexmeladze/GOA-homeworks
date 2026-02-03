from turtle import *

#build a house
width(7)
speed(1)

color("purple")

forward(200)
left(90)

forward(230)
left(90)

forward(200)
left(90)

forward(230)
left(90)
#build a door
forward(75)
color("yellow")
left(90)

forward(115)
right(90)

forward(50)
right(90)

forward(115)
#build the roof
penup()
goto(200,230)
pendown()
color("red")
right(150)
forward(180)
left(115)
forward(190)
# build the windows
penup()
goto (0,0)
pendown()
right(145)
color("purple")
forward(150)
right(90)
penup()
forward(30)
pendown()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward (50)
right(90)
penup()
forward(100)
pendown()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
# fix the door with color
penup()
goto(0,0)
pendown()
right(90)
forward(70)
color("yellow")
forward(60)

exitonclick()


