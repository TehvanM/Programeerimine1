
#tehvan Marjapuu
#18.12.23
"""
1.1. Tervitus
Koostada programm, mis väljastaks ekraanile teksti Tere, maailm! täpselt sellisel kujul - koma ja hüüumärgiga.
"""
def tervita():
    print("Tere, Maailm!")
"""
1.2. Aasta liblikas
Koostada programm, mille
1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks "teelehe-mosaiikliblikas" (sõnena);
3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks ". aasta liblikas on " (sõnena);
4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta, lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni, mis teisendab arvu sõneks);
5. real väljastatakse muutuja lause väärtus ekraanile.
"""
def liblikas():
    aasta = 2020
    liblikas = "teelehe-mosaiikliblikas"
    lause_keskosa = ".aasta liblikas on "
    lause = str(aasta) + lause_keskosa + liblikas
    print(lause)

"""
1.3. Pilved
Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi pilvedeks. Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel, alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis
küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
Kasutaja peab saama sisestada pilvede kõrgust nii täisarvuna kui ka ujukomaarvuna, nt 7.5.
"""

def pilved(alus):
    if alus > 6:
        print("need on ülemised pilved")
    else:
        print("need ei ole ülemised pilved")



""""
1.4. Bussid
Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid on vähemalt üks. Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi kohtade arvu (just sellises järjekorras) ning väljastab ekraanile, mitu bussi on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).
Võib-olla on abi nendest tehetest
// täisarvuline jagamine, 36 // 10 → 3
% jäägi leidmine 36 % 10 → 6
Testige oma programmi muuhulgas järgmiste algandmetega:
inimeste arv: 60, kohtade arv: 40;
inimeste arv: 80, kohtade arv: 40;
inimeste arv: 20, kohtade arv: 40;
inimeste arv: 40, kohtade arv: 40.
Püüdke ka mõista, miks just sellised testandmed valiti.
"""

def bussid(i, k):
    bussid = i % k
    if i == k:
        bussid= i // k
        viimased = i
    elif bussid >0:
        bussid = i // k + 1
        viimased= i % k
    else:
        bussid = i // k
        viimased= i % k
    print(f"busse vaja:{bussid}. \nViimases bussis: {viimased} inimest")
    

# tervita()
# liblikad()
# alus = float(input(f" sisesta pilvede kõrgus kilomeetrites: "))
# pilved(alus)
inimesed =int(input("inimeste arv: "))
kohti_bussis = int(input("kohtade arv bussis: "))
bussid(inimesed, kohti_bussis)

