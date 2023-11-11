''' Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
    preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
    Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato'''
    

def lista_de_compra(cestaCompra):
    ''' Pregunta por los productos que se desea comprar y los almacena
        en el diccionario CestaCompra, hasta que quiera dejar de comprar'''
        
    seguirComprando = 1
    while seguirComprando == 1:
        producto = str(input("Introduzca qué producto desea comprar: "))
        precioProducto = float(input("Introduzca el precio del producto: "))
        cestaCompra[producto] = precioProducto
        seguirComprando = int(input("¿Seguir comprando?\n --> 1 = Sí \n --> 2 = No \n --> "))

def calcular_precio(cestaCompra):
    
    ''' Calcula el precio total de los productos comprados.'''
    
    precioTotal = sum(cestaCompra.values())
    return precioTotal

if __name__ == "__main__":
    # Entrada
    cestaCompra = {}

    # Proceso
    lista_de_compra(cestaCompra)

    # Salida
    for producto in cestaCompra.keys():
        print(producto)

    precioTotal = calcular_precio(cestaCompra)

    print("Precio total: " + str(precioTotal) + "€")
