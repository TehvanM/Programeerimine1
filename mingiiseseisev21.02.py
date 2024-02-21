#Tehvan Marjapuu
#21.02.24

# Raamatukogu laenutussĆ¼steemi arendamine

# EesmĆ¤rk: Luua Pythoni ja Tkinteri abil rakendus, mis haldab raamatukogu laenutustegevust. Rakendus vĆµimaldab kasutajatel sisestada, vaadata, muuta ja kustutada teavet laenutatud raamatute ja lugejate kohta. Iga laenutuse kohta genereeritakse sĆ¼steemi lisamisel unikaalne laenutus-ID.

# Funktsionaalsus:
# * Raamatute ja lugejate andmete sisestamine: Kasutajad saavad sisestada raamatute (pealkiri, autor, vĆ¤ljaandeaasta) ja lugejate (nimi, kontaktandmed) andmeid. Iga uue laenutuse puhul genereerib sĆ¼steem unikaalse laenutus-ID.
# * Laenutuste vaatamine: Rakendus kuvab kĆµik aktiivsed laenutused, sealhulgas raamatu pealkirja, autori, lugeja nime ja laenutusperioodi. Kasutajad saavad otsida laenutusi laenutus-ID, lugeja nime vĆµi raamatu pealkirja alusel.
# * Laenutuste muutmine ja kustutamine: Kasutajad saavad pikendada laenutusperioode, muuta lugeja kontaktandmeid vĆµi kustutada laenutusi sĆ¼steemist.
# * Andmete salvestamine: Andmed salvestatakse failisĆ¼steemi, kasutades CSV vĆµi TXT failivormingut, mis vĆµimaldab hĆµlpsat andmete haldamist ja taaskasutamist.

# NĆµuded:
# * Kasutajaliides tuleb luua Tkinteri abil, et pakkuda kasutajasĆµbralikku ja intuitiivset navigeerimist.
# * Rakendus peab tagama andmete jĆ¤rjepidevuse ja turvalisuse, kasutades failipĆµhist salvestusviisi.
# * Unikaalse laenutus-ID genereerimine peab tagama, et iga laenutus on selgelt identifitseeritav.
# * Rakendus peab vĆµimaldama raamatute ja lugejate andmete lihtsat sisestamist, muutmist ja kustutamist, samuti laenutusprotsessi haldamist.
# * Failid peavad olema kĆ¤ttesaadavad Githubis



import random
import csv
# Removed unused import statement
from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
import random
import csv


class Laenutus: # klass, mis loob laenutuse
    def __init__(self, laenutus_id, raamat, lugeja, laenutusperiood):
        self.laenutus_id = laenutus_id
        self.raamat = raamat
        self.lugeja = lugeja
        self.laenutusperiood = laenutusperiood

    def __str__(self):
        return f"{self.laenutus_id} - {self.raamat} - {self.lugeja} - {self.laenutusperiood}"

class Raamat: # klass, mis loob raamatu
    def __init__(self, pealkiri, autor, valjaandeaasta):
        self.pealkiri = pealkiri
        self.autor = autor
        self.valjaandeaasta = valjaandeaasta

    def __str__(self):
        return f"{self.pealkiri} - {self.autor} - {self.valjaandeaasta}"

class Lugeja: # klass, mis loob lugeja
    def __init__(self, nimi, kontaktandmed):
        self.nimi = nimi
        self.kontaktandmed = kontaktandmed

    def __str__(self):
        return f"{self.nimi} - {self.kontaktandmed}"

class Raamatukogu: # klass, mis loob raamatukogu
    def __init__(self):
        self.laenutused = []
        self.raamatud = []
        self.lugejad = []

    def lisa_raamat(self, raamat): # funktsioon, mis lisab raamatu
        self.raamatud.append(raamat)

    def lisa_lugeja(self, lugeja): # funktsioon, mis lisab lugeja
        self.lugejad.append(lugeja)

    def lisa_laenutus(self, laenutus): # funktsioon, mis lisab laenutuse
        self.laenutused.append(laenutus)

    def laenutuste_nimekiri(self): # funktsioon, mis näitab laenutuste nimekirja
        return self.laenutused

    def raamatute_nimekiri(self): # funktsioon, mis näitab raamatute nimekirja
        return self.raamatud

    def lugejate_nimekiri(self): # funktsioon, mis näitab lugejate nimekirja
        return self.lugejad

    def laenutus_id(self): # funktsioon, mis genereerib laenutus-ID
        return random.randint(1000, 9999)

    def laenutus_kustutamine(self, laenutus_id): # funktsioon, mis kustutab laenutuse
        for laenutus in self.laenutused:
            if laenutus.laenutus_id == laenutus_id:
                self.laenutused.remove(laenutus)
                return True
        return False

    def laenutus_pikendamine(self, laenutus_id, laenutusperiood): # funktsioon, mis pikendab laenutust
        for laenutus in self.laenutused:
            if laenutus.laenutus_id == laenutus_id:
                laenutus.laenutusperiood = laenutusperiood
                return True
        return False

    def lugeja_muutmine(self, nimi , kontaktandmed):
        for lugeja in self.lugejad:
            if lugeja.nimi == nimi:
                lugeja.kontaktandmed = kontaktandmed
                return True
        return False

    def laenutus_otsing(self, laenutus_id): # funktsioon, mis otsib laenutust
        for laenutus in self.laenutused:
            if laenutus.laenutus_id == laenutus_id:
                return laenutus
        return None

    def raamatu_otsing(self, pealkiri): # funktsioon, mis otsib raamatut
        for raamat in self.raamatud:
            if raamat.pealkiri == pealkiri:
                return raamat
        return None

    def lugeja_otsing(self, nimi): # funktsioon, mis otsib lugejat
        for lugeja in self.lugejad:
            if lugeja.nimi == nimi:
                return lugeja
        return None

    def salvesta_raamatud(self): # funktsioon, mis salvestab raamatud
        with open("raamatud.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for raamat in self.raamatud:
                writer.writerow([raamat.pealkiri, raamat.autor, raamat.valjaandeaasta])

    def salvesta_lugejad(self): # funktsioon, mis salvestab lugejad
        with open("lugejad.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for lugeja in self.lugejad:
                writer.writerow([lugeja.nimi, lugeja.kontaktandmed])

    def salvesta_laenutused(self): # funktsioon, mis salvestab laenutused
        with open("laenutused.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for laenutus in self.laenutused:
                writer.writerow([laenutus.laenutus_id, laenutus.raamat, laenutus.lugeja, laenutus.laenutusperiood])

    def lae_raamatud(self): # funktsioon, mis laeb raamatud
        with open("raamatud.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                raamat = Raamat(row[0], row[1], row[2])
                self.lisa_raamat(raamat)

    def lae_lugejad(self): # funktsioon, mis laeb lugejad
        with open("lugejad.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                lugeja = Lugeja(row[0], row[1])
                self.lisa_lugeja(lugeja)

    def lae_laenutused(self): # funktsioon, mis laeb laenutused
        with open("laenutused.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                laenutus = Laenutus(int(row[0]), row[1], row[2], row[3])
                self.lisa_laenutus(laenutus)

raamatukogu = Raamatukogu()

pealkiri_entry = None  # define pealkiri_entry here
autor_entry = None  # define autor_entry here
valjaandeaasta_entry = None  # define valjaandeaasta_entry here
nimi_entry = None  # define nimi_entry here
kontaktandmed_entry = None  # define kontaktandmed_entry here
raamat_entry = None  # define raamat_entry here
lugeja_entry = None  # define lugeja_entry here
laenutusperiood_entry = None  # define laenutusperiood_entry here
laenutus_listbox = None  # define laenutus_listbox here
raamat_listbox = None  # define raamat_listbox here
lugeja_listbox = None  # define lugeja_listbox here
laenutus_id_entry = None  # define laenutus_id_entry here

def raamatukogu_sulg(): # funktsioon, mis salvestab raamatukogu andmed
    raamatukogu.salvesta_raamatud()
    raamatukogu.salvesta_lugejad()
    raamatukogu.salvesta_laenutused()
    raamatukogu_sulg()

def raamatukogu_ava(): # funktsioon, mis avab raamatukogu
    raamatukogu_ava()

pealkiri_entry = None  # define pealkiri_entry here
def raamatukogu_lisa_raamat(): # funktsioon, mis lisab raamatu
    pealkiri = pealkiri_entry.get()
    autor = autor_entry.get()
    valjaandeaasta = valjaandeaasta_entry.get()
    raamat = Raamat(pealkiri, autor, valjaandeaasta)
    raamatukogu.lisa_raamat(raamat)
    raamatukogu.salvesta_raamatud()
    messagebox.showinfo("Raamatukogu", "Raamat lisatud")
    pealkiri_entry.delete(0, END)
    autor_entry.delete(0, END)
    valjaandeaasta_entry.delete(0, END)

def raamatukogu_lisa_lugeja(): # funktsioon, mis lisab lugeja
    nimi = nimi_entry.get()
    kontaktandmed = kontaktandmed_entry.get()
    lugeja = Lugeja(nimi, kontaktandmed)
    raamatukogu.lisa_lugeja(lugeja)
    raamatukogu.salvesta_lugejad()
    messagebox.showinfo("Raamatukogu", "Lugeja lisatud")
    nimi_entry.delete(0, END)
    kontaktandmed_entry.delete(0, END)

def raamatukogu_lisa_laenutus(): # funktsioon, mis lisab laenutuse
    raamat = raamat_entry.get()
    lugeja = lugeja_entry.get()
    laenutusperiood = laenutusperiood_entry.get()
    laenutus_id = raamatukogu.laenutus_id()
    laenutus = Laenutus(laenutus_id, raamat, lugeja, laenutusperiood)
    raamatukogu.lisa_laenutus(laenutus)
    raamatukogu.salvesta_laenutused()
    messagebox.showinfo("Raamatukogu", "Laenutus lisatud")
    raamat_entry.delete(0, END)
    lugeja_entry.delete(0, END)
    laenutusperiood_entry.delete(0, END)

def raamatukogu_laenutuste_nimekiri(): # funktsioon, mis näitab laenutuste nimekirja
    laenutused = raamatukogu.laenutuste_nimekiri()
    for laenutus in laenutused:
        pass
        laenutus_listbox.insert(END, laenutus)

def raamatukogu_raamatute_nimekiri(): # funktsioon, mis näitab raamatute nimekirja
    raamatud = raamatukogu.raamatute_nimekiri()
    for raamat in raamatud:
        raamat_listbox.insert(END, raamat)

def raamatukogu_lugejate_nimekiri(): # funktsioon, mis näitab lugejate nimekirja
    lugejad = raamatukogu.lugejate_nimekiri()
    for lugeja in lugejad:
        lugeja_listbox.insert(END, lugeja)

def raamatukogu_laenutus_kustutamine(): # funktsioon, mis kustutab laenutuse
    laenutus_id = int(laenutus_id_entry.get())
    if raamatukogu.laenutus_kustutamine(laenutus_id):
        messagebox.showinfo("Raamatukogu", "Laenutus kustutatud")
    else:
        messagebox.showinfo("Raamatukogu", "Laenutust ei leitud")
    laenutus_id_entry.delete(0, END)

def raamatukogu_laenutus_pikendamine(): # funktsioon, mis pikendab laenutust
    laenutus_id = int(laenutus_id_entry.get())
    laenutusperiood = laenutusperiood_entry.get()
    if raamatukogu.laenutus_pikendamine(laenutus_id, laenutusperiood):
        messagebox.showinfo("Raamatukogu", "Laenutus pikendatud")
    else:
        messagebox.showinfo("Raamatukogu", "Laenutust ei leitud")
    laenutus_id_entry.delete(0, END)
    laenutusperiood_entry.delete(0, END)

def raamatukogu_lugeja_muutmine(): # funktsioon, mis muudab lugeja kontaktandmeid
    nimi = nimi_entry.get()
    kontaktandmed = kontaktandmed_entry.get()
    if raamatukogu.lugeja_muutmine(nimi, kontaktandmed):
        messagebox.showinfo("Raamatukogu", "Lugeja kontaktandmed muudetud")
    else:
        messagebox.showinfo("Raamatukogu", "Lugejat ei leitud")
    nimi_entry.delete(0, END)
    kontaktandmed_entry.delete(0, END)

def raamatukogu_laenutus_otsing(): # funktsioon, mis otsib laenutust
    laenutus_id = int(laenutus_id_entry.get())
    laenutus = raamatukogu.laenutus_otsing(laenutus_id)
    if laenutus:
        laenutus_listbox.insert(END, laenutus)
    else:
        messagebox.showinfo("Raamatukogu", "Laenutust ei leitud")
    laenutus_id_entry.delete(0, END)

def raamatukogu_raamatu_otsing(): # funktsioon, mis otsib raamatut
    pealkiri = pealkiri_entry.get()
    raamat = raamatukogu.raamatu_otsing(pealkiri)
    if raamat:
        raamat_listbox.insert(END, raamat)
    else:
        messagebox.showinfo("Raamatukogu", "Raamatut ei leitud")
    pealkiri_entry.delete(0, END)

def raamatukogu_lugeja_otsing(): # funktsioon, mis otsib lugejat
    nimi = nimi_entry.get()
    lugeja = raamatukogu.lugeja_otsing(nimi)
    if lugeja:
        lugeja_listbox.insert(END, lugeja)
    else:
        messagebox.showinfo("Raamatukogu", "Lugejat ei leitud")
    nimi_entry.delete(0, END)

raamatukogu_ava() # avab raamatukogu

raamatukogu_sulg() # salvestab raamatukogu andmed

raamatukogu_lisa_raamat() # lisab raamatu

raamatukogu_lisa_lugeja() # lisab lugeja

raamatukogu_lisa_laenutus() # lisab laenutuse

raamatukogu_laenutuste_nimekiri() # näitab laenutuste nimekirja

raamatukogu_raamatute_nimekiri() # näitab raamatute nimekirja

raamatukogu_lugejate_nimekiri() # näitab lugejate nimekirja

raamatukogu_laenutus_kustutamine() # kustutab laenutuse

raamatukogu_laenutus_pikendamine() # pikendab laenutust

raamatukogu_lugeja_muutmine() # muudab lugeja kontaktandmeid

raamatukogu_laenutus_otsing() # otsib laenutust

raamatukogu_raamatu_otsing() # otsib raamatut

raamatukogu_lugeja_otsing() # otsib lugejat

# GUI
