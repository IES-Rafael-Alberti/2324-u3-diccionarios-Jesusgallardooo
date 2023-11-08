''' Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
    pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en 
    el diccionario.'''
    
def detectar_simbolo_divisa(monedas, divisa):
    
    ''' Si divisa está en monedas, devuelve el simbolo, si no, devuelve 0 e informa que no se encuentra.'''
    
    if divisa in monedas:
        simbolo = monedas[divisa]
    else:
        divisa not in monedas
        simbolo = 0
    return simbolo

if __name__ == "__main__":
    #Entrada
    monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa = input("Introduzca de qué divisa desea conocer el símbolo: ")
    
    #Proceso
    simbolo = detectar_simbolo_divisa(monedas, divisa)
    
    #Salida
    if simbolo != 0:
        print("El síimbolo del " + divisa + " es --> " + simbolo)
    else:
        print(divisa + " no se encuentra en el diccionario. ")
     
    