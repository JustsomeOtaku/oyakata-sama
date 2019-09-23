Z = int(input("Nennen sie ein Positive Ganze Zahl"))
x = 1
y = 1
B = 1
while x<Z :
    x= x+1
    y = x+y
    B = B+ (x * x)
print(y, B)