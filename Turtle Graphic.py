import turtle
import random
colors = ["red", "blue", "green", "orange","violet", "purple"]
turtle.speed(5)
# Draws "J" with block width 10
turtle.color(colors[random.randint(0,5)])
turtle.penup()
turtle.setx(-300)
turtle.pendown()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(140)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(10)
turtle.begin_fill()
turtle.penup()

# Draws "A"
turtle.color(colors[random.randint(0,5)])
turtle.setx(-240)
turtle.sety(-50)
turtle.pendown()
turtle.right(105)
turtle.forward(151)
turtle.right(150)
turtle.forward(151)
turtle.right(105)
turtle.forward(10)
turtle.right(75)
turtle.forward(112)
turtle.left(150)
turtle.forward(112)
turtle.right(75)
turtle.forward(10)
turtle.penup()

# Draws "C"
turtle.color(colors[random.randint(0,5)])
turtle.setx(-155)
turtle.sety(-50)
turtle.pendown()
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(130)
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(50)
turtle.penup()

# Draws "K"
turtle.color(colors[random.randint(0,5)])
turtle.setx(-95)
turtle.sety(-50)
turtle.pendown()
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(70)
turtle.left(160)
turtle.forward(75)
turtle.right(70)
turtle.forward(10)
turtle.right(110)
turtle.forward(95)
turtle.left(50)
turtle.forward(75)
turtle.right(120)
turtle.forward(10)
turtle.right(60)
turtle.forward(62)
turtle.left(150)
turtle.forward(52)
turtle.right(90)
turtle.forward(10)
turtle.penup()

turtle.color(colors[random.randint(0,5)])
turtle.setx(0)
turtle.sety(15)
turtle.pendown()
turtle.right(120)

for i in range(36):
	turtle.forward(120)
	turtle.right(170)


turtle.exitonclick()
