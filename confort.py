c = int(input("ingrese compra:"))
t = 100
if c >= 10:
    p = c * 0.25
    total = p * c * t
elif c >= 5 and c <= 9:
    p = c * 0.20
    total = p * c * t
elif c >= 1 and c <= 4:
    p = c * 0.15
    total = p * c * t
print("total a pagar:", total)

