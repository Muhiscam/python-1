def laske_summa(luvut):
    """Palauttaa listassa olevien kokonaislukujen summan."""
    summa = 0
    for luku in luvut:
        summa += luku
    return summa


def main():
    luvut = [4, 8, 15, 16, 23, 42]
    tulos = laske_summa(luvut)
    print(f"Lista: {luvut}")
    print(f"Lukujen summa on {tulos}.")


main()