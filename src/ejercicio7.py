''' Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
    preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
    Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato'''
    

def lista_de_compra(cestaCompra, seguirComprando):
    while seguirComprando == 1:
        producto = str(input("Introduzca qué producto desea compar: "))
        precioProducto = float(input("Introduzca el precio del producto: "))
        cestaCompra[producto] = precioProducto
        seguirComprando = int(input("¿Seguir comprando?\n --> 1 = Sí \n --> 2 = No \n --> "))
    return cestaCompra

def calcular_precio(cestaCompra):
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
    
    #Salida
    for producto in cestaCompra.keys():
        print(producto)
        
    precioTotal = calcular_precio(cestaCompra)
    
    print( "Precio total: " + str(precioTotal) + "€")
    
