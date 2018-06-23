def grados_dias():
    temperatura = float(input("Ingrese temperatura de ahora:"))
    if temperatura >= 10 and temperatura <= 31.1:
        while temperatura >= 10:
            GD = temperatura - 10
            print GD
            break
    else:
        print("nada de GD")
