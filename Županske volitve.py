def glasov(obkrozeno):
    st = 0

    for i in obkrozeno:
        if i:
            st += 1

    return st


def voljeni(obkrozeno, imena):
    c = None
    for i, ime in zip(obkrozeno, imena):

        if i:
            c = ime

    if glasov(obkrozeno) != 1:
        c = None

    return c


def najvecji(d):
    mak = 0

    ime = " "
    for z, j in d.items():
        mak = j
        break

    for z, j in d.items():
        if j > mak:
            mak = j
            ime = z

    if d == {}:
        ime = None
        mak = None

    return (ime, mak)


def pristej(s, t):
    for k, d in t.items():
        if k in s.keys():
            s[k] = s[k] + d

        elif k not in s.keys():
            s[k] = d


def zmagovalec(glasovnice):
    '''preverimo = 0
        lis = []
        lis2 = []
        lis3 = []
        #a = 0
        #b = 0
        #d = voljeni(a, b)

        for a, b in glasovnice:
            iz = voljeni(a, b)
            lis.append(iz)

        for k in lis2:
            if k != None:
                lis2.append(k)

        for w in lis3:
            if w not in lis3:
                lis3.append(w)

        return (lis, / len(lis2)
    '''

    lis = []

    for i, k in glasovnice:
        if glasov(i) == 1:
            for c, e in zip(i, k):
                if c:
                    lis.append(e)

    lis2 = (max(set(lis),
                key = lis.count))

    lis3 = lis.count(lis2)

    return lis2, lis3/len(lis)


def voljeni_vec(obkrozeno, imena):
     d = {}
     for n, o in zip(obkrozeno, imena):
        if n:
            d[o] = 1 / glasov(obkrozeno)

     return d

        # delez = 1 / (glasov(obkrozeno))

def voljeni_vec(obkrozeno, imena):
    delez = 1 / (glasov(obkrozeno) or 42)
    return {ime: delez for ime in vsi_obkrozeni(obkrozeno, imena)}


import unittest

class TestObvezna(unittest.TestCase):
    def test_glasov(self):
        self.assertEqual(2, glasov([True, False, False, True]))
        self.assertEqual(1, glasov([True] + [False] * 1000))
        self.assertEqual(20, glasov([True] * 20 + [False] * 1000))
        self.assertEqual(0, glasov([False] * 1000))
        self.assertEqual(0, glasov([]))

    def test_voljeni(self):
        self.assertEqual("Anna", voljeni([True, False, False], ["Anna", "Berta", "Cilka"]))
        self.assertEqual("Berta", voljeni([False, True, False], ["Anna", "Berta", "Cilka"]))
        self.assertEqual("Cilka", voljeni([False, False, True], ["Anna", "Berta", "Cilka"]))
        self.assertEqual("Cilka", voljeni([True], ["Cilka"]))

        self.assertIsNone(voljeni([True, False, True], ["Anna", "Berta", "Cilka"]))
        self.assertIsNone(voljeni([False, False, False], ["Anna", "Berta", "Cilka"]))
        self.assertIsNone(voljeni([False], ["Cilka"]))
        self.assertIsNone(voljeni([True, True, True], ["Anna", "Berta", "Cilka"]))
        self.assertIsNone(voljeni([], []))

    def test_najvecji(self):
        a, b, c, d = "abcd"
        self.assertEqual((d, 42), najvecji({a: 15, b: 30, c: 8, d: 42}))
        self.assertEqual((c, -5), najvecji({a: -10, b: -30, c: -5, d: -42}))
        self.assertEqual((c, "Dani"), najvecji({a: "Anna", b: "Berta", c: "Dani", d: "Cilka"}))
        self.assertEqual((None, None), najvecji({}))

    def test_pristej(self):
        a, b, c, d = "abcd"
        s = {a: 5, b: 6, d: 4}
        t = {b: 3, c: 8}
        self.assertIsNone(pristej(s, t))
        self.assertDictEqual({a: 5, b: 9, c: 8, d: 4}, s)
        self.assertDictEqual({b: 3, c: 8}, t)

        e = {}
        self.assertIsNone(pristej(s, e))
        self.assertDictEqual({a: 5, b: 9, c: 8, d: 4}, s)
        self.assertDictEqual({}, e)

        self.assertIsNone(pristej(e, t))
        self.assertDictEqual({b: 3, c: 8}, e)

    def test_zmagovalec(self):
        zmago, delez = zmagovalec(
            [([False, True, True], ["Berrta", "Ana", "Cilka"]),  # neveljavna
             ([False, True, True], ["Berrta", "Ana", "Cilka"]),  # neveljavna
             ([False, False, True], ["Ana", "Cilka", "Berrta"]), # Berrta
             ([False, True, False], ["Ana", "Berrta", "Cilka"]), # Berrta
             ([False, True, False], ["Berrta", "Ana", "Cilka"])  # Ana
             ])
        self.assertEqual(zmago, "Berrta")
        self.assertAlmostEqual(2 / 3, delez)

        zmago, delez = zmagovalec(
            [([False, True, True], ["Berrta", "Ana", "Cilka"]),  # neveljavna
             ([False, True, True], ["Berrta", "Ana", "Cilka"]),  # neveljavna
             ([False, True, False], ["Ana", "Cilka", "Berrta"]), # Berrta
             ])
        self.assertEqual(zmago, "Cilka")
        self.assertAlmostEqual(1, delez)


    def test_voljeni_vec(self):
        self.assertEqual(
            {"Ana": .5, "Cilka": .5},
            voljeni_vec([False, True, True], ["Berrta", "Ana", "Cilka"]))
        self.assertEqual(
            {"Cilka": 1},
            voljeni_vec([False, False, True], ["Berrta", "Anna", "Cilka"]))
        self.assertEqual(
            {"Cilka": 0.25, "Berrta": 0.25, "Anna": 0.25, "Dani": 0.25},
            voljeni_vec([True] * 4, ["Berrta", "Anna", "Cilka", "Dani"]))
        self.assertEqual({}, voljeni_vec([False, False], ["Ana", "Berta"]))
        self.assertEqual({}, voljeni_vec([], []))


class TestDodatna(unittest.TestCase):
    def test_ujemanje(self):
        self.assertAlmostEqual(1 / 6, ujemanje(list("abc"), list("cdef")))
        self.assertAlmostEqual(0.5, ujemanje(list("abc"), list("acd")))
        self.assertAlmostEqual(0, ujemanje(list("abc"), list("def")))
        self.assertAlmostEqual(0, ujemanje([], list("acd")))
        self.assertAlmostEqual(0, ujemanje(list("acd"), []))
        self.assertAlmostEqual(0, ujemanje([], []))
        self.assertAlmostEqual(1, ujemanje(list("abc"), list("bca")))
        self.assertAlmostEqual(0.5, ujemanje(list("abcdef"), list("abc")))
        self.assertAlmostEqual(0.5, ujemanje(list("defabc"), list("abc")))
        self.assertAlmostEqual(0.5, ujemanje(list("d"), list("ad")))
        self.assertAlmostEqual(0.5, ujemanje(list("d"), list("ad")))
        self.assertAlmostEqual(1, ujemanje(list("d"), list("d")))

    def test_naj_kandidati(self):
        kandidati = [("Ana", list("abc")),
                     ("Berta", list("bcd")),
                     ("Cilka", list("abcdefg")),
                     ("Dani", list("d")),
                     ("Ema", list("adefgh"))]
        self.assertEqual(("Ana", "Berta"), naj_kandidata(kandidati, list("abc")))
        self.assertEqual(("Dani", "Berta"), naj_kandidata(kandidati, list("d")))


if __name__ == "__main__":
    unittest.main()
