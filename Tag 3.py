try:
    Zahl = int(input("Geben sie eine Zahl ein."))
    a = Zahl
    b = Zahl
    Summe = 0
    while Zahl >= 0:

        Summe = Summe + Zahl
        Zahl = int(input("Geben sie noch eine Zahl ein.  "))
        if a < Zahl:
            a = Zahl
        if b < Zahl and Zahl < a:
            b = Zahl
    print("Alle Zahlen addiert ergeben:  " , Summe , "Die Größete Zahl ist:  ", a,"Die Zweit größte Zahl ist:  ", b, "Die Summe der Zwei größten Zahlen ist:", a+b )

except(ValueError):
    print("Keine Zahl")

