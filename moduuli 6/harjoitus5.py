def karsi_parittomat(luvut):
    """Palauttaa uuden listan, jossa on vain parilliset luvut."""
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


def main():
    alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3, -4, 0]
    karsittu = karsi_parittomat(alkuperainen)
    print(f"Alkuperäinen lista: {alkuperainen}")
    print(f"Karsittu lista: {karsittu}")


main()