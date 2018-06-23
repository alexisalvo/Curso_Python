tiempo_llamada = int(input("duracion llamada:"))
if tiempo_llamada <= 10:
    print ("costo de la llamada: 10 pesos")
else:
    tiempo_llamada = 10 * 1.05
    print ("costo de la llamada es:", tiempo_llamada)
    