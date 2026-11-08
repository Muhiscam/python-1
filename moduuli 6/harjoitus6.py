import math


def yksikkohinta(halkaisija_cm, hinta):
    """Palauttaa pizzan yksikköhinnan (€/m²)."""
    sade_m = (halkaisija_cm / 100) / 2
    ala_m2 = math.pi * sade_m ** 2
    return hinta / ala_m2


def main():
    halkaisija1 = float(input("Anna 1. pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna 1. pizzan hinta (€): "))
    halkaisija2 = float(input("Anna 2. pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna 2. pizzan hinta (€): "))

    yksikkohinta1 = yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = yksikkohinta(halkaisija2, hinta2)

    print(f"1. pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²")
    print(f"2. pizzan yksikköhinta: {yksikkohinta2:.2f} €/m²")

    if yksikkohinta1 < yksikkohinta2:
        print("1. pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("2. pizza antaa paremman vastineen rahalle.")
    else:
        print("Pizzat antavat saman vastineen rahalle.")


main()