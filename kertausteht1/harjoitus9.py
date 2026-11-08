tuotteet = []
maarat = []

jatka = "Kyllä"

while jatka == "Kyllä":
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatka = input("Jatketaanko tuotantoa? ")

print("Tuotanto lopetettu!")
print("Valmistetut tuotteet:")

for i in range(len(tuotteet)):
    print(f"{tuotteet[i]}: {maarat[i]} kpl")