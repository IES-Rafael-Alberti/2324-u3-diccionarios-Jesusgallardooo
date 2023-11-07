''' Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla 
    la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.'''
    
def separar_dia(fecha):
    dia = fecha[:fecha.find('/')]
    return dia

def separar_mes(fecha):
    MesDelAño = fecha[fecha.find('/')+1:]
    mes = MesDelAño[:MesDelAño.find('/')]
    return MesDelAño,mes

def separar_año(MesDelAño):
    año = MesDelAño[MesDelAño.find('/')+1:]
    return año

if __name__ =="__main__":
    #Entrada
    fecha = str(input("Introduzca una fecha en formato (dd/mm/aaaa): "))
    mesesDelAño = {'01':'enero', '02':'febrero', '03':'marzo', '04':'abril', '05':'mayo','06':'junio', '07':'julio', '08':'agosto', '09':'septiembre','10':'octubre', '11':'noviembre', '12':'diciembre' }
    
    #Proceso
    dia = separar_dia(fecha)
    MesDelAño, mes = separar_mes(fecha)
    año = separar_año(MesDelAño)
    
    #Salida
    print("fecha introducida --> " + str(dia) + " de " + mesesDelAño[mes] + " de " + str(año))
    