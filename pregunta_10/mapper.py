#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/ python3

#
# Esta es la funcion que mapea la entrada a parejas (clave, valor)
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
        clave, valor = line.split('\t') 
        valor =list(valor.strip().split(',')) 
        clave = clave.zfill(4) 
        
            
            #
            # escribe al flujo estandar de salida
            #
        for letra in valor: 
            sys.stdout.write("{}\t{}\n".format(letra ,clave))
 
