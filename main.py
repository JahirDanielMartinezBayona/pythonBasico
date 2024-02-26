print("LA TABLA DE MULTIPLICAR QUE TANTO TE GUSTA")
multiploBase = input("Ingresa el múltiplo base de la tabla: ")
multiploMaximo = input("Ingresa el múltiplo hasta dónde puede ser multiplicado la tabla: ")
print("La tabla a multiplicar es: "+ str(multiploBase))

almacenarDatoMultiplo = int(multiploMaximo)+1
for postearMultiplo in range(1,almacenarDatoMultiplo):
    resultado = int(multiploBase) * int(postearMultiplo)
    print(f"{multiploBase} x {postearMultiplo} = {resultado}")