# Lottó számok listájának létrehozása
import random

KihuzottSzamok = []
lottoGomb = []
tipp = []
szam = 0
counter = 0
for i in range(0, 5):
    szam = int(input("Kérek 1 és 90 köté eső számot: "))
    tipp.append(szam)


for i in range (1, 91):
    lottoGomb.append(i)


random.shuffle(lottoGomb)

for i in range(0, 5):
    KihuzottSzamok.append(lottoGomb[i])


KihuzottSzamok.sort()
tipp.sort()

print("Az ön tippje: ", tipp)
print("A számok sorba rendezve: ", KihuzottSzamok)
