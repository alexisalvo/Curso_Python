nombre = "abcdefghijklnmopkrspquvwxyz"
vocal = "vocal"
i = 0
for i in range(len(nombre)):
    if nombre[i] == "a" or nombre[i] == "e" or nombre[i] == "i" or nombre[i] == "o" or nombre[i] == "u":
        print nombre[i] + vocal
    