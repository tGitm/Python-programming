
ljubljana = [28, 30, 25, 28, 30, 32, 35, 28, 25, 27]
maribor = [30, 28, 26, 34, 26, 32, 34, 30, 28, 28]
celje = [28, 32, 30, 31, 32, 28, 27, 26, 25, 25]
koper = [32, 35, 35, 31, 32, 34, 35, 30, 28, 28]
kranj = [28, 27, 30, 32, 28, 27, 26, 28, 30, 25]


max = 0
cel = 0
avg = 0

for ljubljana, maribor in zip(ljubljana, maribor):

    if abs((ljubljana-maribor)) > max:
        max = abs((ljubljana-maribor))

if maribor > ljubljana:
    print(max, "Maribor")

else:
    print(max, "Ljubljana")


# Dodatna naloga:
'''
for ljubljana, maribor, celje, koper, kranj in zip(ljubljana, maribor, celje, koper, kranj):

    avg = (ljubljana + maribor + celje + koper + kranj) / 5
    print("Povprečje: ", avg)

    if avg > 30:
        cel = cel + 1

print("Temperatura je bila višja od 30°C ", cel, "krat.")

'''
