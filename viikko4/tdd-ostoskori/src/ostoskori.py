from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        summa = 0
        for ostos in self._ostokset:
            summa += ostos._lukumaara

        return summa
            

        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self._ostokset:
            summa += ostos.hinta()
        return summa

        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._ostokset:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return
        uusi_tuote = Ostos(lisattava)
        self._ostokset.append(uusi_tuote)

    def poista_tuote(self, poistettava: Tuote):
       poistettava = Ostos(poistettava)
       for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == poistettava.tuotteen_nimi():
                    if ostos._lukumaara == 1:
                        self._ostokset.remove(ostos)
                    else:
                        ostos._lukumaara -= 1

    def tyhjenna(self):
        self._ostokset = []

    def ostokset(self):
        return self._ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
