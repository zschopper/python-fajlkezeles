import fajlbeolvasas

nevek = []
nemek = []
korok = []
tartalom = fajlbeolvasas.beolvas("teszt.txt")
print("2. feladat:", fajlbeolvasas.tarol(tartalom, nevek, korok, nemek))
print("3. feladat:", fajlbeolvasas.adatok_szama(tartalom))
print("4. feladat:", fajlbeolvasas.atlag_eletkor(korok))
print("5. feladat:", fajlbeolvasas.nok_szama(nemek))
print("6. feladat:", fajlbeolvasas.legfiatalabb_no_kora(nemek, korok))

print("nevek: ", nevek)
print("nemek: ", nemek)
print("korok: ", korok)

fajlbeolvasas.uj_adat("teszt.txt", nevek, nemek, korok)
