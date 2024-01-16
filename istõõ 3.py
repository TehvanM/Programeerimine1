#Tehvan Marjapuu
#10.01.2024


import random

failinimi = input("Palun sisestage faili nimi: ")
fail = open(f"C:\\Users\\tmarjapuu\\Desktop\\drive-download-20240110T085328Z-001\\{failinimi}", encoding="utf-8")

nr = 1
for rida in fail:
    print(f"{nr}, {rida}", end="")
    nr += 1

fail.seek(0)
nr = 1
jrk = int(input("\nValige laulu järjekorranumber: "))
for rida in fail:
    if nr == jrk:
        print(f"Mängitav muusika pala on: {rida}")
    nr += 1

fail.close()


