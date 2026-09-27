oikea_tunnus = "kayttaja1"
oikea_salasana = "salainen123"

yritykset = 0
kirjautunut = False

while yritykset < 5 and not kirjautunut:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        kirjautunut = True
    else:
        yritykset += 1

if kirjautunut:
    print("Tervetuloa")
else:
    print("Pääsy evätty")