numFactorial = int(input("Ingrese el número para conocer su factorial: "))
acumularResultadoFactorial = 1
while numFactorial>=1:
    acumularResultadoFactorial = acumularResultadoFactorial * numFactorial
    numFactorial-=1
print("El resultado del factorial es: " + str(acumularResultadoFactorial))
