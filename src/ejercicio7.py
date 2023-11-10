''' Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
    preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
    Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato'''
    

def lista_de_compra(cestaCompra, seguirComprando):
    ''' Pregunta por los productos que se desea comprar y los almacena
        en el diccionario CestaCompra.'''
    while seguirComprando == 1:
        producto = str(input("Introduzca qué producto desea compar: "))
        precioProducto = float(input("Introduzca el precio del producto: "))
        cestaCompra[producto] = precioProducto
    return cestaCompra

def calcular_precio(cestaCompra):
    ''' Calcula el precio total de los produtos compraados.'''
    precioTotal = 0
    for precio in cestaCompra.values():
        precioTotal = precioTotal + precio
    return precioTotal

if __name__ == "__main__":
    #Entrada
    cestaCompra = {}
    seguirComprando = 1
    
    #Proceso
    lista_de_compra(cestaCompra, seguirComprando)
    seguirComprando = int(input("¿Seguir comprando?\n --> 1 = Sí \n --> 2 = No \n --> "))

    
    #Salida
    for producto in cestaCompra.keys():
        print(producto)
        
    precioTotal = calcular_precio(cestaCompra)
    
    print( "Precio total: " + str(precioTotal) + "€")
    
