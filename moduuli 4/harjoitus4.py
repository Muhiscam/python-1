import random

arvottu_luku = random.randint(1, 10)
arvaus = int(input("Arvaa luku väliltä 1-10: "))

while arvaus != arvottu_luku:
    if arvaus > arvottu_luku:
        print("Liian suuri arvaus")
    else:
        print("Liian pieni arvaus")
    
    arvaus = int(input("Arvaa luku väliltä 1-10: "))

print("Oikein")