import random

lkm = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0
for i in range(lkm):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print(f"Silmälukujen summa on {summa}.")