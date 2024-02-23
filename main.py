numPrimo = int(input("Ingrese el número para averiguar si es primo: "))
divisorPrimo = numPrimo
contarCantidadMultiplo = 0;
while int(divisorPrimo) >= 1:
    if int(numPrimo) % int(divisorPrimo) == 0:
        contarCantidadMultiplo+=1
    divisorPrimo -= 1
if contarCantidadMultiplo == 2:
    print("El número " + str(numPrimo) + " es primo")
else:
    print("El número " + str(numPrimo) + " no es primo")
