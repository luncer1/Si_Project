import SGA

if __name__ == '__main__':
    Generator = SGA.SGA(4, 7, 2, 40, 15, 10, 80, 3)

    populacja = Generator.wylosuj_pierwsza_populacje()
    for i in range(40):
        print(populacja," przed")
        wartosci_funkcji_celu = Generator.sprawdzenie_funkcji_celu(populacja)
        wartosci_wkladu = Generator.wyliczenie_wkladu(wartosci_funkcji_celu)
        populacja = Generator.selekcja(wartosci_wkladu)
        populacja = Generator.mutacja(populacja)
        pary = Generator.dobranie_pary(populacja)
        populacja = Generator.krzyzowanie(pary)
        print(populacja, "po")
    print(max(populacja))
    print(Generator.funkcja_celu(max(populacja)))
    results = open("results.txt", 'a')
    results.write(f"f({max(populacja)}) = {Generator.funkcja_celu(max(populacja))}\n")