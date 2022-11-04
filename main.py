import SGA

if __name__ == '__main__':
    pr_krzyz = 60
    pr_mut = 5
    l_os = 30
    l_pop = int(150/l_os)
    statistical_try = list()
    for i in range(40):
        Generator = SGA.SGA(11, 1, 6, l_os, pr_krzyz, pr_mut)
        populacja = Generator.wylosuj_pierwsza_populacje()
        for i in range(l_pop):
            wartosci_funkcji_celu = Generator.sprawdzenie_funkcji_celu(populacja)
            czy_ujemne = Generator.sprawdzenie_ujemnych(wartosci_funkcji_celu)
            if czy_ujemne != False:
                for key in wartosci_funkcji_celu.keys():
                    wartosci_funkcji_celu[key] = wartosci_funkcji_celu[key] + (czy_ujemne * (-1))
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
        statistical_try.append(best_osobnik)
    print(sum(statistical_try)/len(statistical_try))