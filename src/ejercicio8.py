''' Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá 
    las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados 
    por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá 
    una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no 
    está en el diccionario debe dejarla sin traducir.'''
    
    
def separar_palabra_traduccion(palabras):
    palabra,traduccion = palabras.split(":")
    return palabra,traduccion

def dividir_palabras_frase(fraseEspañol):
    dividirFrase = fraseEspañol.split()
    return dividirFrase

if __name__ == "__main__":
    #Entrada
    traducciones = {}
    palabrasATraducir = str(input("Introduzca las palabras en formato[p.español:traducciónAlInglés, p.español2:traducciónAlInglés2...]: \n\n"))
    dividirTraducciones = palabrasATraducir.split(", ") #divide los caracteres a los lados de ", "
    
    #Proceso
    for palabras in dividirTraducciones:
        palabra, traduccion = separar_palabra_traduccion(palabras) #Divide las palabras a los lados de ":"
        traducciones[palabra] = traduccion #Guarda cada palabra con su traducción en el diccionario traducciones.
    
    #Entrada
    fraseEspañol = str(input("Introduzca una frase en español: "))
    
    dividirFrase = dividir_palabras_frase(fraseEspañol) #divide las palabras de la frase introducida en español.
    traduccionIngles = [] #lista vacía para almacenar la traducción. 
    
    for palabra in dividirFrase:
        traduccion = traducciones.get(palabra, dividirFrase)
        traduccionIngles.append(traduccion) #Añade cada palabra traducida a la lista
        
    fraseTraducida = " ".join(traduccionIngles) #Concatena todos los elemenetos de una lista con " " entre ellos.
    
    #Salida
    print("Tu frase traducida al inglés significa: \n \t" + fraseTraducida)