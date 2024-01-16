import turtle

#akna seaded
aken = turtle.Screen()
aken.setup(600,600)
aken.title("Ülesanded 1-2 T.Marjapuu")


edasi = 100
nurk = 144
kokku = 5

varv = 'green'


def joonistakolmnurk(l, c):
    k = turtle.Turtle()
    k.color(c)
    for x in range(3):
        k.fd(-l)
        k.right(120)


k = turtle.Turtle()
for x in range(kokku):
    k.fd(edasi)
    k.right(nurk)
           
joonistakolmnurk(edasi, varv)
turtle.exitonclick()