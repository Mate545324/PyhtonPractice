

szám= int(input("kérem a kiinduló számot: "))
lépések = 0
while szám > 1:
    if szám % 2 == 0:
        szám= int (szám / 2)
        lépések = lépések + 1
        print(szám)
    else:
        szám = int (szám * 3 + 1)
        lépések = lépések + 1
        print(szám)

print("A lépések száma: ", lépések)
