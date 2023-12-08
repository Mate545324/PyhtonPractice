alsóhatár = 0
felsőhatár = 0
összeg = 0

alsóhatár=int(input("Add meg a sorozat alsó határát: "))
felsőhatár=int(input("Add meg a sorozat felső határát: "))

while alsóhatár <= felsőhatár:
    összeg= összeg + alsóhatár
    alsóhatár= alsóhatár + 1


print("a sorozat tagjainak összege:", összeg)