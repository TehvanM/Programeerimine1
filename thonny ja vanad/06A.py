#tehvan marjapuu
#5.12.23

fail = open("s6pru_l6ustaraamatus.txt", "r")

re=0
ke=0
erakonnad=[]


sisu =fail.readlines()
for tyyp in sisu:
    print(tyyp,end="")
    tyybike = tyyp.split(" ")
    print(tyybike[2])
    if tyybike[2] =="RE":   
        re+=1
    elif tyybike[2]=="KE":
        ke+=1
    if tyybike[2] not in erakonnad:
        erakonnad.append(tyybike[2])
    with open("poliitikud.txt", "a") as uusfail:
        uusfail.write(tyybike[0]+" "+tyybike[2]+"\n") 







print(f"reformikad:{re} ja keskud:{ke}")
print(f"erakondi kokku: {len(erakonnad)}")


