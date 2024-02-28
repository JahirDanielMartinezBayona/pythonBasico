import sys
Panes = {
    "Pan de Bono": 700,
    "Pan de Queso": 800,
    "Pan de Yuca": 800,
    "Calentano": 700,
    "Rollito de Sal": 900,
    "Pan Integral": 700,
    "Pan relleno de Arequipe": 1150,
    "Pan con Salchicha": 1300,
    "Pan recubierto de Chocolate": 1200}
Pasteles = {
    "Pastel de Vainilla": 5000,
    "Pastel de Chocolate": 5500,
    "Pastel de Arequipe": 5700,
    "Pastel de Oreo": 7000,
    "Postre de Vainilla": 4000,
    "Postre de Tres Leches": 4500}
Bebida = {
    "Coca-Cola": 3000,
    "Red-Bull": 4000,
    "Gatorade": 3700,
    "Budweiser": 3200,
    "Pony-Malta": 2300,
    "Monster": 3000,
    "Tropicana": 2400}
Promociones = {
    "a) Panes de yuca": 4000,
    "b) Pan relleno de Arequipe": 5500,
    "c) Pastel de Arequipe": 13000,
    "d) Postres de Oreo": 25000,
}

productos_por_categoria = {
    "Panaderia": Panes,
    "Pasteleria": Pasteles,
    "Bebidas": Bebida ,
    "Apartado de Promociones": Promociones
    } 

#Bienvenida
print("BIENVENIDO A ENJOYBREAD, LA PANADERÍA NÚMERO UNO EN SABOR DE LEVADURA")
#Menu
print("Nuestro menu:")
for posicionCategoria,categoria in enumerate(productos_por_categoria, start=0):
    print(f" {posicionCategoria+1}. {categoria}")

opcionCategoria = int(input("Ingresa la categoria digitando un número: "))

categoria_seleccionada = list(productosCategoria.keys())[opcionCategoria - 1]
productosCategoriaSeleccionada = productosCategoria[categoriaSeleccionada]

print(f"\nProductos disponibles en la categoria '{categoriaSeleccionada}':")
for disponibleCategoriaPosicion, (productoPan, precioPan) in enumerate(productosCategoriaSeleccionada.items(), start=1):
    print(f" {disponibleCategoriaPosicion}. {productoPan} - ${precioPan}")

opcionesProductos = int(input("\nIngrese el numero del producto que desea comprar. Para otros productos, seleccione por comas(,): "))

productoSeleccionado = list(productosCategoriaSeleccionada.keys())[opcionesProductos - 1]
precioProductoSeleccionado = productosCategoriaSeleccionada[productoSeleccionado]

print(f"\nEl producto que desea comprar es'{productoSeleccionado}' con un precio de'{precioProductoSeleccionado}.")


respuesta = input("¿Es esto correcto?: ")
if respuesta.lower() == "no": 
    print("Perfecto, acá estamos para servirte y puedes volver cuando quieras. Bonito día")
    sys.exit()
else: 
    print("Muy bien, ahora procedemos al pago de los productos")

dinero = int(input("Ingrese el dinero: "))

cambio = dinero - precioProductoSeleccionado
if dinero >= precioProductoSeleccionado:
    print(f"Usuario usted compro el producto {productoSeleccionado} con un valor de {precioProductoSeleccionado}, su cambio es: ${cambio}")
else:
    print(f"Su producto a comprar es {productoSeleccionado} y su precio es {precioProductoSeleccionado}, le falta un total de ${-cambio}")