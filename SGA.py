import random


class SGA:
    def __init__(self,a,b,c,ile_wyn,lb_pop,ile_os,pr_krzyz,pr_mut):
        self.a = a
        self.b = b
        self.c = c
        self.ile_wyn = ile_wyn
        self.lb_pop = lb_pop
        self.ile_os = ile_os
        self.pr_krzyz = pr_krzyz
        self.pr_mut = pr_mut

    def __funkcja_celu(self,x) -> int:
        return (self.a*x*x) + (self.b*x) + self.c

    def wylosuj_pierwsza_populacje(self) -> list:
        populacja = list()
        for i in range(self.ile_os):
            populacja.append(random.randrange(0,255))

        return populacja

    def sprawdzenie_funkcji_celu(self,populacja) -> dict:
        wartosci_funkcji_celu = dict()
        for item in populacja:
            wartosci_funkcji_celu[item] = self.__funkcja_celu(item)

        return wartosci_funkcji_celu

    @staticmethod
    def wyliczenie_wkladu(wartosci_funkcji_celu: dict):
        suma_funkcji = 0
        for key in wartosci_funkcji_celu.keys():
            suma_funkcji += wartosci_funkcji_celu[key]

        for key in wartosci_funkcji_celu.keys():
            wartosci_funkcji_celu[key] = wartosci_funkcji_celu[key]/suma_funkcji

        return {k: v for k,v in sorted(wartosci_funkcji_celu.items(), key=lambda item:item[1])}

    def selekcja(self,wklady_w_funkcje_celu: dict) -> list:
        values = list()
        for index,value in enumerate(wklady_w_funkcje_celu.keys()):
            values.append(wklady_w_funkcje_celu[value])
            if index-1 > -1:
                wklady_w_funkcje_celu[value] = wklady_w_funkcje_celu[value] + values[index-1]
                values[index] = wklady_w_funkcje_celu[value]

        nowa_populacja = list()
        for i in range(self.ile_os):
            losowa_liczba = random.random()
            for key in wklady_w_funkcje_celu.keys():
                if losowa_liczba < wklady_w_funkcje_celu[key]:
                    nowa_populacja.append(key)
                    break

        return nowa_populacja