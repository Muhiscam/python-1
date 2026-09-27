syote = input("Anna luku (tyhjä merkkijono lopettaa): ")

if syote != "":
    pienin = float(syote)
    suurin = float(syote)
    
    syote = input("Anna luku (tyhjä merkkijono lopettaa): ")
    
    while syote != "":
        luku = float(syote)
        
        if luku < pienin:
            pienin = luku
        
        if luku > suurin:
            suurin = luku
        
        syote = input("Anna luku (tyhjä merkkijono lopettaa): ")
    
    print(f"Pienin luku oli: {pienin}")
    print(f"Suurin luku oli: {suurin}")
else:
    print("Lukuja ei syötetty.")