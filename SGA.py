import random


class SGA:
    def __init__(self,a,b,c,ile_os,pr_krzyz,pr_mut):
        self.a = a
        self.b = b
        self.c = c
        self.ile_os = ile_os
        self.pr_krzyz = pr_krzyz/100
        self.pr_mut = pr_mut/100

    def funkcja_celu(self,x) -> int:
        return (self.a*x*x) + (self.b*x) + self.c

    def wylosuj_pierwsza_populacje(self) -> list:
        populacja = list()
        for i in range(self.ile_os):
            populacja.append(random.randrange(0,255))
        return populacja

    def sprawdzenie_funkcji_celu(self,populacja: list) -> dict:
        wartosci_funkcji_celu = dict()
        for item in populacja:
            wartosci_funkcji_celu[item] = self.funkcja_celu(item)

        return wartosci_funkcji_celu

    def sprawdzenie_ujemnych(self, wartosci_funkcji_celu: dict):
        if min(wartosci_funkcji_celu.values()) < 0:
            return min(wartosci_funkcji_celu.values())
        else:
            return False

    @staticmethod
    def wyliczenie_wkladu(wartosci_funkcji_celu: dict):
        suma_funkcji = 0
        for key in wartosci_funkcji_celu.keys():
            suma_funkcji += wartosci_funkcji_celu[key]

        if suma_funkcji == 0:
            suma_funkcji += 1

        for key in wartosci_funkcji_celu.keys():
            wartosci_funkcji_celu[key] = wartosci_funkcji_celu[key]/suma_funkcji

        return {k: v for k,v in sorted(wartosci_funkcji_celu.items(), key=lambda item:item[1])}

    def selekcja(self,wklady_w_funkcje_celu: dict) -> list:
        values = list()
        print(len(wklady_w_funkcje_celu))
        for index,value in enumerate(wklady_w_funkcje_celu.keys()):
            values.append(wklady_w_funkcje_celu[value])
            if index-1 > -1:
                wklady_w_funkcje_celu[value] = wklady_w_funkcje_celu[value] + values[index-1]
                values[index] = wklady_w_funkcje_celu[value]
=========== HERE ========
        nowa_populacja = list()
        for i in range(self.ile_os):
            losowa_liczba = random.random()
            for key in wklady_w_funkcje_celu.keys():
                if losowa_liczba < wklady_w_funkcje_celu[key]:
                    nowa_populacja.append(key)
                    break

        return nowa_populacja

    def mutacja(self, popuacja: list) -> list:
        new_populacja = []
        for osobnik in popuacja:
            osobnik_binary = lambda x, n :format(x,'b').zfill(n)
            new_osobnik = []
            for sign in [*osobnik_binary(osobnik,8)]:
                mutacja = random.random()
                if mutacja <= self.pr_mut:
                    if sign == '0':
                        new_osobnik.append('1')
                    else:
                        new_osobnik.append('0')
                else:
                    new_osobnik.append(sign)
            new_populacja.append(int(''.join(new_osobnik),2))
        return new_populacja

    @staticmethod
    def dobranie_pary(populacja: list) -> list:
        pary = []
        cnt = 0
        while len(populacja) > 0:
            if len(populacja) == 1:
                pary.append([populacja[0]])
                populacja.remove(populacja[0])
                break
            pierwszy = random.randrange(0,len(populacja),1)
            drugi = random.randrange(0,len(populacja),1)
            while pierwszy == drugi:
                pierwszy = random.randrange(0,len(populacja),1)
            pary.append([populacja[pierwszy],populacja[drugi]])
            pierwszy = populacja[pierwszy]
            drugi = populacja[drugi]
            populacja.remove(pierwszy)
            populacja.remove(drugi)
            cnt += 1
        return pary

    def krzyzowanie(self, pary:list) -> list:
        populacja = []
        osobnik_binary = lambda x, n: format(x, 'b').zfill(n)
        for para in pary:
            para_bin = []
            if len(para) == 1:
                populacja.append(para[0])
                continue
            krzyzowanie = random.random()
            if krzyzowanie <= self.pr_krzyz:
                for osobnik in para:
                    para_bin.append([*osobnik_binary(osobnik,8)])
                miejsce_krzyz = random.randrange(1,len(para_bin[0]))
                populacja.append(int(''.join(para_bin[0][:miejsce_krzyz]+para_bin[1][miejsce_krzyz:]),2))
                populacja.append(int(''.join(para_bin[1][:miejsce_krzyz]+para_bin[0][miejsce_krzyz:]),2))
            else:
                for osobnik in para:
                    populacja.append(osobnik)
        return populacja





