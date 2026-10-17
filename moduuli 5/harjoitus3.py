luku = int(input("Anna kokonaisluku: "))

alkuluku = True

if luku < 2:
    alkuluku = False
else:
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            alkuluku = False
            break

if alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")