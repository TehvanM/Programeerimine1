#Tehvan Marjapuu
# 16.01.24
# Iseseisev

# 12. Eurokalkulaator
# 	Koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
# 	Oluline on kasutada kahte funktsiooni!!




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





