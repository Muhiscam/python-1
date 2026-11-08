def gallonat_litroiksi(gallonat):
    """Muuntaa Yhdysvaltain nestegallonat litroiksi."""
    return gallonat * 3.785


def main():
    gallonat = float(input("Anna bensiinin määrä gallonoina: "))

    while gallonat >= 0:
        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")
        gallonat = float(input("Anna bensiinin määrä gallonoina: "))

main()

