NameundJahr = {"Benjamin" : 2000}

def Update():
    Key = 0
    Value = 0
    while Key != "" :
        Person = input("Geben sie einen Namen und ein Geburtsjahr ein: ")
        Key , Value = Person.split(" ")
        if Key != "":
           try:
               NameundJahr[Key] = int(Value)
           except:
               Error(Key)

def Error(Key):
        Value = 0
        try:
            Value = int(input("bitte geben sie ein richtiges Geburtsdatum ein"))
            NameundJahr[Key] = int(Value)

        except:
            Error(Key)



try:
    if __name__ == '__main__':
        Update()
        print(NameundJahr)

except(ValueError):
    Error()