pituus = float(input("Anna kuhan pituus senttimetreinä: "))

alinsallittu = 37

if pituus < alinsallittu:
    puuttuu = alinsallittu - pituus
    print(f"Kuha on alamittainen. Laske se takaisin järveen.")
    print(f"Alimmasta sallitusta mitasta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on mitallinen, sen saa pitää.")