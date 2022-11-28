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

    def hinta(self):
        summa = 0
        for ostos in self._ostokset:
            summa += ostos.hinta()
        return summa

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
