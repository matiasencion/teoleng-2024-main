# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    aux = [] 
    aux1 =  sorted(set(re.findall(r'"user": "(\w+)"', texto)), key=lambda x: texto.index(''+x))
    for i in aux1:
        aux.append(re.findall(r'"user": "({})"'.format(i), texto))  
    k = aux[0]
    ret = k[0] + ': ' + f'{len(k)}'
    print(aux)
    for j in range(1, len(aux)):
        res = aux[j]
        ret += '\n' + res[0] + ': ' + f'{len(res)}' 
    return ret

    
if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
