ht = int(input("Horas trabajadas?: "))
tarifa_hora = 5000
if ht > 40:
   tarifa_hora = tarifa_hora * 1.5
   pago = tarifa_hora * ht
   print ("total a pagar son:",pago)
else:
    pago = tarifa_hora * ht
    print ("total a pagar son:",pago)
