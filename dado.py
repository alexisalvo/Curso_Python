from random import *
x = 0
i = 0
while True:
    x = randint (1, 1000)
    print(x)
    i += 1
    if x == 5:
        break
    print("El lanzamiento en el que salio el 5 fue: " , i)
