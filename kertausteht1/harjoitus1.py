tuntipalkka = float(input("Anna tuntipalkka (€/h): "))


tunnit = float(input("Anna tehdyt tunnit: "))

paiva = input("Anna viikonpäivä: ").strip().lower()

if paiva == "sunnuntai":
    palkka = 2 * tuntipalkka * tunnit
else:
    palkka = tuntipalkka * tunnit

print(f"Päiväpalkka on {palkka:.2f} €")