import turtle, math
scr = turtle.Screen() #where we're going to put our turtle myTurtle = turtle.Turtle()
myTurtle.color("green")
myTurtle.shape("turtle")
myTurtle.penup()
myTurtle.setx(200)
myTurtle.sety(200)
myTurtle.pendown()
size=400
numberOfSides = int(raw_input("How many sides? "))
for a in range(1,numberOfSides):
    myTurtle.forward(size/numberOfSides)
    myTurtle.left(360/numberOfSides)
wait = raw_input("Press Enter to continue...")
