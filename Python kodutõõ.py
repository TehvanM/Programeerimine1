#Tehvan Marjapuu
# 16.01.24
# Iseseisev

# 16. TÃ¤ringud
# 	Kasutaja vÃµistleb kahe tÃ¤ringuga arvuti vastu. Kasutaja teeb pakkumise ning suurima tÃ¤ringupunktisumma vÃµitja saab laual oleva raha endale juurde. MÃ¤ng kestab kuni kummalgi on raha otsas.
# 	(Vihjed: kÃ¼si kasutajalt nime, kuva pidevalt konto seisu ja tÃ¤ringuviskeid, kasutajate raha hulga mÃ¤ngu alguses mÃ¤Ã¤rad sina)

import random


def täringud():
    kasutaja = input("Sisesta nimi: ")
    raha = int(input("Sisesta raha: "))
    # ausalt võiks olla see arvuti raha random
    arvuti = 123 + random.randint(1,100)
    while raha > 0 and arvuti > 0:
        print(f"{kasutaja} raha: {raha}")
        print(f"Arvuti raha: {arvuti}")
        print(f"{kasutaja} viskab tärningu")
        # veits unfair no?
        ktäring = random.randint(1,6) + random.randint(1,6)
        print("Arvuti viskab tärningut")
        atäring = random.randint(1,6) 
        print(f"{kasutaja} tulemus: {ktäring}")
        print(f"Arvuti tulemus: {atäring}")
        # las nad panevad mõlevad all in poh kuigi juhend vist tahab et mingi kümne kaupa paneks vms aga noh nii on kiirem ja true to irl xd
        if ktäring > atäring:
            print(f"{kasutaja} võitis")
            arvuti -= raha
        elif ktäring < atäring:
            print("Arvuti võitis")
            raha -= arvuti
        else:
            print("viik")
        if raha == 0 or arvuti == 0:
            break
    print("mäng läbi")

täringud()



# 14. Palkade võrdlus - Loo palk.txt fail tÃ¶Ã¶tajate nime, soo ja palganumbriga.
# 	Koosta programm, mis analüüsib kas firmas toimub diskrimineerimist soo järgi. Selleks võrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kÃµige kÃµrgemat palka. Programm peab tegema otsuse.

        # Hubert Hunt m 2340
        # Siim Siil m 2570
        # MÃ¤rt MÃ¤ger m 1960
        # Vilma Vihmauss n 2060
        # Merike Metskits n 2250
        # Kati Karu n 2370
        # Elmar Elevant m 2900
        # Timoteus Tigu m 2850
        # Reet Rebane n 2340
        # Kalev Kaamel m 2570
        # Karmen Kass n 2120
        # Kornelius Koer m 2250

# tuleb välja et see UTF-8 on üli vajalik muidu üldse ei toimi
def palgad():
    fail = open("palk.txt", encoding="UTF-8")
    sisu = fail.read()
    fail.close()

    # see split \n on vaja selleks et saada listi iga rida eraldi yk
    read = sisu.split("\n")
    mees = []
    naine =[]
    # see split(" ") on vajalik selleks et saada listi iga sõna eraldi
    for rida in read:
        osad = rida.split(" ")
        # kontrollib rea algusest tühikuid ja kui peale kolmandat tühikut on m siis lisame mees listi kui n siis naine listi
        if osad[2] == "m":
            mees.append(int(osad[3]))
        else:
            naine.append(int(osad[3]))

    # arvutame meeste ja naiste keskmise palga
    mkeskmine = sum(mees)/len(mees)
    nkeskmine = sum(naine)/len(naine)

    # arvutame meeste ja naiste kõrgeima palga
    mkõrgeim = max(mees)
    nkõrgeim = max(naine)

    # kontrollime kas meeste keskmine on suurem kui naiste keskmine
    if mkeskmine > nkeskmine:
        print("Meeste keskmine palk on suurem ")
    else:
        print("Naiste keskmine palk on suurem ")

    # kontrollime kas meeste kõrgeim palk on suurem kui naiste kõrgeim palk
    if mkõrgeim > nkõrgeim:
        print("Meeste kõrgeim palk on suurem ")
    else:
        print("Naiste kõrgeim palk on suurem ")

palgad()


# 12. Eurokalkulaator
# 	Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
# 	Oluline on kasutada kahte funktsiooni!!

def euro():
    raha = int(input("Sisesta raha: "))
    print(f"{raha} eurot on {raha*15.64} krooni")

def kroon():
    raha = int(input("Sisesta raha: "))
    print(f"{raha} krooni on {raha/15.64} eurot")

def põhi():
    vali = input("Vali euro või kroon: ")
    if vali == "euro":
        euro()
    elif vali == "kroon":
        kroon()
    else:
        print("Vale valik")

põhi()

# 10. KaugushĆ¼pe
# 	kasutaja sisestab 3 kaugushĆ¼ppe tulemust - 1p
# 	sinu programm leiab ning vĆ¤ljastab parima ja keskmise tulemuse - 2p
# 	programmi dialoog kasutajaga on arusaadav ja Ć¼heselt mĆµistetav - 1p
# 	kood kommenteeritud - 1p

def kaugus():
    esimene = int(input("Sisesta esimene tulemus: "))
    teine = int(input("Sisesta teine tulemus: "))
    kolmas = int(input("Sisesta kolmas tulemus: "))
    parim = max(esimene, teine, kolmas)
    keskmine = (esimene + teine + kolmas)/3

    print(f"Parim tulemus: {parim}")
    print(f"Keskmine tulemus: {keskmine}")

kaugus()



# 8. Täringud
# 	kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# 	kasutaja võistleb kahe täringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p
import random


def täringud2():
    kasutaja = input("Sisesta nimi: ")
    raha = int(input("Sisesta raha: "))
    # ausalt võiks olla see arvuti raha random
    arvuti = 123 + random.randint(1,100)
    while raha > 0 and arvuti > 0:
        print(f"{kasutaja} raha: {raha}")
        print(f"Arvuti raha: {arvuti}")
        print(f"{kasutaja} viskab tärningu")
        # veits unfair no?
        ktäring = random.randint(1,6) + random.randint(1,6)
        print("Arvuti viskab tärningut")
        atäring = random.randint(1,6) 
        print(f"{kasutaja} tulemus: {ktäring}")
        print(f"Arvuti tulemus: {atäring}")
        # las nad panevad mõlevad all in poh kuigi juhend vist tahab et mingi kümne kaupa paneks vms aga noh nii on kiirem ja true to irl xd
        if ktäring > atäring:
            print(f"{kasutaja} võitis")
            arvuti -= raha
        elif ktäring < atäring:
            print("Arvuti võitis")
            raha -= arvuti
        else:
            print("viik")
        if raha == 0 or arvuti == 0:
            break
    print("mäng läbi")

täringud2()

# 6. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vĆµi paaritu
# 	kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu vĆµi pani nulli - 1p
# 	kood mis teavitab paaris vĆµi paaritust arvust - 1p
# 	kuvatakse programmi pealkiri - 1p
# 	kood kommenteeritud - 1p

def number():
    arv = int(input("sisesta arv: "))
    if arv == 0:
        print("arv on null")
    elif arv % 2 == 0:
        print("arv on paaris")
    else:
        print("arv on paaritu")

number()


# 4. List Less Than Ten
# 	Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
# 		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
# 	Write this in one line of Python. 1p
# 	Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 1p
	
def vk10():

    print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < 5])
    num = int(input("Sisesta number: "))
    print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < num])

vk10()


# 2. Vanused
# 	loo vanuste loend 1p
# 	leia numbrite suurim ja vĆ¤ikseim arv  1p
# 	kogusumma  1p
# 	keskmine 1p
def vanused():
    vanused = [10,34,12,54,12,34,45,83,46,76,4,7,94,56,26,8,4,83,87,35,76,3,22,43,6,2,26,34,25,28,24]

    väiksemArv = min(vanused)
    suurimArv = max(vanused)
    koguSumma =sum(vanused)
    keskmineArv = koguSumma/len(vanused)

    print(f"Väikseim arv on {väiksemArv}, suurim arv on {suurimArv}, kogusumma on {koguSumma} ja keskmine arv on {keskmineArv}.")

vanused()



