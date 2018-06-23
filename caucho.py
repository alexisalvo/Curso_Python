n = int(input("Ingrese la cantidad de cauchos a comprar: "))
p = float(input("Ingrese el precio unitario: "))
if n >= 6:
    d = 0.15 * p
    total =  p * d
else:
    d = 0.1 * p
    total =  p * d
suma = n * total
print("El total a pagar es: " ,suma)
