# -*- coding: utf-8 -*-
import re
import sys

# DIFERENTES ENTRADAS Y SALIDA VALIDA

 #   SIN SECUENCIA DE CIERRE

 #   #texto por <h1>texto</h1>
 #   ##texto por <h2>texto</h2>
 #   ###texto por <h3>texto</h3>

  #   CON SECUENCIA DE CIERRE

  #   **texto** por <strong>texto</strong>
  #   *texto* por <em>texto<em/>
  #   ~~texto~~ por <s>texto</s>

def prog(texto):
  ret = re.sub(r'###(.*)\\n', lambda x: x.group(0).replace('###', '<h3>', 1).replace('\\n', '</h3>\\n', 1), texto)
  ret = re.sub(r'##(.*)\\n', lambda x: x.group(0).replace('##', '<h2>', 1).replace('\\n', '</h2>\\n', 1), ret)
  ret = re.sub(r'#(.*)\\n', lambda x: x.group(0).replace('#', '<h1>', 1).replace('\\n', '</h1>\\n', 1), ret)
  ret = re.sub(r'~~(.*)~~', lambda x: x.group(0).replace('~~', '<s>', 1).replace('~~', '</s>', 1), ret)
  ret = re.sub(r'\*\*(.*)\*\*', lambda x: x.group(0).replace('**', '<strong>', 1).replace('**', '</strong>', 1), ret)
  ret = re.sub(r'\*(.*)\*', lambda x: x.group(0).replace('*', '<em>', 1).replace('*', '</em>', 1), ret)

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
