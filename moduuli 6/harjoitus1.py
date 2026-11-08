import random


def heita_noppa():
    """Palauttaa satunnaisen silmäluvun väliltä 1-6."""
    return random.randint(1, 6)


def main():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppa()
        print(f"Heitto: {silmaluku}")

main()

