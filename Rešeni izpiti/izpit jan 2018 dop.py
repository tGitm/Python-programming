
def migracije(ime_datoteke):
    from collections import defaultdict

    viri = defaultdict(int)
    ponori = defaultdict(int)
    for vrstica in open(ime_datoteke):
        koliko, kraja = vrstica.split(":")
        odkod, kam = kraja. split("->")
        viri[odkod.strip()] += int(koliko)
        ponori[kam.strip()] += int(koliko)

    return naj_kljuc(viri), naj_kljuc(ponori)


def naj_kljuc(d):
    naj_k = None
    naj_v = 0

    for k, v in d.items():
        if v > naj_v:
            naj_k, naj_v = k, v
    return naj_k

'''
Napiši funkcijo migracije(ime_datoteke), ki prejme ime datoteke, ki vsebuje vrstice oblike

8: Maribor -> Ljubljana
3: Maribor -> Nova Gorica
10: Ljubljana -> Maribor
5: Koper -> Nova Gorica
3: Novo mesto -> Nova Gorica
Vsaka vrstica pove, koliko ljudi se je preselilo odkod kam. Funkcija naj vrne par imen krajev: kraj, iz katerega je odšlo največ ljudi in kraj, v katerega se je preselilo največ ljudi. V gornjem primeru funkcija vrne ("Maribor", "Nova Gorica").

Rešitev
Nalogo, najprej, zanima, ali znamo brati datoteke. Nekatere testne datoteke se končajo s prazno vrstico, druge ne ... Če ne počnete neumnosti z for vrstica in open(ime_datoteke).read().split("\n") ali še čim hujšim, temveč lepo pridno napišete for vrstica in open(ime_datoteke), bo vse v redu.

Potem je potrebno razbiti vrstice. Ker sem iz gole hudobije dodal kraje, katerih ime je sestavljeno iz več besed, razbijanje po presledkih ne bo delovalo. Spomniti ste se morali, da lahko metodi split podamo tudi argument. Vrstico najprej razbijemo glede na ":", nato glede na "->". Torej

koliko, kraja = vrstica.split(":")
odkod, kam = kraja.split("->")
Deluje tudi obratno, le nekako bolj logično je tako.

Potem seštevamo prišleke in odšleke v dva slovarja s privzetimi vrednostmi. Na koncu vrnemo ključa, ki ustrezata največji vrednosti v vsakem slovarju.

V return-u kličemo funkcijo naj_kljuc, ki nam vrne ključ, ki pripada največji vrednosti. To se nam splača storiti zato, da ne bomo dvakrat programirali istega. Funkcijo moramo seveda napisati - kar pa ne bi smel biti problem, saj smo to ničkolikokrat počeli na predavanjih, pa tudi v kakšni domači nalogi smo jo videli.
'''


def zakladi(navodila):
    robot = Robot()
    pobrano = {(0, 0)}

    for c in navodila:
        if c == "L":
            robot.levo()
        elif c == "D":
            robot.desno()

        else:
            robot.naprej(int(c))

        x, y = robot.koordinate()
        if (abs(x) + abs(y)) % 7 == 0:
            pobrano.add((x, y))
    return len(pobrano)
'''
Imamo razred Robot. Ta se v začetku nahaja na koordinatah (0, 0) in je obrnjen na desno. Koordinatni sistem je takšen kot pri matematiki: koordinata y narašča navzgor. Robot ima naslednje metode.

naprej(d) gre za d naprej v podani smeri;
desno() se obrne za 90 stopinj v desno;
levo() se obrne za 90 stopinj levo;
koordinate() vrne trenutne koordinate (x in y).
Večini je razred znan iz domače naloge; tokrat je že podan.

Napisati pa morate funkcijo zakladi(navodila), ki prejme navodila za robota v obliki niza, na primer "7D3221LL", kar bi pomenilo, da skoči za 7 polj naprej, se obrne desno, nato skoči za 3 polja naprej, za 2 polji naprej, za 2 polji naprej, za 1 polje naprej, nato se obrne levo in še enkrat levo. Na vseh poljih, za katera velja, da je vsota absolutnih vrednosti njunih koordinat deljiva s 7, je zaklad. (To velja tudi za začetno polje, (0, 0)!).

Funkcija naj vrne, koliko polj z zakladom je robot obiskal. Če večkrat obišče polje z zakladom, dobi zaklad le enkrat. Če zaklad preskoči (torej: gre čez tisto polje, vendar se ne ustavi na njem, ga ne dobi.)

Rešitev
Pri tej nalogi me je zanimalo, ali boste znali pametno uporabiti razred, ki ga že imamo (iz domače naloge). Če ne, bo to zahtevalo (pre)več programiranja. Sicer pa je to naloga iz množic.

Najprej vodenje robota. To je preprosto: gremo čez znake in vsakega od njih prevedemo v eno od akcij Zdaj pa dodamo še pobiranje zakladov. Zlagal jih bo v množico pobrano(), ki bo vsebovala koordinate polj z zakladi, ki jih je obiskal. Če katero dodamo dvakrat - nič hudega, saj gre za množico..
'''

def roboti(navodila, n):
    spremembe = {"S": (0,1), "J": (0, -1), "V": (1,0), "Z": (-1, 0)}
    koordinate = [(0, 0)] * n

    for korak, smer in enumerate(navodila):
        x, y = koordinate[korak % n]
        dx, dy = spremembe[smer]
        x += dx
        y += dy
        koordinate[korak % n] = x, y
    return koordinate

'''
Recimo, da imamo tri robote in jim damo navodila "JSVZZVJ". Vsi roboti začnejo na (0, 0) in izmenično jemljejo navodila iz niza. Prvi robot bo šel za eno polje na J, drugi na S, tretji na V, potem spet prvi na Z, drugi Z, tretji V, prvi J. Njihove koordinate po tem so [(-1, -2), (-1, 1), (2, 0)]. Prvi, recimo, je šel namreč na J, Z in J, zato -1 in -2.

Napiši funkcijo roboti(navodila, n), ki prejme navodila in število robotov (niso nujno trije!), ter vrne seznam terk njihovih koordinat.

Rešitev
Spet premikanje robotov. Tokrat vzemimo, recimo, slovar, ki pove, za koliko se ob posamezni črki spremenita koordinati x in y: {"S": (0, 1), "J": (0, -1), "V": (1, 0), "Z": (-1, 0)}. Potrebovali bomo seznam koordinat, koordinate = [(0, 0)] * n.

Zdaj pa gremo čez navodila. Iz seznama koordinat poberemo koordinati, ju spremenimo, in vpišemo nazaj v seznam. Za to bomo potrebovali enumerate(navodila), da bomo poznali tako črko iz navodil kot tudi njeno zaporedno številko, iz katere bomo izračunali, na katerega robota se črka nanaša. Številko robota dobimo kar z ostankom po deljenju s številom robotov.
'''


def brez_ponavljanja(s):
    if len(s) < 2:
        return s
    elif s[0] == s[1]:
        return brez_ponavljanja(s[1:])
    else:
        return s[:1] + brez_ponavljanja(s[1:])

'''
Napiši rekurzivno funkcijo brez_ponavljanja(s), ki prejme seznam in vrne nov seznam, v katerem vse zaporedne ponovitve istega elementa zamenja z enim samim elementom. Klic brez_ponavljanja([3, 1, 1, 4, 2]) vrne [3, 1, 4, 2].

Pomoč: Seznam brez ponavljanja dobimo tako, da prvi element obdržimo, ali pa ne. Slediti pa mora seznam brez ponavljanja.
'''

class Delitelj:
    def __init__(self, n):
        self.n = n
        self.cena = 0

    def akcija(self, s):
        for i, e in enumerate(s):
            if e % self.n == 0:
                s[i] //= self.n
                self.cena += s[i]

'''
Napiši razred Delitelj, katerega konstruktor kot argument prejme število; imenujmo ga n.

Razred ima metodo akcija(s), ki prejme seznam. V njem vsa števila, ki so deljiva s n, deli s n.

Tega ne dela zastonj: za vsako deljenje zaračuna toliko, kolikor je velik količnik. Skupno ceno vseh dosedanjih klicev akcij hrani v atributu cena.

>>> s = [25, 8, 9, 15, 3, 81]
>>> deli5 = Delitelj(5)
>>> deli5.akcija(s)
>>> s 
[5, 8, 9, 3, 3, 81]
>>> deli5.cena
8
>>> deli5.akcija(s)
>>> s
[1, 8, 9, 3, 3, 81]
>>> deli5.cena
9
Prva cena je 8, ker je naračunal 25/5 = 5 in 15/5 = 3, in 5 + 3 je enako 8. V drugem klicu se cena poveča za 1, ker je delil 5 z 1 in dobil 1.

Rešitev
Konstruktor si bo zapomnil število n in skupno ceno doslej.

Prek seznama gremo z enumerate, da poznamo tako elemente kot njihove indekse, saj jih bomo morali spreminjati. Ko naletimo na element, deljiv z n, ga pač delimo in k ceni prištejemo njegovo novo vrednost.
'''

import unittest


class Robot:
    def __init__(self):
        self.x = self.y = 0
        self.smer = 1

    def desno(self):
        self.smer = (self.smer + 1) % 4

    def levo(self):
        self.smer = (self.smer - 1) % 4

    def naprej(self, d):
        if self.smer == 0:
            self.y += d
        elif self.smer == 1:
            self.x += d
        elif self.smer == 2:
            self.y -= d
        else:
            self.x -= d

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)


class Test01Migracije(unittest.TestCase):
    def test_migracije(self):
        import os
        from random import randint
        fn = "m".format(randint(10000, 99999))
        try:
            with open(fn, "wt") as f:
                f.write("""8: Maribor -> Ljubljana
3: Maribor -> Nova Gorica
10: Ljubljana -> Maribor
5: Koper -> Nova Gorica
3: Novo mesto -> Nova Gorica
""")
            self.assertEqual(migracije(fn), ("Maribor", "Nova Gorica"))

            with open(fn, "wt") as f:
                f.write("""8: Mb -> Lj
3: Mb -> Ng
12: Lj -> Mb
5: Kp -> Ng
3: Nm -> Ng""")
            self.assertEqual(migracije(fn), ("Lj", "Mb"))

            with open(fn, "wt") as f:
                f.write("""8: Mb -> Lj
3: Mb -> Ng""")
            self.assertEqual(migracije(fn), ("Mb", "Lj"))

            with open(fn, "wt") as f:
                f.write("""8: Mb -> Lj
9: Ng -> Lj""")
            self.assertEqual(migracije(fn), ("Ng", "Lj"))

            with open(fn, "wt") as f:
                f.write("""11: Maribor -> Lj
5: Lj -> Celje
9: Ng -> Celje""")
            self.assertEqual(migracije(fn), ("Maribor", "Celje"))
        finally:
            os.remove(fn)


class Test02Zakladi(unittest.TestCase):
    def test_zakladi(self):
        self.assertEqual(zakladi(""), 1)
        self.assertEqual(zakladi("L"), 1)
        self.assertEqual(zakladi("LLL"), 1)
        self.assertEqual(zakladi("7"), 2)
        self.assertEqual(zakladi("77"), 3)
        self.assertEqual(zakladi("733"), 2)
        self.assertEqual(zakladi("7331"), 3)
        self.assertEqual(zakladi("7D32"), 2)
        self.assertEqual(zakladi("7D322"), 3)
        self.assertEqual(zakladi("7D3221LL"), 3)
        self.assertEqual(zakladi("7D322LL7"), 3)
        self.assertEqual(zakladi("7D322LL77"), 4)
        self.assertEqual(zakladi("7D331"), 3)
        self.assertEqual(zakladi("7D33D1"), 2)
        self.assertEqual(zakladi("7LLL77LLL"), 4)


class Test03Roboti(unittest.TestCase):
    def test_roboti(self):
        self.assertEqual(roboti("V", 1), [(1, 0)])
        self.assertEqual(roboti("Z", 1), [(-1, 0)])
        self.assertEqual(roboti("S", 1), [(0, 1)])
        self.assertEqual(roboti("J", 1), [(0, -1)])

        self.assertEqual(roboti("VZVZ", 2), [(2, 0), (-2, 0)])
        self.assertEqual(roboti("VZVZV", 2), [(3, 0), (-2, 0)])

        self.assertEqual(roboti("SJVZSJVZSJVZ", 4), [(0, 3), (0, -3), (3, 0), (-3, 0)])
        self.assertEqual(roboti("SJVZSJVZSJVZ", 12), 3 * [(0, 1), (0, -1), (1, 0), (-1, 0)])

        self.assertEqual(roboti("S", 3), [(0, 1), (0, 0), (0, 0)])
        self.assertEqual(roboti("", 300), 300 * [(0, 0)])
        self.assertEqual(roboti("SJ" * 100, 200), 100 * [(0, 1), (0, -1)])


class Test04BrezPonavljanja(unittest.TestCase):
    def test_brez_ponavljanja(self):
        self.assertEqual(brez_ponavljanja([3, 1, 1, 4, 2]), [3, 1, 4, 2])
        self.assertEqual(brez_ponavljanja([3, 1, 1, 4, 2, 1]), [3, 1, 4, 2, 1])
        self.assertEqual(brez_ponavljanja([3, 1, 1, 4, 4, 15, 4, 2, 1]), [3, 1, 4, 15, 4, 2, 1])

        self.assertEqual(brez_ponavljanja([3, 42, 42]), [3, 42])
        self.assertEqual(brez_ponavljanja([42, 42, 3]), [42, 3])

        self.assertEqual(brez_ponavljanja([42, 42]), [42])
        self.assertEqual(brez_ponavljanja([42]), [42])
        self.assertEqual(brez_ponavljanja([]), [])


class Test05Delitelj(unittest.TestCase):
    def test_delitelj(self):
        deli1 = Delitelj(1)
        deli3 = Delitelj(3)
        deli5 = Delitelj(5)

        self.assertEqual(deli1.cena, 0)
        self.assertEqual(deli3.cena, 0)
        self.assertEqual(deli5.cena, 0)

        s = [25, 8, 9, 15, 3, 81]

        self.assertIsNone(deli1.akcija(s))
        self.assertEqual(s, [25, 8, 9, 15, 3, 81])
        self.assertEqual(deli1.cena, sum(s))
        self.assertEqual(deli3.cena, 0)
        self.assertEqual(deli5.cena, 0)

        self.assertIsNone(deli1.akcija(s))
        self.assertEqual(s, [25, 8, 9, 15, 3, 81])
        self.assertEqual(deli1.cena, 2 * sum(s))
        self.assertEqual(deli3.cena, 0)
        self.assertEqual(deli5.cena, 0)

        self.assertIsNone(deli3.akcija(s))
        self.assertEqual(s, [25, 8, 3, 5, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, 0)

        self.assertIsNone(deli5.akcija(s))
        self.assertEqual(s, [5, 8, 3, 1, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, 5 + 1)

        self.assertIsNone(deli5.akcija(s))
        self.assertEqual(s, [1, 8, 3, 1, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, (5 + 1) + 1)

        self.assertIsNone(deli5.akcija(s))
        self.assertEqual(s, [1, 8, 3, 1, 1, 27])
        self.assertEqual(deli3.cena, 3 + 5 + 1 + 27)
        self.assertEqual(deli5.cena, (5 + 1) + 1)

        self.assertIsNone(deli3.akcija(s))
        self.assertEqual(s, [1, 8, 1, 1, 1, 9])
        self.assertEqual(deli3.cena, (3 + 5 + 1 + 27) + (1 + 9))
        self.assertEqual(deli5.cena, (5 + 1) + 1)


if __name__ == "__main__":
    unittest.main()
