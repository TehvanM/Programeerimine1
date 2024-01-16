#Tehvan Marjapuu
# 28.11.23
"""
 funktsioon, mis loob erineva suuruse ja asukohaga ringe kogu platsi ulatuses
- funktsioon, mis loob erineva suuruse ja asukohaga ruutusid kogu platsi ulatuses
- funktsioon, mis kasutab eelmisi funktsioone, et luua suvaliselt ringe ja ristkülikuid
- küsib kasutajalt, et mingit atribuuti funktsioonis muuta (näiteks värv, suurus, koguarv)
"""


import turtle
import random

aken = turtle.Screen()
aken.setup(600,600)


mkujund= input("sisesta mis kujundit(1 on ruudud, 2 on ringid, 3 on segamini):  ")
koguarv= int(input("sisesta koguarv: "))
värv1= input("sisesta ruudu värv:  ")
värv2= input("sisesta ringi värv:  ")




def joonesta_ruudud():
    for i in range(1):
        x,y = random.randint(-300,300), random.randint(-300,300)
        z = random.randint(-150,150)
        t = turtle.Turtle()
        t.color(värv1)
        t.speed("fastest")
        t.penup()
        t.goto(x,y)
        t.pendown()
        for rr in range(2):
            t.forward(z)
            t.left(90)
            t.forward(z)
            t.left(90)
            t.hideturtle()
            
def joonesta_ringid():
    for i in range(1):
        r = random.randint(1, 100)
        x,y = random.randint(-300,300), random.randint(-300,300)
        t = turtle.Turtle()
        t.color(värv2)
        t.speed("fastest")
        t.hideturtle()
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(r)

def joonesta_suvalisikujundeid():
    suv = random.randint(1,2)
    if suv == 1:
        joonesta_ringid()
    else:
        joonesta_ruudud()

for i in range(koguarv):
    if mkujund == "1":
        joonesta_ruudud()
    elif mkujund == "2":
        joonesta_ringid()
    else:
        joonesta_suvalisikujundeid()
  
    

turtle.exitonclick()
