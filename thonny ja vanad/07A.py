#tehvan marjapuu
#5.12.23
import math

def kera(r):
    v = round((4*math.pi*r**3)/3,2)
    print(f"kera ruumala on {v}")

def kuup(a):
    v= a**3
    print(f"kuubi ruumala on {v}")

def koonus(r, h):
    print(f"koonuse ruumala on ")


def silinder(r, h):
    print(f"silindri ruumala on ")

loop = 1

while loop ==1:

    print("****************************MEGA HEA KALK***********************************")
    print("1, kera/2. kuup/3. koonus/4. silinde/5. EXIT\n")
    valik = int(input("SISESTA VALIK:"))



    print("***************************************************************")

    if valik ==1:
        r = int(input("sisesta kera ruumala:   "))
        kera(r)
    elif valik ==2:
        k = int(input("sisesta kuubi külg:   "))
        kuup(k)
    elif valik ==3:
        koonus
    elif valik ==4:
        silinder
    else:
        loop = 0
        print("thx et kasutasid")




"""
def tervita(nimi, keel="ge"):
    if keel=="en":
        print(f"Hi {nimi}")
    elif keel=="et":
        print(f"Tere {nimi}")
    else:
        print(f"Hallo {nimi}")

tervita("märt","en")
tervita("märt","et")
tervita("märt","wabsioosen")
tervita("märt")
"""









