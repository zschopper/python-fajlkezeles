"""
Véletlen számok - kockadobás
A feladat leadása github-on keresztül történik, github linket kérek!

Projekt neve: Sajat_nev_kockadobás

1.) Készíts egy kockadobas listát, amiben 10 (teszteléshez, majd 1000) kockadobás eredményét tárolod.
2.) Töltsd fel adatokkal!
3.) Készíts függvényt, ami visszaadja, hogy hányszor dobtuk a paraméterében megadott számot!
4.) Készíts egy metódust, amely kiír a képernyőre annyi csillagot, ahányszor dobták a paraméterében kapott számot.
5.) Készíts metódust, ami megjeleníti a képernyőn egy sávdiagram formájában a kockadobások eredményét:
  1: **********
  2: ********
  3: *****************
  4: ********************
  5: ************
  6: ********************

6.) Volt-e olyan eset, hogy kétszer egymás után ugyanazt a számot dobtuk?
7.) Mekkora volt a leghosszabb ilyen sorozat? Melyik számot dobtuk ekkor?  - nehéz
8.) Készíts "cinkelt" kockát! 6-ost kétszer akkora nagyobb valószínűséggel dobjon, mint bármelyik más számot!
9.) Jelentítsd meg ehhez a dobókockéhoz tartozó statisztikát is!
10.) Alakítsd át úgy az eddig megírt függvényeket, hoyg most is használhatsd őket!

"""

from random import random

# 1. feladat
# 2. feladat
# 8. feladat: cinkelt kocka
def dobas(dobasok, db=10, cinkelt=False):
    i = 0
    while i < db:
        if not cinkelt:
            szam = int(random() * 6) + 1
        else:
            szam = int(random() * 12) + 1
            if szam > 6:
                szam = 6
        i += 1

        dobasok.append(szam)
    pass


# 3. feladat
def szam_keresese(dobasok, szam):
    db = 0
    i = 0
    while i < len(dobasok):
        if dobasok[i] == szam:
            db += 1
        i += 1
    return db


# 4. feladat
def csillag(dobasok, szam):
    db = szam_keresese(dobasok, szam)
    print(f"{szam}: {'*' * db}")


# 5. feladat
def savdiagramm(dobasok):
    szam = 1
    while szam <= 6:
        csillag(dobasok, szam)
        szam += 1


# 6. feladat
def ugyanaz_ketszer(dobasok):
    i = 1
    while i < len(dobasok) and dobasok[i - 1] != dobasok[i]:
        i += 1
    if i < len(dobasok):
        print(
            f"Az első ismétlődő dobás a(z) {i} és a {i + 1}. dobás volt. A {dobasok[i]}. számot dobták kétszer."
        )
    else:
        print("Nem volt ismétlődő dobás.")


# 7. feladat
def sorozat_keres(dobasok):
    sor_szam = []  # ebben tároljuk, hogy melyik számot figyeljük
    sor_hossz = []  # ebben tároljuk, hogy milyen hosszú volt a sorozat
    sor_futo = []  # ebben tároljuk, hogy az adott sorozat még fut-e (bool típusú)


    i = 0
    while i < len(dobasok):
        dobott_szam = dobasok[i]
        j = 0

        # karbantartjuk a futó sorozatkereséseket:
        futo_szamok = []
        while j < len(sor_szam):
            if sor_futo[j]:
                futo_szamok.append(sor_szam[j])
                if sor_szam[j] == dobott_szam:  # ha jó a szám, növeljük a sorozat hosszát
                    sor_hossz[j] += 1
                else:  # ha nem jó a szám: lezárjuk, többet nem nézzük, hogy nő-e a sorozat hossza
                    sor_futo[j] = False

            j += 1
        # ha nincs a futó számok között a dobott szám, hozzáadjuk a számot 1 hosszal
        if dobott_szam not in futo_szamok:
            sor_szam.append(dobott_szam)
            sor_hossz.append(1)
            sor_futo.append(True)

        i += 1
    # kész a listánk, megkeressük a leghosszabbat

    max_idx = 0

    i = 1

    while i < len(sor_hossz):
        if sor_hossz[max_idx] < sor_hossz[i]:
            max_idx = i
        i += 1

    print(f"A leghosszabb sorozat {sor_hossz[max_idx]} dobás hosszú volt, a(z) {sor_szam[max_idx]}-es számokat dobták.")


# 10. feladat
def statisztikak(dobasok):
    szam = 1
    while szam <= 6:
        db = szam_keresese(dobasok, szam)
        if db > 0:
            print(f"A(z) {szam} számot {db} alkalommal dobták.")
        else:
            print(f"A(z) {szam} számot egy alkalommal se dobták.")
        szam += 1

    savdiagramm(dobasok)
    ugyanaz_ketszer(dobasok)
    sorozat_keres(dobasok)


dobas_szam = 100

dobasok = []
dobas(dobasok, dobas_szam)
print(dobasok)
statisztikak(dobasok)

# kiürítjük a dobás listát, cinkelten dobunk
print("** Cinkelt kockás dobások **")

dobasok = []
dobas(dobasok, dobas_szam, True)
print(dobasok)
statisztikak(dobasok)
