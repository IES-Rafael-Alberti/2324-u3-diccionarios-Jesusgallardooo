''' Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes 
    se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro 
    diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente 
    tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una 
    opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar 
    todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el 
    programa tendrá que hacer lo siguiente:

    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    Preguntar por el NIF del cliente y mostrar sus datos.
    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    Terminar el programa.'''
    
if __name__ =="__main__": 
    clientes = {}
    continuar = "1"
    
    while continuar == "1":
        
        print("\n- Menú de opciones:")
        print("\n\t1. Añadir cliente")
        print("\t2. Eliminar cliente")
        print("\t3. Mostrar cliente")
        print("\t4. Listar todos los clientes")
        print("\t5. Listar clientes preferentes ")
        print("\t6. Terminar")
        
        opcion = str(input("\nSeleccione una opción (1/2/3/4/5/6): "))

        if opcion == "1":
            nif = input("Introduzca el NIF del cliente: ")
            nombre = input("Introduzca el nombre del cliente: ")
            direccion = input("Introduzca la dirección del cliente: ")
            telefono = input("Introduzca el telefono del cliente: ")
            correo = input("Introduzca el correo del cliente: ")
            preferente = input("¿Es cliente preferente? \n\t(1)--> Sí. \n\t(2)--> no")
            
            cliente = {'nombre':nombre, 'direccion':direccion, 'telefono':telefono, 'correo':correo, 'preferente':preferente}
            clientes[nif] = cliente
            
            continuar = input("¿Desea continuar? \n\t(1)--> Sí. \n\t(2)--> No.")
            
        elif opcion == "2":
            nif = input("Introduzca el nif del cliente que desea eliminar: ")
            if nif in clientes:
                del clientes[nif]
                mensaje = "Cliente con nif " + str(nif) + " ha sido eliminado"
                continuar = input("¿Desea continuar? \n\t(1)--> Sí. \n\t(2)--> No.")
                
            else:
                mensaje = "El cliente con nif " + str(nif) + " no se encuentra en la base de datos"
                continuar = input("¿Desea continuar? \n\t(1)--> Sí. \n\t(2)--> No.")
        
        elif opcion == "3":
            nif = input("Introduzca el nif del cliente que quiera mostrar: ")
            if nif in clientes:
                cliente = clientes[nif]
                print("Datos del cliente con NIF " + nif + ":")
                for clave, valor in cliente.items():
                    print(clave + ": " + str(valor))
            else:
                mensaje = "El cliente con NIF " + nif + " no se encuentra en la base de datos"
            
            continuar = input("¿Desea continuar? \n\t(1)--> Sí. \n\t(2)--> No.")
            
            
        elif opcion == "4":
            claves = clientes.values()
            print(list(claves))
            
            continuar = input("¿Desea continuar? \n\t(1)--> Sí. \n\t(2)--> No.")
        
        elif opcion == "5":
            for nif, cliente in clientes.items():
                if cliente['preferente'] == "1":
                    print(nif, cliente)
                    
                    
            continuar = input("¿Desea continuar? \n\t(1)--> Sí. \n\t(2)--> No.")
            

        elif opcion == "6":
            print("Fin del programa.")
            continuar = 0
                
            