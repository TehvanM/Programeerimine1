#Tehvan Marjapuu
# 16.01.24
# Iseseisev

# 16. TÃ¤ringud
# 	Kasutaja vÃµistleb kahe tÃ¤ringuga arvuti vastu. Kasutaja teeb pakkumise ning suurima tÃ¤ringupunktisumma vÃµitja saab laual oleva raha endale juurde. MÃ¤ng kestab kuni kummalgi on raha otsas.
# 	(Vihjed: kÃ¼si kasutajalt nime, kuva pidevalt konto seisu ja tÃ¤ringuviskeid, kasutajate raha hulga mÃ¤ngu alguses mÃ¤Ã¤rad sina)

import random
kasutaja = input("Sisesta kasutajanimi: ")
raha = int(input("Sisesta raha: "))
arvuti = 100
while raha > 0 and arvuti > 0:
    print("Kasutaja raha: " + str(raha))
    print("Arvuti raha: " + str(arvuti))
    print("Kasutaja viskab tärningut.")
    kasutajaTäring = random.randint(1,6) + random.randint(1,6)
    print("Arvuti viskab tärningut.")
    arvutiTäring = random.randint(1,6) + random.randint(1,6)
    print("Kasutaja tulemus: " + str(kasutajaTäring))
    print("Arvuti tulemus: " + str(arvutiTäring))
    if kasutajaTäring > arvutiTäring:
        print("Kasutaja võitis.")
        raha = raha + 10
        arvuti = arvuti - 10
    elif kasutajaTäring < arvutiTäring:
        print("Arvuti võitis.")
        raha = raha - 10
        arvuti = arvuti + 10
    else:
        print("Viik.")
print("Mäng läbi.")






# 14. Palkade vÃµrdlus - Loo palk.txt fail tÃ¶Ã¶tajate nime, soo ja palganumbriga (10 tÃ¶Ã¶tajat).
# 	Koosta programm, mis analÃ¼Ã¼sib kas firmas toimub diskrimineerimist soo jÃ¤rgi. Selleks vÃµrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kÃµige kÃµrgemat palka. Programm peab tegema otsuse.

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



with open("palk.txt", "r") as file:
    sisu = file.read()
    file.close()

sisu = sisu.split("\n")
mees = []
naine = []
for i in sisu:
    i = i.split(" ")
    if i [2] == "m":
        mees.append(i[3])
    else:
        naine.append(i[3])

mees = [int(i) for i in mees]
naine = [int(i) for i in naine]

meesKeskmine = sum(mees)/len(mees)
naineKeskmine = sum(naine)/len(naine)

meesSuurim = max(mees)
naineSuurim = max(naine)

if meesKeskmine > naineKeskmine:
    print("Meeste keskmine palk on suurem.")
else:
    print("Naiste keskmine palk on suurem.")

if meesSuurim > naineSuurim:
    print("Meeste suurim palk on suurem.")
else:
    print("Naiste suurim palk on suurem.")



# 12. Eurokalkulaator
# 	Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
# 	Oluline on kasutada kahte funktsiooni!!

def eureek(eur):
    return eur*15.6466

def eekeur(eek):
    return eek/15.6466 

print("EUR EEK või EEK EUR") 
valik = input("Sisesta valik: ")
if valik == "EUR EEK":
    eur = int(input("Sisesta EUR: "))
    print(str(eur) + " EUR on " + str(eureek(eur)) + " EEK.")
elif valik == "EEK EUR":
    eek = int(input("Sisesta EEK: "))
    print(str(eek) + " EEK on " + str(eekeur(eek)) + " EUR.")
else:
    print("Vale valik.")




# 10. KaugushĆ¼pe
# 	kasutaja sisestab 3 kaugushĆ¼ppe tulemust - 1p
# 	sinu programm leiab ning vĆ¤ljastab parima ja keskmise tulemuse - 2p
# 	programmi dialoog kasutajaga on arusaadav ja Ć¼heselt mĆµistetav - 1p
# 	kood kommenteeritud - 1p

for i in range(3):
    tulemus = int(input("Sisesta tulemus: "))
    if i == 0:
        parim = tulemus
        keskmine = tulemus
    else:
        if tulemus > parim:
            parim = tulemus
        keskmine = keskmine + tulemus

print("Parim tulemus: " + str(parim))
print("Keskmine tulemus: " + str(keskmine/3))




# 8. Täringud
# 	kuvatakse korrektne arusaadav kĆ¼simus ja hiljem vastus - 1p
# 	kasutaja vĆµistleb kahe tĆ¤ringuga arvuti vastu - 1p
# 	kasutaja teeb pakkumise ning suurima tĆ¤ringupunktisumma vĆµitja saab laual oleva raha endale - 2p
# 	kood kommenteeritud - 1p

import random
Panus = int(input("Sisesta panus: "))

kasutaja = random.randint(1,6) + random.randint(1, 6)
arvuti = random.randint(1,6)
print("Kasutaja tulemus: " + str(kasutaja))
print("arvuti tulemus: " + str(arvuti))

if kasutaja > arvuti:
    print("Kasutaja võitis " + str(Panus) + " eurot.")
elif kasutaja < arvuti:
    print("Arvuti võitis " + str(Panus) + " eurot.")
else:
    print("Viik.")



# 6. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vĆµi paaritu
# 	kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
# 	eelnev kontroll, kas kasutaja ei lisanud arvu vĆµi pani nulli - 1p
# 	kood mis teavitab paaris vĆµi paaritust arvust - 1p
# 	kuvatakse programmi pealkiri - 1p
# 	kood kommenteeritud - 1p

arv1 = int(input("sisesta number: "))
if arv1 % 2 == 0:
    print("arv on paariga.")
else:
    print("arv on paaritu.")


# 4. List Less Than Ten
# 	Take a list and write a program that prints out all the elements of the list that are less than 5. 1p
# 		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. 1p
# 	Write this in one line of Python. 1p
# 	Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user. 1p
	

print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < 5])
num = int(input("Sisesta number: "))
print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < num])



# 2. Vanused
# 	loo vanuste loend 1p
# 	leia numbrite suurim ja vĆ¤ikseim arv  1p
# 	kogusumma  1p
# 	keskmine 1p




vanused = [10,34,12,54,12,34,45,83,46,76,4,7,94,56,26,8,4,83,87,35,76,3,22,43,6,2,26,34,25,28,24]

väiksemArv = min(vanused)
suurimArv = max(vanused)
koguSumma =sum(vanused)
keskmineArv = koguSumma/len(vanused)

kõik = dir() 
  # saadud https://www.geeksforgeeks.org/viewing-all-defined-variables-in-python/
for i in kõik: 
    if not i.startswith('__'): 
        myvalue = eval(i) 
        print(i , myvalue) 





