lépések = 0
határérték = int(input("Kérem a határértéket:  "))
leghossabbSzvekvencia= -1
leghossabbSzvekvenciaszam = -1
vizsgaltszam = 0
legmagasabbszam = 0
maximumvizsgaltszam = 0
szam = 0

for szamlalo in range (2, határérték):
    szam = szamlalo
    vizsgaltszam = szam
    while szam > 1:
        if szam % 2 == 0:
            szam = int(szam / 2)
            lépések = lépések + 1
        else:
            szam = int (szam * 3 + 1)
            lépések = lépések + 1
        if lépések > leghossabbSzvekvencia:
            leghossabbSzvekvencia = lépések
            leghossabbSzvekvenciaszam = vizsgaltszam
            print("Új leghosszabb szekvenciát találtam: ", leghossabbSzvekvencia, "A vizsgált szám: ", leghossabbSzvekvenciaszam)
        if szam > legmagasabbszam:
            legmagasabbszam = szam
            maximumvizsgaltszam = vizsgaltszam
            print("Új legmaggasabb számot találtam: ", legmagasabbszam, "A vizsgált szám: ", maximumvizsgaltszam)
    lépések = 0
print ("A leghosszabb szekvencia: ", leghossabbSzvekvencia, "a hozzá tartozó szám: ", leghossabbSzvekvenciaszam)
print ("A legmagasabb szám: ", legmagasabbszam, "A hozzá tartozó kiinduló szám", maximumvizsgaltszam)
