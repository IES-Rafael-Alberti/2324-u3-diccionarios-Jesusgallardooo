''' Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
    (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez 
    que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''


def nombrar_dato():
    dato = str(input("Introduzca qué dato desea almacenar: "))
    return dato

def introducir_valor_dato(dato):
    valorDato = input("Introduzca el valor de su " + dato + ":")
    return valorDato

def guardar_dato(datosPersonales, dato, valorDato):
    datosPersonales[dato] = valorDato

if __name__ == "__main__":
    #Entrada
    datosPersonales = {}
    numDatos = int(input("Introduzca el nº de datos que desea guardar en el diccionario: "))
    
    #Proceso
    for i in range(numDatos):
        
        dato = nombrar_dato()
        
        valorDato = introducir_valor_dato(dato) 
        
        guardar_dato(datosPersonales, dato, valorDato)
        
    #Salida
        for dato, valorDato in datosPersonales.items():
            print(dato + ":" + str(valorDato))