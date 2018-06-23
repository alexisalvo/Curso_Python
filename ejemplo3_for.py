suma = 0
n = int(input("ingrese numeros: "))
for a in range(n):
    x = float(input("ingrese un dato: "))
    suma = suma + x
    promedio = suma / n
print("el promedio es: ", promedio)
