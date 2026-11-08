luvut = []
luku = int(input("Anna luku (0 lopettaa): "))

while luku != 0:
    luvut.append(luku)
    print("Lisäysjärjestyksessä:", luvut)
    print("Järjestettynä:", sorted(luvut))
    luku = int(input("Anna luku (0 lopettaa): "))

print("Ohjelma päättyy.")