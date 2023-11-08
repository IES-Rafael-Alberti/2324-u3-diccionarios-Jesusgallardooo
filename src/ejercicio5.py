''' Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
    {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
    asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una 
    de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número 
    total de créditos del curso.'''


def detectar_y_sumar_creditos(creditos, sumaCreditos):
    
    ''' Conoce cuántos créditos tiene cada asignatura, mostrando un mensaje informativo de cada 
        una de ellas, y devuelve la suma de los créditos de todas las asignaturas. '''
    
    for asignatura, creditos in creditos.items():
        print(asignatura + " tiene " + str(creditos) + " creditos.")
        sumaCreditos = sumaCreditos + creditos
    return sumaCreditos

if __name__ == "__main__":
    #Entrada
    creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    sumaCreditos = 0
    
    #Proceso
    sumaCreditos = detectar_y_sumar_creditos(creditos, sumaCreditos)
    
    #Salida
    print("El total de creditos es --> " + str(sumaCreditos))