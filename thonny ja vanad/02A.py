
#tehvan marjapuu 14.11.23-21.11.23

#------------------------------
#Arvutame kolmnurga ümbermõõdu
#Loo kolm täisarvulist muutujat a, b, c
#Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
#----------------------------------
"""
a = 5
b = 10
c = 15
P = a+b+c

print("kolmnurga ümbermõõt on:",P)
"""
#--------------------
#Toote hind
#Toote hind 36,75€
#Soodushind hetkel 40%
#Soovin kolme toote summat
#---------------------
"""
hind = 36.75
soodus = 0.4
kokku = hind*soodus*3
print("kolme pitsa hind on:",kokku)
"""
#--------------------
# Pitsa
# Võtsite 3 sõbraga suure pitsa hinnaga 12,90€
# Jätate teenindajale 10% jootraha
# Koosta programm, mis leiab kui palju peab igaüks maksma
#--------------------
"""
sobrad = 3
Spizza = 12.9
tip = 0.1
Kokku = (Spizza * tip+Spizza)/sobrad
print("igaüks maksab "+str(Kokku)+"$")
"""
#--------------------
#Rulluisutajad
#Rulluisutaja keskmine kiirus on 29,9km/h
#Kui kaugele jõuab 24minutiga
#--------------------
"""
kiirus = 29.9
aeg = 24
Tee_Pikkus = kiirus/ 60 *aeg
print("kaugus",round(Tee_Pikkus,2),"km")

"""
#--------------------
# Leia kolmnurga hüpotenuus
# Kolmnurga külgede pikkused on a=16 ja b=9
# Kasuta Pythagorase teoreemi (a2 + b2 = c2) ja leia kolmnurga hüpotenuus
#--------------------
"""
from math import *
a, b = 16, 9
c = sqrt(a**2 + b**2) 
print("vastus:",c)
"""
#--------------------
#Ajateisendus
#Kasutaja sisestab aja minutites
#Sinu valem leiab ja väljastab tunnid ja minutid
#Näiteks: sisestus 72, vastus 1:12
#--------------------
"""
aeg = int(input("Sisesta aeg minutites: "))
h = aeg // 60
m = aeg % 60
print (h,":",m)
"""
#--------------------
#Arvusüsteemid
#Kasutaja sisestab täisarvu kümnendsüsteemis
#Sinu programm teisendab selle 2nd ja 16nd süsteemi
#--------------------
"""
arv = int(input("sisesta 10nd arv: "))
bii = bin(arv)
heks =hex(arv)
print("kümnendarv",arv,"kahendsüsteemis",bii,"ja kuueteistkümnendsüsteemis",heks)
"""
#--------------------'
#Kütusekulu arvutamine
#Kasutaja sisestab tangitud kütuse liitrid
#Kasutaja sisestab läbitud kilomeetrid
#Programm leiab kütusekulu 100km kohta keskmiselt
#--------------------
"""
l = int(input("Lisa tangitud kütuse kogus: "))
Km = int(input("Lisa läbitud Km kogus: "))
kulu = l / (Km /100)
print("sinu masin võtab keskmiselt",kulu,"liitrit 100kmle")

"""

#Kilpkonn küsib kasutajalt, kui suurt ruutu tahad ja joonistab ruudu (kasuta funktsiooni)

import turtle
W = turtle.Screen()
def ruut(k):
    M = turtle.Turtle()
    for i in range(4):
        M.fd(k)
        M.rt(90)

kylg =W.numinput("joonistame ruudu","sisesta ruudu külje pikkus: ")
ruut(kylg)

turtle.exitonclick()







