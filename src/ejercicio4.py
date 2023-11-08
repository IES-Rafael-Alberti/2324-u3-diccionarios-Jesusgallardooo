''' Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla 
    la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.'''
    
def filtrar_dia(fecha):
    
    ''' encuentra la primera / y devuelve lo anterior a ella(día). '''
    
    dia = fecha[:fecha.find('/')]
    return dia


def filtrar_mes(fecha):
    
    ''' Encuentra la posicion de la primera / y almacena lo que posterior (mes/año). 
        Luego encuentra la "segunda" / y devuelve lo anterior(mes). Devuelve '''
    
    MesDelAño = fecha[fecha.find('/')+1:]
    mes = MesDelAño[:MesDelAño.find('/')]
    return MesDelAño,mes

def filtrar_año(MesDelAño):
    
    ''' Encuentra la posición de la "segunda" / (mes/año), y devuelve lo posterior (año)'''
    
    año = MesDelAño[MesDelAño.find('/')+1:]
    return año

if __name__ == "__main__":
    #Entrada
    fecha = str(input("Introduzca una fecha en formato (dd/mm/aaaa): "))
    mesesDelAño = {'01':'enero', '02':'febrero', '03':'marzo', '04':'abril', '05':'mayo','06':'junio', '07':'julio', '08':'agosto', '09':'septiembre','10':'octubre', '11':'noviembre', '12':'diciembre' }
    
    #Proceso
    dia = filtrar_dia(fecha)
    MesDelAño, mes = filtrar_mes(fecha)
    año = filtrar_año(MesDelAño)
    
    #Salida
    print("fecha introducida --> " + str(dia) + " de " + mesesDelAño[mes] + " de " + str(año))
    