#Tehvan marjapuu
#28.11.23




"""
Vanused
Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine

"""


vanused = [3,12,31,53,45,65,23,85,97,56,34]
print(f"kõige vanem:{max(vanused)} ja kõige noorem:{min(vanused)}")
print(f"vanuste summa:{sum(vanused)} ja vanuste keskmine:{round(sum(vanused)/len(vanused),2)}")

for vanus in vanused:
    print(vanus * "*") 









"""
Duplikaadid
Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.
opilased = [‘Juhan','Kati','Mario','Mario','Mati','Mati']
Loo kood, mis ei väljasta kordusi.

"""
"""
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
nimed = []

for opilane in opilased:
    if opilane not in nimed:
        nimed.append(opilane) 
print(nimed)

"""




"""
Õpilased
Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.

"""
"""
opilased = ['Juhan','Kati','Maarja','Mario','Mati']

nr = 1
for opilane in opilased:
    print(f"{nr}. {opilane}")
    nr=nr +1
valik = int(input("mitmendat nime soovid muuta:  "))
del opilased[valik -1]
uus_nimi = input("lisa uus või parandatud nimi:  ")
opilased.insert(valik-1, uus_nimi)

for opilane in opilased:
    print(opilane)
    
"""

"""
Nimede lisamine loendisse
    Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.
Õpilased

nimed =[]

for i in range(5):
    nimi = input("lisa nimi: ")
    nimed.append(nimi)
    


print(nimed)

"""






