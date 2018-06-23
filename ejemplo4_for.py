from random import*
n = int(input("ingrese numero:"))
gana = 0
for a in range(n):
    x = randint (1,6)
    print(x)
    if x == 6:
        gana = gana + 600
    elif x == 3:
        gana = gana + 300
    elif x == 1:
        print("seguir jugando")
    else:
        gana = gana - 50
print("la ganancia total es:", gana)

