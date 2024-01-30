import random


kasutaja = input("Sisesta nimi: ")
raha = int(input("Sisesta raha: "))
arvuti = 123
while raha > 0 and arvuti > 0:
    print(f"Kasutaja raha:  {raha}")
    print(f"Arvuti raha:   {arvuti}")
    print("Kasutaja viskab tärningu")
    ktäring = random.randint(1,6) + random.randint(1,6)
    print("Arvuti viskab tärningut")
    atäring = random.randint(1,6) 
    print(f"Kasutaja tulemus:  {ktäring}")
    print(f"Arvuti tulemus:  {atäring}")
    if ktäring > atäring:
        print("Kasutaja võitis")
        arvuti -= raha
    elif ktäring < atäring:
        print("Arvuti võitis")
        raha -= arvuti
    else:
        print("Viik")
    if raha == 0 or arvuti == 0:
        break
print("Mäng läbi")