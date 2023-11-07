''' Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
    pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de 
    ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje 
    informando de ello.'''
    

def calcular_precio_frutas(fruta, cantidad, preciosFrutas):
    if fruta in preciosFrutas:
        precio = cantidad * preciosFrutas[fruta]
    else:
        fruta not in preciosFrutas
        precio = 0
    return precio

if __name__ =="__main__":
    #Entrada
    fruta = str(input("Introduzca qué fruta quiere comprar: "))
    cantidad = float(input("Introduzca la cantidad en kg:"))
    preciosFrutas = {'platano' : 1.35, 'manzana' : 0.80, 'pera' : 0.85, 'naranja' : 0.70}
    
    #Proceso
    precio = calcular_precio_frutas(fruta, cantidad, preciosFrutas)
    
    #Salida
    if precio != 0:
        print("El precio de " + str(cantidad) +  " kilos de " + fruta + " equivale a --> " + str(precio) + "€")
    else:
        print("La fruta introducida (" + fruta + ") no se encuentra en existencia. ")