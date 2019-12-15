
def nogavice(s):
    brez_para = []
    for e in s:
        if e in brez_para:
            brez_para.remove(e)
        else:
            brez_para.append(e)
    return brez_para
'''
Ker smo moški, vemo, barvno slepi, obenem pa v družini z ženo in n otroki ni mogoče, da bi imel vsak same enake nogavice, se lahko znajdemo tako, da na vsako nogavico prišijemo številko. Enake nogavice imajo enako številko; ker imamo več enakih nogavic, ima lahko več nogavic enako številko.

Recimo, da iz pralnega stroja potegnemo nogavice s številkami [1, 2, 3, 2, 3, 1, 3, 1, 1, 1, 1]. Imamo torej tri pare nogavic 1, en par nogavic 2 in en par nogavic 3 in (eh, spet!) še eno 3 brez para.

Napiši funkcijo nogavice(s), ki prejme seznam številk nogavic in vrne seznam vseh številk nogavic brez para. V gornjem primeru torej vrne [3].

Vrstni red elementov v seznamu naj bo enak vrstnemu redu zadnjih pojavitev teh številk; za [1, 1, 4, 1, 3, 1] vrne [4, 3] in ne [3, 4].

Rešitev
S številkami ravnajmo enako, kot bi z nogavicami. Zlagajmo jih na mizo (oziroma v nov seznam). Za vsako novo nogavico najprej pogledamo, ali je ena taka že na mizi. Če je, jo odstranimo. Če ni, jo dodamo.
'''

def bingo(listki, vrstni_red):
    izklicano = set()
    for stevilka in vrstni_red:
        izklicano.add(stevilka)
        for listek in listki:
            if set(listek) <= izklicano:
                return listek
'''
Igra Bingo poteka tako, da ima vsak igralec listek z nekaj številkami. Voditelj žreba številke. Če se izžrebana številka nahaja na igralčevem listku, jo ta prečrta. Zmaga igralec, ki prvi prečrta vse številke.

Vedeževalka nam je napovedala vrstni red, v katerem bodo žrebane številke. Imamo seznam listkov za Bingo; izbrali bi radi tistega, na katerem bodo prej prečrtane se številke.

Napiši funkcijo bingo(listki, vrstni_red), ki prejme listke (seznam seznamov številk) in vrne listek, na katerem bodo najprej prečrtane vse številke.

bingo([[4, 1, 2, 3, 5], [6, 1, 2, 3, 4], [7, 6, 4, 3, 2]],
    [4, 2, 8, 3, 1, 6, 5, 7])
vrne [6, 1, 2, 3, 4] (saj bo ta očitno prehitel prvega in zadnjega, zaradi 5 in 7).

Funkcija naj ne spreminja podanega seznama!
'''

def selitve(zacetek, navodila, kraj):
    lokacije = {kraj: {prebivalec} for kraj, prebivalec in zacetek}
    for vrstica in open(navodila):
        _, odkod, _, kam, _ = vrstica.split('"')
        lokacije[kam] |= lokacije[odkod]
        lokacije[odkod] = set()
    return lokacije[kraj]
'''
Napiši funkcijo selitve(zacetek, datoteka_selitev, kraj), ki prejme začetno razdelitev oseb, ime datoteke s selitvami in ime nekega kraja. Vrniti mora množico imen oseb, ki po podanih selitvah živijo v podanem kraju.

Začetna razdelitev oseb po krajih je lahko, recimo, [("Ljubljana", "Jana"), ("Šentvid", "Vid"), ("Mala Polana", "Ana"), ("Maribor", "Bor"), ("Kamnik", "Nik"), ("Ozeljan", "Jan"), ("Županje Njive", "Ive"), ("Koroška Bela", "Ela"))]. Vedno le po ena oseba v vsakem mestu.

Argument datoteka_selitev pove ime datoteke z vsebino, ki je lahko, recimo, taka

Najprej grejo iz "Mala Polana" v "Šentvid".
Iz "Kamnik" pa tudi v "Šentvid".
Pa še iz "Koroška Bela" odidejo v "Ozeljan".
Potem pa iz "Šentvid" v "Maribor" (kwa?!).
Vsaka vrstica torej vsebuje dve imeni krajev, zapisani v dvojnih narekovajih. V vrstici ni drugih dvojnih narekovajev. Vedno se preselijo vsi prebivalci podanega kraja.

Če je gornje začetno stanje shranjeno v seznamu zacetek, one štiri vrstice pa v datoteki selitve.txt, mora klic selitve(zacetek, "selitve.txt", "Maribor") vrniti {"Ana", "Vid", Nik", "Bor"}, klic selitve(zacetek, "selitve.txt", "Šentvid") pa vrne prazno množico (saj so šli Šentvidčani v Maribor).

Pri reševanju si lahko - ni pa nujno - pomagaš s tem, kar boš sprogramiral(a) v peti nalogi.
'''

def brez_para(stevilka, nogavice):
    if not nogavice:
        return False
    if nogavice[0] == stevilka:
        return not brez_para(stevilka, nogavice[1:])
    else:
        return brez_para(stevilka, nogavice[1:])
'''
Napiši rekurzivno funkcijo brez_para(nogavica, nogavice), ki prejme številko nogavice in podoben seznam kot prva naloga. Vrniti mora True, če je nogavica brez para, in False, če ni.

Klic brez_para(39, [41, 39, 39, 41, 41, 39, 39]) vrne False in klic brez_para(41, [41, 39, 39, 41, 41, 39, 39]) vrne True, saj imamo eno 41 brez para.

Rešitev
Če je seznam nogavic prazen, podana nogavica ni brez para in vrnemo False. Sicer preverimo, ali je prva nogavica enaka podani. Če je, bo brez para, če v ostanku seznama ta nogavica ni brez para. Sicer pa prvi element ignoriramo in gledamo ostanek seznama.
'''

class Sledilnik:
    def __init__(self, zacetek):
        self.osebe = {prebivalec: kraj for kraj, prebivalec in zacetek}
        self.n_selitev = 0

    def kje_zivi(self, oseba):
        return self.osebe[oseba]

    def prebivalci(self, kraj):
        return {oseba for oseba, kje in self.osebe.items() if kje == kraj}

    def preseli(self, oseba, kraj):
        self.osebe[oseba] = kraj
        self.n_selitev += 1

    def preseli_vse(self, odkod, kam):
        for oseba in self.prebivalci(odkod):
            self.preseli(oseba, kam)

    def selitev(self):
        return self.n_selitev
'''
Napiši razred Sledilnik, katerega konstruktor prejme začetno razdelitev po krajih v takšni obliki, kot smo jo imeli tudi v tretji nalogi. Te podatke si shrani v poljubni obliki, ki sem vam zdi primerna. Če vam pride prav (ni pa nujno, da vam bo), lahko predpostavite, da so imena unikatna, torej, da ni dveh oseb z enakim imenom.

Razred ima naslednje metode:

kje_zivi(self, oseba) vrne kraj, v katerem trenutno živi podana oseba;
prebivalci(self, kraj) vrne množico prebivalcev podanega kraja;
preseli(self, oseba, kraj) preseli podano osebo v podani kraj;
preseli_vse(self, odkod, kam) preseli vse prebivalce kraja odkod v kraj kam;
selitev(self) vrne število vseh selitev. Če se oseba seli v kraj, v katerem že živi, se to šteje za selitev. Če se iz nekega kraja preselijo tri osebe v drug kraj, so to tri selitve.
Rešitev
Ves trik je v tem, da si pametno shranimo podatke. In pri tej nalogi se to da storiti na precej načinov. Tule bomo naredili slovar, katerega ključi so osebe (saj vemo, da nimamo dveh oseb z istim imenom), vrednosti pa kraji, v katerih živijo. Vse ostalo je potem rutinsko.
'''





import unittest

class Test01Nogavice(unittest.TestCase):
    def test_nogavice(self):
        self.assertEqual(nogavice([1, 2, 3, 2, 3, 1, 3, 1, 1, 1, 1]), [3])
        self.assertEqual(nogavice([1, 2, 3, 2, 3, 3, 4, 1]), [3, 4])
        self.assertEqual(nogavice([1, 4, 2, 3, 2, 3, 3, 1]), [4, 3])
        self.assertEqual(nogavice([1, 1, 4, 1, 3, 1]), [4, 3])
        self.assertEqual(nogavice([1, 4, 2, 3, 2, 3, 3, 4, 3, 1]), [])
        self.assertEqual(nogavice([100, 512, 1]), [100, 512, 1])
        self.assertEqual(nogavice([]), [])
        self.assertEqual(nogavice([123]), [123])

        n = [1, 2, 3, 2]
        self.assertEqual(nogavice(n), [1, 3])
        self.assertEqual(n, [1, 2, 3, 2])


class Test02Bingo(unittest.TestCase):
    def test_bingo(self):
        listki = [[4, 1, 2, 3, 5], [6, 1, 2, 3, 4], [7, 6, 4, 3, 2]]
        self.assertEqual(bingo(listki, [1, 2, 3, 4, 5, 6, 7]), [4, 1, 2, 3, 5])
        self.assertEqual(bingo(listki, [1, 2, 3, 4, 6, 7, 5]), [6, 1, 2, 3, 4])
        self.assertEqual(bingo(listki, [1, 6, 2, 3, 4, 5, 7]), [6, 1, 2, 3, 4])
        self.assertEqual(bingo(listki, [2, 3, 4, 6, 1, 7, 5]), [6, 1, 2, 3, 4])
        self.assertEqual(bingo(listki, [2, 3, 4, 5, 1, 7, 6]), [4, 1, 2, 3, 5])
        self.assertEqual(bingo(listki, [2, 3, 4, 5, 1, 6, 7]), [4, 1, 2, 3, 5])
        self.assertEqual(bingo(listki, [2, 3, 4, 1, 5, 6, 7]), [4, 1, 2, 3, 5])
        self.assertEqual(bingo(listki, [2, 3, 4, 6, 7, 5, 1]), [7, 6, 4, 3, 2])

        self.assertEqual(bingo(listki, [8, 2, 3, 4, 6, 7]), [7, 6, 4, 3, 2])


class Test03Selitve(unittest.TestCase):
    def setUp(self):
        from random import randint
        self.fname = "f{}".format(randint(10000, 99999))

    def tearDown(self):
        import os
        try:
            os.remove(self.fname)
        except:
            pass

    def test_selitve(self):
        zacetek = [
            ("Ljubljana", "Jana"), ("Šentvid", "Vid"), ("Šempeter", "Peter"),
            ("Maribor", "Bor"), ("Kamnik", "Nik"), ("Libanja", "Anja"),
            ("Županje Njive", "Ive"), ("Koroška Bela", "Ela"),
            ("Jablan", "Lan"), ("Krtina", "Tina"), ("Lepa njiva", "Iva"),
            ("Mala Polana", "Ana"), ("Mojstrana", "Ana"), ("Ozeljan", "Jan"),
            ("Slatina", "Tina"), ("Stomaž", "Tomaž"), ("Šentjanž", "Anže"),
            ("Begunje", "Lan"), ("Odranci", "Ajda"), ("Polževo", "Tim"),
            ("Lozice", "France")]
        fname = self.fname

        with open(fname, "w") as f:
            f.write("""iz "Ljubljana" v "Šentvid"
iz "Šentvid" pa v "Kamnik"
""")
        self.assertEqual(selitve(zacetek, fname, "Kamnik"), {"Jana", "Vid", "Nik"})
        self.assertEqual(selitve(zacetek, fname, "Ljubljana"), set())
        self.assertEqual(selitve(zacetek, fname, "Ozeljan"), {"Jan"})
        self.assertEqual(selitve(zacetek, fname, "Mojstrana"), {"Ana"})

        with open(fname, "w") as f:
            f.write("""iz "Mala Polana" v "Šentvid"
in iz "Kamnik" v "Šentvid"
""")
        self.assertEqual(selitve(zacetek, fname, "Šentvid"), {"Ana", "Vid", "Nik"})
        self.assertEqual(selitve(zacetek, fname, "Ozeljan"), {"Jan"})

        with open(fname, "w") as f:
            f.write("""Najprej grejo iz "Mala Polana" v "Šentvid".
            Iz "Kamnik" pa tudi v "Šentvid".
            Pa še iz "Koroška Bela" odidejo v "Ozeljan".
            Potem pa iz "Šentvid" v "Maribor" (kwa?!).
""")
        self.assertEqual(selitve(zacetek, fname, "Maribor"), {"Ana", "Vid", "Nik", "Bor"})
        self.assertEqual(selitve(zacetek, fname, "Šentvid"), set())

        with open(fname, "w") as f:
            f.write("""najprej iz "Mala Polana" grejo v "Šentvid"
iz "Kamnik" pa tudi v "Šentvid"
""")
        self.assertEqual(selitve(zacetek, fname, "Šentvid"), {"Ana", "Vid", "Nik"})
        self.assertEqual(selitve(zacetek, fname, "Ozeljan"), {"Jan"})

        with open(fname, "w") as f:
            f.write('''iz "Ljubljana" v "Begunje"
iz "Šentvid" v "Kamnik"
iz "Mojstrana" v "Begunje"
iz "Kamnik" v "Koroška Bela"
iz "Begunje" v "Polževo"''')

        self.assertEqual(selitve(zacetek, fname, "Ljubljana"), set())
        self.assertEqual(selitve(zacetek, fname, "Begunje"), set())
        self.assertEqual(selitve(zacetek, fname, "Šentvid"), set())
        self.assertEqual(selitve(zacetek, fname, "Kamnik"), set())
        self.assertEqual(selitve(zacetek, fname, "Koroška Bela"), {"Vid", "Nik", "Ela"})
        self.assertEqual(selitve(zacetek, fname, "Mojstrana"), set())
        self.assertEqual(selitve(zacetek, fname, "Begunje"), set())
        self.assertEqual(selitve(zacetek, fname, "Polževo"), {"Jana", "Ana", "Tim", "Lan"})
        self.assertEqual(selitve(zacetek, fname, "Mala Polana"), {"Ana"})

        with open(fname, "w") as f:
            f.write('''iz "Ljubljana" v "Begunje"
iz "Kamnik" v "Ljubljana"
''')
        self.assertEqual(selitve(zacetek, fname, "Ljubljana"), {"Nik"})
        self.assertEqual(selitve(zacetek, fname, "Begunje"), {"Lan", "Jana"})
        self.assertEqual(selitve(zacetek, fname, "Kamnik"), set())


class Test04BrezPara(unittest.TestCase):
    def test_brez_para(self):
        class Nogavice(list):
            def __getitem__(self, i):
                if not isinstance(i, int) or i == 0:
                    return super().__getitem__(i)
                else:
                    raise IndexError(
                        "Dostopajte le do prvega elementa ali do ostanka")

            def __iter__(self):
                raise ValueError("Brez zanke for, prosim. Hvala.")

        self.assertFalse(brez_para(39, Nogavice([41, 39, 39, 41, 41, 39, 39])))
        self.assertTrue(brez_para(41, Nogavice([41, 39, 39, 41, 41, 39, 39])))
        self.assertTrue(brez_para(1, Nogavice([1, 2, 3, 4, 2, 3, 4])))
        self.assertTrue(brez_para(2, Nogavice([1, 2, 3, 4, 1, 3, 4])))
        self.assertTrue(brez_para(3, Nogavice([1, 2, 4, 1, 2, 3, 4])))
        self.assertTrue(brez_para(4, Nogavice([1, 2, 4, 1, 2, 3])))


class Test05Sledilnik(unittest.TestCase):
    def test_sledilnik(self):
        zacetek = [
            ("Ljubljana", "Jana"), ("Šentvid", "Vid"), ("Šempeter", "Peter"),
            ("Maribor", "Bor"), ("Kamnik", "Nik"), ("Libanja", "Anja"),
            ("Županje Njive", "Ive"), ("Koroška Bela", "Ela"),
            ("Jablan", "Lan"), ("Krtina", "Tina"), ("Lepa njiva", "Iva"),
            ("Mojstrana", "Ana"), ("Ozeljan", "Jan"),
            ("Slatina", "Tina"), ("Stomaž", "Tomaž"), ("Šentjanž", "Anže"),
            ("Odranci", "Ajda"), ("Polževo", "Tim"),
            ("Lozice", "France")]

        sledilnik = Sledilnik(zacetek)
        sledilnik2 = Sledilnik([("Mala Polana", "Ana"), ("Begunje", "Lan")])

        self.assertEqual(sledilnik.selitev(), 0)
        self.assertIsNone(sledilnik.preseli("Jana", "Ljubljana"))
        self.assertEqual(sledilnik.selitev(), 1)
        self.assertEqual(sledilnik.kje_zivi("Jana"), "Ljubljana")
        self.assertEqual(sledilnik.prebivalci("Ljubljana"), {"Jana"})

        self.assertIsNone(sledilnik.preseli("Jana", "Šentvid"))
        self.assertEqual(sledilnik.selitev(), 2)
        self.assertEqual(sledilnik.kje_zivi("Jana"), "Šentvid")
        self.assertEqual(sledilnik.prebivalci("Ljubljana"), set())
        self.assertEqual(sledilnik.prebivalci("Šentvid"), {"Jana", "Vid"})

        self.assertIsNone(sledilnik.preseli("France", "Slatina"))
        self.assertEqual(sledilnik.selitev(), 3)
        self.assertEqual(sledilnik.kje_zivi("France"), "Slatina")
        self.assertEqual(sledilnik.prebivalci("Lozice"), set())
        self.assertEqual(sledilnik.prebivalci("Slatina"), {"France", "Tina"})

        self.assertIsNone(sledilnik.preseli_vse("Slatina", "Mojstrana"))
        self.assertEqual(sledilnik.selitev(), 5)
        self.assertEqual(sledilnik.kje_zivi("France"), "Mojstrana")
        self.assertEqual(sledilnik.kje_zivi("Tina"), "Mojstrana")
        self.assertEqual(sledilnik.prebivalci("Slatina"), set())
        self.assertEqual(sledilnik.prebivalci("Mojstrana"), {"Ana", "France", "Tina"})

        self.assertIsNone(sledilnik.preseli_vse("Mojstrana", "Šentvid"))
        self.assertEqual(sledilnik.selitev(), 8)
        self.assertEqual(sledilnik.kje_zivi("France"), "Šentvid")
        self.assertEqual(sledilnik.kje_zivi("Tina"), "Šentvid")
        self.assertEqual(sledilnik.kje_zivi("Ana"), "Šentvid")
        self.assertEqual(sledilnik.prebivalci("Mojstrana"), set())
        self.assertEqual(sledilnik.prebivalci("Šentvid"), {"Jana", "Vid", "Ana", "France", "Tina"})

        self.assertEqual(sledilnik2.kje_zivi("Ana"), "Mala Polana")
        self.assertEqual(sledilnik2.selitev(), 0)


if __name__ == "__main__":
    unittest.main()

