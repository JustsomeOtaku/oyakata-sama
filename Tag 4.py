Zahl = []
try:
    while Zahl != str:
        Zahl.append(int(input("Geben sie eine Zahl")))
        print(Zahl)
except:
    print("Die Größte Zahl ist:", max(Zahl),"Die kleinste Zahl ist: ",min(Zahl),"Der durchschnitt beträgt",sum(Zahl)/len(Zahl) )
    Zahl.sort()
    print("Sotiert lautet die Liste:",Zahl)