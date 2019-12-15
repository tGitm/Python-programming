from random import*
from math import*


n = 0
st = 0


while st < 1000:
    x = int(2 * (random() - 1))
    y = int(2 * (random() - 1))


    hip = sqrt((pow(x, 2) + pow(y, 2)))


    if hip <= 1:
        n += 1

    st = st + 1


st_pi = (4 * n) / 1000

print("Število Pi: ", st_pi)


