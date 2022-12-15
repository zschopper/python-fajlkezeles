# Fájlkezelés pythonban

## Fájl megnyitása: 
open(fajlnev,mod, kodolas)

### mód
„r”	read – alapértelmezett érték olvasásra nyitja meg a fájlt és hibaüzenetet kapunk, ha a fájl nem létezik
„a”	append- a fájlhoz hozzáfűzhetünk értékeket. létrehozzza a fájlt, ha nem létezik még. 
„w”	write – megnyitja a fájlt írásra/olvasásra, létrehozza, ha még nem létezik
„x”	create – létrehozza a fájlt, hibaüzenetet kapunk, ha már létezik

fajlom = open(fajlnev, "r", encoding='utf-8')
fajltartalom_szovegesen = print(f.read()) – kiolvassa a fájl tartalmát
kovetkezo_sor = print(f.readline()) – kiolvassa a fájl következő tejes sorát
sorok_lista = print(f.readlines()) – kiolvassa a fájl összes sorát és soronként beleteszi egy listába. 

## Használat után zárjuk le a fájlt!
fajlom.close()

## Sorok feldolgozása
A listába tett sorokat egy ciklussal járhatjuk be. 
Minden sor végéről a nem kívánatos enter jelet el kell távolítani: aktsor.strip()
Minden sort a szeparátor (,) mentén fel kell osztani: aktsor.split(',') => ennek eredménye egy lista, amiben az elemek vannak
A lista elemeit rendre tároljuk el a nevek, nemek és korok listákban!

# Feladat

 - Forkold ezt a repositoryt és clone-ozd le!
 - Olvasd be a teszt.txt tartalmát!
 - Az egyes sorok tartalmát tárold rendre nevek, nemek és korok listában!
 - Hány adat van rögzítve a fájlban? 
 - Mekkora az emberek átlagos életkora? 
 - Hány nő van alistában? 
 - Hány éves a legfiatalabb nő? 
 - Hozz étre egy új adatsort! 
    - Kérd be a felahsználótól a nevet!
    - A nemet addig kérd be, amíg a "férfi" vagy a "nő" szöveget nem adja meg! Minden más válasz esetén kérd be újra a nem értékét! és a nemet. 
    - A kor értékének beállításához generálj egy véletlen számot 10 és 80 között!
  - Az új adatsort csatold a meglévő fáj végére!
  

