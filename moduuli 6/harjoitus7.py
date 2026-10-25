sanat = ["auto", "tietokone", "kissa", "ohjelmointi", "talo", "puhelin", "kukka", "kirjasto"]

lukumaara = 0

for sana in sanat:
    if len(sana) > 5:
        lukumaara += 1

print(f"Listassa on {lukumaara} sanaa, joissa on enemmän kuin 5 kirjainta.")