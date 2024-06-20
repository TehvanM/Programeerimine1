import turtle
#akna seaded
aken = turtle.Screen()
aken.setup(300,300)

t = turtle
for y in range(2):
    for x in range(4):
        t.forward(100)
        t.left(90)

    t.penup()
    t.left(45)
    t.fd(50)
    t.left(135)
    t.pendown()


turtle.exitonclick()