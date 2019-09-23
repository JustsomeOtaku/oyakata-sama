us= 0
os =1000

while os-us!= 1 or us-os !=-1:

    print("Ist ihre Zahl unter ",os,"? (Y/N)")
    Frage = input()

    if Frage == "y":
        os =os- ((os-us) // 2)
        print(us,os)

    else:
        us = os
        os += (os+us)//2
        print (us, os)



else:
    print("Ihre zahl war: ",us)

