# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    aux =  sorted(set(re.findall(r'@(\w+)', texto)), key=lambda x: texto.index('@'+x))
    if len(aux) > 0:
        ret = aux[0]
        for i in range(1,len(aux)):
            ret += '\n' + aux[i] 
        return ret
    else:
        return ""


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
