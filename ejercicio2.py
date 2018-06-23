n1 = int(input("Ingrese el primer numero:"))
n2 = int(input("ingrese el segundo numero:"))
div = n1 / n2
print div
sum = n1 + n2
print sum
mul = n1 * n2
print mul
res = n1 - n2
print res
if div < 20 and sum < 20 and mul < 20 and res < 20:
    print "azul"
elif div < 40 and sum < 40 and mul < 40 and res < 40:
    print "rojo"
elif div < 60 and sum < 60 and mul < 60 and res < 60:
    print "negro"
else:
    print "error, interntelo nuevamente"
