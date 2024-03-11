from time import localtime
import datetime
def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    t = localtime()
    dia_actual = t.tm_mday
    mes_actual = t.tm_mon
    anno_actual = t.tm_year
    edad = anno_actual - anno 
    if (datetime.datetime(anno,mes,dia)>datetime.datetime(anno_actual,mes_actual,dia_actual)):
        respuesta="Fecha de nacimiento inválida"
    
    else:
        if mes_actual <= mes and dia_actual < dia:
            edad -= 1
        respuesta = "Usted tiene "+ str(edad)+ " años"
    
    return respuesta

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
