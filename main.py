import SGA

if __name__ == '__main__':

    for i in range(40):
        Generator = SGA.SGA(-1, 1, 0, 9, 70, 1)
        populacja = Generator.wylosuj_pierwsza_populacje()
        for i in range(15):
          #  print(populacja,sum(populacja)/len(populacja)," przed")
            wartosci_funkcji_celu = Generator.sprawdzenie_funkcji_celu(populacja)
            czy_ujemne = Generator.sprawdzenie_ujemnych(wartosci_funkcji_celu)
            if czy_ujemne:
                for key in wartosci_funkcji_celu.keys():
                    wartosci_funkcji_celu[key] = wartosci_funkcji_celu[key] + (czy_ujemne * (-1) + 2)

            wartosci_wkladu = Generator.wyliczenie_wkladu(wartosci_funkcji_celu)
            print("wartosci wkladu",wartosci_wkladu)
            populacja = Generator.selekcja(wartosci_wkladu)
            print("populacja - po selekcji: ", populacja)
            populacja = Generator.mutacja(populacja)
            print("populacja - po mutacji: ", populacja)
            pary = Generator.dobranie_pary(populacja)
            print("populacja - po parach: ", pary)
            populacja = Generator.krzyzowanie(pary)
            print("populacja - koniec: ", populacja)
        ostatnie_pokolenie = Generator.sprawdzenie_funkcji_celu(populacja)
        best_osobnik = list(ostatnie_pokolenie.keys())[0]
        for key in ostatnie_pokolenie.keys():
            if ostatnie_pokolenie[key] > Generator.funkcja_celu(best_osobnik):
                best_osobnik = key
        print("best osobnik",best_osobnik)
        results = open("results.txt", 'a')
        results.write(f"{Generator.funkcja_celu(best_osobnik)} {best_osobnik}\n")