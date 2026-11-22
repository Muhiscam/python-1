# Monikko, jossa on vuodenaika kullekin kuukaudelle (tammikuu = indeksi 0, ..., joulukuu = indeksi 11)
vuodenajat = (
    "talvi",   # 1  tammikuu
    "talvi",   # 2  helmikuu
    "kevät",   # 3  maaliskuu
    "kevät",   # 4  huhtikuu
    "kevät",   # 5  toukokuu
    "kesä",    # 6  kesäkuu
    "kesä",    # 7  heinäkuu
    "kesä",    # 8  elokuu
    "syksy",   # 9  syyskuu
    "syksy",   # 10 lokakuu
    "syksy",   # 11 marraskuu
    "talvi",   # 12 joulukuu
)

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print(f"Kuukautta {kuukausi} vastaava vuodenaika on {vuodenajat[kuukausi - 1]}.")
else:
    print("Virheellinen kuukauden numero. Anna luku väliltä 1-12.")