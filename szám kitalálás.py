import random
tipp = 0
gondoltszam =random.randint(1,100)

tipp = int(input("Gondoltam egy számra, tippled meg: "))

while tipp != gondoltszam:
    if tipp < gondoltszam:
        print("A gondolt szám nagyobb")
        tipp = int(input("Próbáld újra: "))
    elif tipp > gondoltszam:
        print("A gondolt szám kisebb.")
        tipp = int(input("Még egyszer: "))
print("Nyertél, kitaláltad a számot!")
    