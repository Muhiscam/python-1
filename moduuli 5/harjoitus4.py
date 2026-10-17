kaupungit = []

for i in range(5):
    nimi = input(f"Anna kaupungin nimi ({i + 1}/5): ")
    kaupungit.append(nimi)

print("Syöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)