# -*- coding: utf-8 -*-
import re
import sys



def prog(texto):
    patron = r'(^|[^#])(#{1,3})(.*)\\n'
    ocurrencias = re.findall(patron, texto)
    ret = ""
    if(len(ocurrencias) != 0):
        ocurrencia = ocurrencias[0]
        ret = f"{ocurrencia[2]}"
        for i in range(1, len(ocurrencias)):
            ret += '\n' + ocurrencias[i][2]  
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
