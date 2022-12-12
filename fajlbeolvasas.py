import random

# Forkold ezt a repositoryt és clone-ozd le!
# Olvasd be a teszt.txt tartalmát!
def beolvas(fajlnev):
    fh = open(fajlnev, "r", encoding="utf-8")
    tartalom = fh.read()
    fh.close()
    return tartalom


# Az egyes sorok tartalmát tárold rendre nevek, nemek és korok listában!
def tarol(tartalom, nevek, korok, nemek):
    sorok = tartalom.split("\n")
    i = 1
    while i < len(sorok):
        adatok = sorok[i].split(", ")
        nevek.append(adatok[0])
        nemek.append(adatok[1])
        korok.append(int(adatok[2]))
        i += 1


# Hány adat van rögzítve a fájlban?
def adatok_szama(tartalom):
    return len(tartalom.split("\n")) - 1


# Mekkora az emberek átlagos életkora?
def atlag_eletkor(korok):
    i = 0
    osszeg = 0
    if not len(korok):
        return 0  # átlagolásnál nullával osztanánk
    while i < len(korok):
        osszeg += korok[i]
        i += 1

    return osszeg / len(korok)


# Hány nő van a listában?
def nok_szama(nemek):
    i = 0
    db = 0
    while i < len(nemek):
        if nemek[i] == "nő":
            db += 1
        i += 1

    return db


# Hány éves a legfiatalabb nő?
def legfiatalabb_no_kora(nemek, korok):
    i = 0
    kor = 999
    while i < len(nemek):
        if nemek[i] == "nő" and korok[i] < kor:
            kor = korok[i]
        i += 1

    return kor


# Hozz létre egy új adatsort!
# Kérd be a felhasználótól a nevet!
# A nemet addig kérd be, amíg a "férfi" vagy a "nő" szöveget nem adja meg! Minden más válasz esetén kérd be újra a nem értékét! és a nemet.
# A kor értékének beállításához generálj egy véletlen számot 10 és 80 között!
# Az új adatsort csatold a meglévő fáj végére!
def uj_adat(fajlnev, nevek, nemek, korok):
    print("Új adatot rögzítünk.")
    nev = input("Adja meg a nevet: ")

    nem = ""
    while nem not in ["nő", "férfi"]:
        nem = input("Adja meg a nemet: ")
    kor = int(random.random() * 70) + 10

    nevek.append(nev)
    nemek.append(nem)
    korok.append(kor)

    fh = open("teszt.txt", "a", encoding="utf-8")
    fh.write(f"\n{nev}, {nem}, {kor}")
    fh.close()
