''' Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y 
    lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene 
    <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''
    
def mensaje_datos_personales(nombre, edad, direccion, telefono):
    
    ''' Asigna valores (a las variables) a las claves  que forman el abecedario y crea un mensaje. '''
    
    datosPersonales = {'nombre' : nombre, 'edad' : edad, 'direccion' : direccion, 'telefono' : telefono}
    mensaje = (datosPersonales["nombre"] + " tiene " + datosPersonales["edad"] + " años, vive en " + datosPersonales["direccion"] + " y su numero de telefono es " + datosPersonales["telefono"])
    return mensaje

if __name__ == "__main__":
    #Entrada
    nombre = str(input("Introduzca su nombre: "))
    edad = int(input("Introduzca su edad: "))
    direccion = input("Introduzca su dirección: ")
    telefono = int(input("Introduzca su nº de telefono: "))
    
    #Proceso
    mensaje = mensaje_datos_personales(nombre, edad, direccion, telefono)
    
    #Salida
    print(mensaje)
    
    