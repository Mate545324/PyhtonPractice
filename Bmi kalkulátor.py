Tömeg = float(input("Mekkora a tömeged kilogrammban?"))
Magasság = float(input("Mekkora a magasságod centiméterben?"))
Méter = Magasság/100
BMI = Tömeg/(Méter*Méter)

if BMI <= 18.5:
    print("Ön alultáplált",BMI)
elif 18.5 <= BMI < 24.9:
    print("Ön iddeális.",BMI)
elif 25<= BMI <29.9:
    print("Ön túlsúlyos",BMI)
elif 30 <=BMI <34.9:
    print ("Ön elhízott.", BMI)
elif 34.9<= BMI <39.9:
    print ("Ön súlyosan elhízott.", BMI)
elif BMI >= 39.9:
    print ("Ön morbidan elhízott.", BMI)

