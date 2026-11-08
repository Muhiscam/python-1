import random


def heita_noppa(tahkot):
    """Palauttaa satunnaisen silmäluvun väliltä 1-tahkot."""
    return random.randint(1, tahkot)


def main():
    maksimi = int(input("Anna nopan tahkojen lukumäärä: "))

    silmaluku = 0
    while silmaluku != maksimi:
        silmaluku = heita_noppa(maksimi)
        print(f"Heitto: {silmaluku}")


main()