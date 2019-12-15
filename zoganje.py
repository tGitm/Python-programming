from math import sin, cos, radians
import risar
import random


class Zoganje:
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 800)
        self.body = risar.krog(0, 0, 10, risar.nakljucna_barva(), 3)
        self.angle = random.randint(-180, 180)
        self._update()

    def _update(self):
        self.body.setPos(self.x, self.y)

    def forward(self, forw):
        self.x = self.x + forw * cos(radians(self.angle))
        self.y = self.y - forw * sin(radians(self.angle))
        self._update()



krogci = []
for i in range(30):
    krogci.append(Zoganje())

while True:
    for krog in krogci:
        krog.forward(5)

        if (krog.x < 0 or krog.x > 800):
            krog.angle = 180 - krog.angle

        elif (krog.y > 500 or krog.y < 0):
            krog.angle = 360 - krog.angle

    risar.cakaj(0.02)

risar.stoj()
