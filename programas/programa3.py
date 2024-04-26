import re
import sys

meses = {
    "01" : "enero",
    "02" : "febrero",
    "03" : "marzo",
    "04" : "abril",
    "05" : "mayo",
    "06" : "junio",
    "07" : "julio",
    "08" : "agosto",
    "09" : "septiembre",
    "10" : "octubre",
    "11" : "noviembre",
    "12" : "diciembre"
}
 
def prog(texto):
    match = re.findall(r'"timestamp": "T (\d+):(\d+):(\d+) (\d+):(\d+)', texto)
    fecha = match[0]
    anio = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    hora = fecha[3]
    min = fecha[4]
    ret = f"{dia} de {meses[mes]} del {anio} a las {hora}:{min} hs."
    for i in range(1, len(match)):
        fecha = match[i]
        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2]
        hora = fecha[3]
        min = fecha[4]
        ret = ret + f"\n{dia} de {meses[mes]} del {anio} a las {hora}:{min} hs."
    return ret

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
