
from cmath import sqrt

luku = int(input("Anna kokonaisluku: "))

while luku != 0:
    if luku < 0:
        print("Virheellinen numero")
    else:
        print(sqrt(luku))
    luku = int(input("Anna kokonaisluku: "))

print("Kiitos, ohjelma päättyy.")