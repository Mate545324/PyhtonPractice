alsóhatár = 0
felsőhatár = 0
összeg = 0

alsóhatár=int(input("Add meg a sorozat alsó határát: "))
felsőhatár=int(input("Add meg a sorozat felső határát: "))
számosság =felsőhatár - alsóhatár + 1

összeg = ((alsóhatár+felsőhatár)*számosság) / 2
print("a sorozat összege:", összeg)