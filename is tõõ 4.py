#Tehvan Marjapuu
# 10.01.24
# iseseisev tõõ 4

import random
import datetime 






fail = open("myndid.txt")












#-------------------------------------------------------------------------------------------------------
"""





def tervitus(jrk):
    print('võõrustaja: "tere!"')
    print(f"täna {jrk}. Kord tervitada, mõtliskeb võõrustaja.")
    print("külaline: tere, suur tänu kutse eest!")

kylastajate_arv = int(input("mittu inimest on kutsutud?: "))
for i in range(kylastajate_arv):
    tervitus(i+1)

"""
#-------------------------------------------------------------------------------------------------------
"""
def eelarv(arv):
    kogusumma = arv  * 10 + 55
    return kogusumma 

tegelik_arv = int(input("mittu kutsutud?: "))
kylastajate_arv = int(input("mittu inimest on kutsutud?: "))
print(f"MAX eelarve: {eelarve(tegelik_arv))}")
print(f"MIN eelarve: {eelarve(kylastajate_arv))}")

"""
#-------------------------------------------------------------------------------------------------------

"""

def mahlapakkide_arv(kg):
    pakkide_arv = round(kg * 0.4 / 3)
    return pakkide_arv

õunade_kogus = float(input("Sisesta õunade arv: "))
print(mahlapakkide_arv(õunade_kogus))
"""
#-------------------------------------------------------------------------------------------------------
"""


def banner(l):
    print(l.upper())


korduvarv = int(input("mitu korda soovid?: "))
tekst = input("lisatext: ")

for i in range(korduvarv):
    banner(tekst)


"""
#-------------------------------------------------------------------------------------------------------


