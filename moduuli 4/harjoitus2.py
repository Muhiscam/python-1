tuumaa = float(input("Anna tuumien määrä (negatiivinen luku lopettaa ohjelman): "))

while tuumaa >= 0:
    senttia = tuumaa * 2.54
    print(f"{tuumaa} tuumaa on {senttia:.2f} senttimetriä.")
    tuumaa = float(input("Anna tuumien määrä (negatiivinen luku lopettaa ohjelman): "))

print("Ohjelma lopetetaan.")