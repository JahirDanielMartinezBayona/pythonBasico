numCantidadPromedio = int(input("Ingrese la cantidad de números a calcular su promedio: "))
mostrarNumeroElemento = 1
posicionNumeroElemento = 0
arregloPromedioNumeros = []
sumaPromedio = 0
resultadoPromedio = 0
while numCantidadPromedio > 0:
    arregloPromedioNumeros.append((input("Ingresa el número " + str(mostrarNumeroElemento) + ": ")))
    mostrarNumeroElemento += 1
    numCantidadPromedio -= 1

while posicionNumeroElemento <= (len(arregloPromedioNumeros)-1):
    sumaPromedio = float(sumaPromedio) + float(arregloPromedioNumeros[posicionNumeroElemento])
    posicionNumeroElemento += 1
resultadoPromedio= sumaPromedio/(len(arregloPromedioNumeros))
print("La cantidad de números evaluados fueron: "+str(len(arregloPromedioNumeros)))
print("El promedio de los números insertados es: "+str(resultadoPromedio))