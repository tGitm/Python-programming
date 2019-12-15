import math 

hitrost = float(input("Hitrost strela? "))
kot_izs = float(input("Kot izstrelka? "))

#s = ((v**2) * (sin**2 * kot)) / g
dolzina = (pow(hitrost, 2) * math.sin((2 * kot_izs) * 0.01745329252) / 9.81)

print("Dolžina strela znaša: ", dolzina, "m.")