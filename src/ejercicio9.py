''' Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán 
    en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
    El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea 
    añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea 
    pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación 
    el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.'''
    
    
    
def calcular_pago_pendiente(facturas, cantidadPendiente, cantidadCobrada, numFactura):
    cantidadPendiente = cantidadPendiente + facturas[numFactura]
    return cantidadPendiente,cantidadCobrada

def calcular_cobro_hecho(cantidadPendiente, cantidadCobrada, precioFactura):
    cantidadCobrada = cantidadCobrada + precioFactura
    cantidadPendiente = cantidadPendiente - precioFactura
    return cantidadPendiente,cantidadCobrada

def eliminar_factura_de_diccionario(facturas, numFactura):
    facturas.pop(numFactura)


if __name__ == "__main__":
    
    facturas = {}
    terminar = 1
    cantidadPendiente = 0
    cantidadCobrada = 0
    
    
    while terminar == 1:

        #Entrada
        eleccion = int(input("¿Qué acción deseas realizar? \n\t (1)--> Añadir nueva factura. \n\t (2)--> Pagar factura existente.\n"))
        if eleccion == 1:
            #Entrada
            print("NUEVA FACTURA: ")
            precioFactura = int(input("\t Introduzca el coste de la factura: "))
            numFactura = input("\t Introduzca el nº de factura: ")
            
            #Proceso
            facturas[numFactura] = precioFactura
            cantidadPendiente, cantidadCobrada = calcular_pago_pendiente(facturas, cantidadPendiente, cantidadCobrada, numFactura)
            
        else:
            #Entrada
            print("COBRO FACTURA: ")
            numFactura = input("\tIntroduzca el nº de la factura que desea pagar: ")
            
            #Proceso
            eliminar_factura_de_diccionario(facturas, numFactura)
            cantidadPendiente, cantidadCobrada = calcular_cobro_hecho(cantidadPendiente, cantidadCobrada, precioFactura)
            
        #Salida
        print("Cantidad pendiente de cobro: " + str(cantidadPendiente))
        print("Cantidad cobrada hasta el momento: " + str(cantidadCobrada))
        
        #Entrada
        terminar = int(input("\n ¿Desea continuar? \n\t(1)--> Sí \n\t(2)--> No\n"))