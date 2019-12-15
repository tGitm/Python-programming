
#dop
def dolzina_poti(pari, x):
    pari = dict(pari)
    length = 0

    while x in pari:
        length += 1
        x = pari[x]
    return length
'''
Napiši funkcijo dolzina_poti(s, o), ki prejme tak seznam in številko osebe, ki ji damo čokolado, ter vrne število podaj, preden bo čokolada pojedena. Klic dolzina_poti([(8, 2), (1, 8), (5, 1), (4, 42)], 5) vrne 3. 
Če namreč damo čokolado osebi 5, jo bo ta dala osebi 1, oseba 1 osebi 8 in oseba 8 osebi 2, ki jo poje. Torej tri podaje.
'''

def ne_daje_naprej(pari):
    dobi = set()
    daje = set()

    for kdo, komu in pari:
        dobi.add(komu)
        daje.add(kdo)
    return dobi - daje
'''
Napiši funkcijo ne_daje_naprej(s), ki prejme takšen seznam in vrne množico številk oseb, ki čokolad ne dajejo naprej. V gornjem primeru je to {2, 5}.

Seznam lahko tudi zelo dolg; morda se ga splača znotraj funkcije pretvoriti v kaj prikladnejšega za to nalogo.
'''

def alterniraj(s):
    n = []
    for i in s:
        if not n or i * n[-1] < 0:
            n.append(i)
    s[:] = n
'''
Napiši funkcijo alterniraj(s), ki prejme seznam števil in ga spremeni tako, da za vsakim pozitivnim številom odstrani vsa števila do naslednjega negativnega števila, in za vsakim negativnim vsa števila do naslednjega pozitivnega.
 Funkcija naj spremeni podani seznam in ne vrne ničesar.

Z drugimi besedami, funkcija obdrži prvi element vsakega zaporedja pozitivnih ali negativnih števil.

Seznam [3, 4, -1, 1, -5, -2, -1, 7, -8] tako spremeni v [3, -1, 1, -5, 7, -8].

Z not n poskrbibo, da bomo gotovo dodali prvi element. Z e * n[-1] < 0 pa preverimo, ali ima e drugačen predznak kot zadnji element n. Če imata namreč različne predznake, bo njun produkt negativen.

Seveda bi delovalo tudi kaj bolj zapletenega, na primer e < 0 and n[-1] > 0 or e > 0 and n[-1] < 0. A naj se vidi, da poznavanje matematike koristi.

V nalogi sem pozabil določiti, kaj naj se zgodi z ničlami. No, recimo, da jih ni. Vsaj v testih jih ni bilo in upam, da je to dovolj pregnalo skrbi.
'''

def nima_vhoda(bots):
    from collections import Counter
    outs = [b for (o, b), (_, __) in bots.values() if o == "bot"] + \
           [b for (_, __), (o, b) in bots.values() if o == "bot"]

    cts = Counter(outs)
    return set(bots) - set(outs), {b for b, c in cts.items() if c == 1}

'''
V dveh domačih nalogah smo delali z mrežami botov. Recimo, da so opisane s slovarji, kot v prvih od teh domačih nalog. Napiši funkcijo nima_vhoda(boti), ki prejme takšen slovar in vrne dve množici: 
množico botov, ki ne prejmejo nobenega čipa od drugega bota in množico botov, ki prejme od drugega bota le en čip. Za mrežo na sliki mora vrniti množici {1, 2}, {3, 6}.
'''

#dolžine ladij
def dolzina(plosca, x, y):
    v = 1
    while x + v < len(plosca[y]) and plosca[y][x + v] == "X":
        v += 1
    s = 1
    while y + s < len(plosca) and plosca[y + s][x] == "X":
        s += 1
    return max(v, s)
'''
Recimo, da položaj pri igri Potapljanje ladjic predstavimo s seznamom nizov, kot, recimo

[".......XXX....X",
 "X..XX.......X..",
 "X......XXXXX...",
 "X..XX.........."]
Napiši funkcijo dolzina(plosca, x, y), ki prejme takšno ploščo in pove, kako dolga je ladja, ki se začne na koordinatah x, y in gre potem na desno ali navzdol.
 Poleg tega napiši funkcijo najdaljsa_ladja(plosca), ki vrne dolžino najdaljše ladje na plošči; v gornjem primeru je to 5.
 Od podanega polja poskušamo riniti na desno in navzdol. Koliko desno lahko gremo, smo merili v v, koliko dol, pa v s. Eno od teh števil bo vedno 1. Vrnemo tisto, ki je večje.

Najdaljšo ladjo potem dobimo tako, da preverimo vse dolžine ladij. To lahko storimo na kak dolg način ali pa z izpeljanim seznamom (oziroma generatorjem).
'''

def na_poti(oddajnik, prejemnik, boti):
    return oddajnik == prejemnik \
        or any(na_poti(kam, prejemnik, boti)
               for kako, kam in boti[oddajnik] if kako == "bot")

'''
Napiši rekurzivno funkcijo na_poti(oddajnik, sprejemnik, boti), ki pove (True ali False) ali je možno, da bo eden od čipov, ki jih oddaja oddajnik, prišel v roke sprejemniku. Zadnji argument je slovar botov, kakršnega smo vajeni iz domačih nalog.

V gornjem primeru je možno, da bo čip, ki ga oddaja bot 1, prišel do bota 6. Čip, ki ga oddaja 3, pa ne more do bota 6.
'''

class Mesto:
    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina
        self.polno = set()

    def postavi(self, x, y):
        self.polno.add((x,y))

    def porusi(self, x0, y0, x1, y1):
        self.polno -= {(x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)}

    def prosto(self):
        return self.sirina * self.visina - len(self)

    def __len__(self):
        return len(self.polno)
'''
Napiši razred Mesto, ki predstavlja mesto, postavljeno na koordinatno mrežo.

Konstruktor prejme njegovo širino in višino.
Metoda postavi(x, y) postavi hišo na koordinate x, y. Koordinate številčimo od 0 naprej. Če postavimo na isto mesto več hiš, je postavljena le ena.
Metoda porusi(x0, y0, x1, y1) poruši vse hiše v pravokotniku med vključno x0, y0 in vključno x1, y1 (pri smeš predpostaviti, da velja x0 <= x1 in y0 <= y1).
Klic len(mesto), pri čemer je mesto nek objekt vrste Mesto, naj vrne število zasedenih polj.
Metoda prosto() naj vrne število prostih polj.

Rešitev
Čeprav naj bi bila to naloga iz objektnega programiranja, je le-to relativno preprosto. Razmisliti moramo predvsem, kako bomo shranili podatek o tem, kje so hiše.
Najpreprosteje bo, če jih damo kar v množico. Tako dobimo
V porusi smo uporabili izpeljano množico. Lahko bi napisali tudi dve zanki in odstranjevali hišo za hišo.
V postavi bi lahko preverili, ali so koordinate res na tej mreži. Vendar naloga tega ni zahtevala, torej ne bomo. Potemtakem pa pravzprav niti ne potrebujemo self.sirina in self.visina, temveč le njun produkt, ki je potreben za izračun števila prostih mest.v
'''

class Ladja:
    def __init__(self, zacetno, dolzina, smer):
        x, y = zacetno

        if smer == ">":
            self.polja = {(x + k, y) for k in range(dolzina)}
        else:
            self.polja = {(x, y + k) for k in range(dolzina)}

    def __len__(self):
        return len(self.polja)

    def strel(self, x, y):
        self.polja -= {(x, y)}
'''
Napiši razred Ladja, ki predstavlja ladjo iz igre Potapljanje ladjic.

Konstruktor prejme tri argumente: prvi je terka s koordinama začetnega polja (x in y), drugi dolžina ladje in tretji smer, ki je lahko ">" (ladja je postavljena tako, da narašča koordinata x) ali "v" (narašča koordinata y).
Metoda strel(x, y) pomeni, da je igralec ustrelil na polje s podanimi koordinatami. Pri tem je morda zadel ladjo, morda ne.
Klic len(ladja), kjer je ladja nek objekt razreda Ladja, vrne število nepotopljenih delov ladje. Če je ladja v začetku dolga 5 in zadanemo dva dela, bo len(ladja) vrnil 3.
Rešitev
Tudi tole ni bistveno drugače kot v izpitu za prvo skupino: spet bi moralo iti za objektno programiranje, v resnici pa moramo razmisliti predvsem, kako bomo shranjevali podatke. 
In izkaže se, da enako, kot v izpitu za prvo skupino: v množici. Tokrat množici koordinat, na kateri se nahajajo deli ladje.
'''




import unittest


class Test01DolzinaPoti(unittest.TestCase):
    def test_dolzina_poti(self):
        import random
        from itertools import chain

        stevilke = list(range(1, 100001))
        random.shuffle(stevilke)

        kosi = stevilke[:50000], stevilke[50000:70000], stevilke[70000:]
        pari = list(chain(*(zip(p, p[1:]) for p in kosi)))
        random.shuffle(pari)
        self.assertEqual(dolzina_poti([(1, 2), (3, 4), (2, 3)], 1), 3)
        self.assertEqual(dolzina_poti([(1, 2), (2, 3), (3, 4)], 2), 2)
        self.assertEqual(dolzina_poti([(1, 2), (2, 3), (3, 4), (5, 6)], 1), 3)
        self.assertEqual(dolzina_poti([(1, 2), (2, 3), (3, 4), (5, 6)], 5), 1)
        self.assertEqual(dolzina_poti([(1, 2), (2, 3), (3, 4), (5, 6)], 6), 0)
        self.assertEqual(dolzina_poti(pari, stevilke[0]), 49999)
        self.assertEqual(dolzina_poti(pari, stevilke[1]), 49998)
        self.assertEqual(dolzina_poti(pari, stevilke[50000]), 19999)


class Test02Alterniraj(unittest.TestCase):
    def test_alterniraj(self):
        s = [3, 4, -1, 1, -5, -2, -1, 7, -8]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [3, -1, 1, -5, 7, -8])

        s = [3, 4, 8, 1, 2]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [3])

        s = [3, 4, 8, 1, -4, 2]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [3, -4, 2])

        s = []
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [])

        s = [-1]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [-1])

        s = [5]
        self.assertIsNone(alterniraj(s))
        self.assertEqual(s, [5])


class Test03NimaVhoda(unittest.TestCase):
    def test_nima_vhoda(self):
        # https://ucilnica.fri.uni-lj.si/mod/assign/view.php?id=17726
        instr = {1: (('bot', 3), ('bot', 4)),
                 2: (('bot', 4), ('output', 0)),
                 3: (('output', 5), ('bot', 5)),
                 4: (('bot', 5), ('bot', 6)),
                 5: (('output', 1), ('bot', 7)),
                 6: (('bot', 7), ('output', 4)),
                 7: (('output', 2), ('output', 3))}
        self.assertEqual(nima_vhoda(instr), ({1, 2}, {3, 6}))


class Test04NaPoti(unittest.TestCase):
    def test_na_poti(self):
        instr = {1: (('bot', 3), ('bot', 4)),
                 2: (('bot', 4), ('output', 0)),
                 3: (('output', 5), ('bot', 5)),
                 4: (('bot', 5), ('bot', 6)),
                 5: (('output', 1), ('bot', 7)),
                 6: (('bot', 7), ('output', 4)),
                 7: (('output', 2), ('output', 3))}
        self.assertTrue(na_poti(1, 1, instr))
        self.assertFalse(na_poti(1, 2, instr))
        self.assertTrue(na_poti(1, 3, instr))
        self.assertTrue(na_poti(1, 4, instr))
        self.assertTrue(na_poti(1, 5, instr))
        self.assertTrue(na_poti(1, 6, instr))
        self.assertTrue(na_poti(1, 7, instr))

        self.assertFalse(na_poti(2, 1, instr))
        self.assertTrue(na_poti(2, 2, instr))
        self.assertFalse(na_poti(2, 3, instr))
        self.assertTrue(na_poti(2, 4, instr))
        self.assertTrue(na_poti(2, 5, instr))
        self.assertTrue(na_poti(2, 6, instr))
        self.assertTrue(na_poti(2, 7, instr))

        self.assertFalse(na_poti(4, 1, instr))
        self.assertFalse(na_poti(4, 2, instr))
        self.assertFalse(na_poti(4, 3, instr))
        self.assertTrue(na_poti(4, 4, instr))
        self.assertTrue(na_poti(4, 5, instr))
        self.assertTrue(na_poti(4, 6, instr))
        self.assertTrue(na_poti(4, 7, instr))

        self.assertFalse(na_poti(5, 1, instr))

        self.assertFalse(na_poti(7, 1, instr))
        self.assertFalse(na_poti(7, 2, instr))
        self.assertFalse(na_poti(7, 3, instr))
        self.assertFalse(na_poti(7, 4, instr))
        self.assertFalse(na_poti(7, 5, instr))
        self.assertFalse(na_poti(7, 6, instr))
        self.assertTrue(na_poti(7, 7, instr))


class Test05Mesto(unittest.TestCase):
    def test_mesto(self):
        m = Mesto(5, 8)
        self.assertEqual(len(m), 0)
        self.assertEqual(m.prosto(), 40)

        m.postavi(2, 6)
        self.assertEqual(len(m), 1)
        self.assertEqual(m.prosto(), 39)

        m.postavi(2, 6)
        self.assertEqual(len(m), 1)
        self.assertEqual(m.prosto(), 39)

        for x in range(4):
            for y in range(2, 5):
                m.postavi(x, y)
        self.assertEqual(len(m), 13)
        self.assertEqual(m.prosto(), 27)

        m.porusi(1, 1, 2, 4)
        self.assertEqual(len(m), 7)
        self.assertEqual(m.prosto(), 33)

if __name__ == "__main__":
    unittest.main()

