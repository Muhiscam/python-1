tarina = ""
sana = input("Anna sana lisättäväksi tarinaan: ")

while sana != "loppu":
    tarina = tarina + sana + " "
    sana = input("Anna sana lisättäväksi tarinaan: ")

print(tarina.strip())