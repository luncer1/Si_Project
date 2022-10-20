import SGA

if __name__ == '__main__':
    Generator = SGA.SGA(4, 7, 2, 40, 15, 10, 80, 3)

    populacja = Generator.wylosuj_pierwsza_populacje()
    for i in range(100):
        print(populacja," przed")
        wartosci_funkcji_celu = Generator.sprawdzenie_funkcji_celu(populacja)
        wartosci_wkladu = Generator.wyliczenie_wkladu(wartosci_funkcji_celu)
        populacja = Generator.selekcja(wartosci_wkladu)
        print(populacja, "po")
