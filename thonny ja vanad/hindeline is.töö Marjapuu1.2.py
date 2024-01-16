# Tehvan Marjapuu
# 18.12.23


import winsound
import random
"""
Otil on hommikuti raske tõusta ja tal on äratuskell, mis äratab teda teatud arv kordi koos tervitustekstiga. Koosta programm, mis

    küsib kasutajalt, mitu korda äratus heliseb ning
    väljastab sama arv kordi ekraanile Tõuse ja sära!
"""

def aratus (nr):
    for i in range(nr):
        winsound.Beep(2500,1200)
        print("Tõuse ja sära!")

"""
Jänestevanemad on mures, et lapsed ei liigu piisavalt. Laste motiveerimiseks mõtlesid nad välja 
süsteemi, kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4 
progandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel
porgandeid juurde ei saa.

Koostada programm, mis
    küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
    arvutab while-tsükli abil saadavate porgandite koguarvu;
    väljastab saadavate porgandite koguarvu ekraanile.
"""

def porgandid(r):
    ringid = 0
    porgandid = 0
    while ringid < r:
        ringid+=1
        if ringid%2 == 0:
            porgandid += ringid
    print(f"Porgandidte arv on: {porgandid} ")
porgandid(10) # siia peab panema seda int input v noh et r = int(input(f"sasfsfs"))

"""
Erinevate täringumängude jaoks on vajalik erinev arv täringuid. Näiteks Yahtzee (Yatzy) jaoks
on vaja 5 täringut, Crapsi jaoks aga 2 täringut. Koosta programm, mis
    küsib kasutajalt vajalike täringute arvu;
    viskab vastava arvu täringuid
    väljastab iga arvu eraldi reale
"""

def taringud(t):
    for i in range(t):
        print(random.randint(1,6))


def male(arv):
    ruut = 1
    nisuterad = 1
    while ruut < arv:
        nisuterad = nisuterad*2
        ruut +=1
    print(nisuterad) 

def lumi(p):
    ounad = 14
    for i in range(p):
        oun = random.randint(1,2)
        ounad -=oun
        print(oun)
    print(F"Lumivalgekesekesekele jäi {ounad} õuna")


#  kordused = int(input("Äratuste arv : "))
#  aratus(kordused)
#  ringid = int(input("Ringide arv : "))
#  porgandid(ringid)
# taringud(6)
#  male(5)
# lumi(6) 
#