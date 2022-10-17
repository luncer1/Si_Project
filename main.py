import SGA

if __name__ == '__main__':
    Generator = SGA.SGA(4, 7, 2, 40, 15, 10, 80, 3)

    asd = Generator.wyliczenie_wkladu(Generator.sprawdzenie_funkcji_celu(Generator.wylosuj_pierwsza_populacje()))
    print(asd)
    print(Generator.selekcja(asd))