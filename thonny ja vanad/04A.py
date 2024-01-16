"""
Tehvan Marjapuu
21.11.23
ÜL 4
"""
import random
#loto

for i in range(5):
    print(random.randint(0, 9), end=" ")



print ()
print ()
print ()
#teistpidi kolmnurk

k = 5
for i in range(6):
    print("* " * k)
    k = k -1 


#kolmnurk
k = 5
for i in range(1,k+1):
    print("* " * i)

print()





#5*5 tärnid
ruut = 5
for i in range(ruut):
    print("* " * ruut) 








sugu = "m"
vanus = 16

if sugu == "m" :
    if vanus>=16 and vanus<=18:
        print("pääseb meeskonda")
    else:
        print("vanus ei sobi")
else:
    print("tahan noori poisse")
    
"""
Jalgpalli meeskond
Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita.
"""

sugu = input("sisesta oma sugu: ")
if sugu == 'mees':
    vanus = int(input("sisesta oma vanus: "))
    if 16 <= vanus <= 18:
        print("sa saad kanditeerida")
    else:
        print("sa ei saa kandideerida")
else:
    print("ainult mehed saavad kandideerida")
    

"""
Müük
Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
Kuva toote lõplik hind. Plokkskeemi pole vaja!
"""
hind = int(input("sisesta hind:  "))
al1 = 0.1
al2 = 0.2
if hind <= 10:
    al = hind-hind*al1
else:
    al = hind-hind*al2
print(f"soodus hind on {al}")




"""
Juubel
Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
Plokkskeemi pole vaja!
"""
a = 154
if a % 5 == 0:
    v = "on"
else:
    v = "ei ole"
print(f"vanus: {a} {v} juubel")





"""
Matemaatika
Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""
arv1 = int(input("sisesta esimene arv: "))
arv2 = int(input("sisesta teine arv: "))
tehe = input("vali tehe (+-*/): ")
if tehe == "+":
    vastus = arv1+arv2
elif tehe == "-":
    vastus = arv1-arv2    
elif tehe == "*":
    vastus = arv1*arv2
elif tehe == "/":
    vastus = round(arv1/arv2, 2)
else:
    vastus:"Tehet ei saa teha"

print(f"{arv1} {tehe} {arv2} = {vastus}")




"""
Ruut
Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""

arv1 = input("sisesta külg 1: ")
arv2 = input("sisesta külg 2: ")
if arv1 == arv2:
    print("võimalik et saab ruudu")
else:
    print("Nii ei saa ruutu teha")
