# Tehvan Marjapuu
# 18.12.23

"""
Failis konto.txt on kirjas ujukomaarvudena pangakonto tehingud (kus positiivsed arvud on sissetulekud ja negatiivsed arvud on väljaminekud). Iga arv on eraldi real. Tekstifaili kasutamiseks programmi sees peab fail asuma programmifailiga samas kaustas.
Koostada programm, mis
loeb failist nimega konto.txt andmed;
väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud. Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord peab jääma samaks nagu failis. 
Näide programmi tööst:
Näiteks antud näitefaili konto.txt puhul peab ekraanile ilmuma

"""

fail = open("konto.txt", encoding="UTF-8")
for rida in fail:
    if float(rida) > 0:
        print(float(rida))
vastuvõetud = []





"""
Ülikooli I õppeastmesse (bakalaureuseõpe jm) võetakse igal aastal vastu sadu inimesi. Viimastel aastatel vastuvõetud inimeste arvud on aastate kaupa failis rebased.txt, kus esimesel real on 2011. aastal vastuvõetute arv, teisel real 2012. aastal vastuvõetute arv kuni viimasel real on 2019. aastal vastuvõetute arv. 
Koostada programm, mis
loeb failist registreeritud vastuvõetute andmed aastate järgi järjendisse;
Failist järjendisse saab lugeda järgmise programmijupi abil:
küsib kasutajalt aastat
võib eeldada, et sisestatakse täisarv, mis kuulub lõiku [2011; 2019].
väljastab, mitu inimest sel aastal vastu võeti.

"""

# fail = open("rebased.txt", encoding="UTF-8")

# vastuvõetud = []

# for rida in fail:
#     vastuvõetud.append(int(rida))
# print(vastuvõetud)


# aasta = 2011
# print(f"aastal {aasta} võeti vastu {vastuvõetud[aasta-2011]} õpilast")

# fail.close()
















