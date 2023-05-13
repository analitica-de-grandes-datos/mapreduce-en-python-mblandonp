import sys 
 
if __name__ == '__main__': 
 
    curkey = None 
    total = 0 
 
    for line in sys.stdin: 
 
        key, valor = line.split("\t") 
        valor = valor.strip() 
 
        if key == curkey: 
            # 
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma 
            # clave. 
            # 
            numeros = numeros + ',' + str(int(valor)) 
        else: 
            # 
            # Se cambio de clave. Se reinicia el acumulador. 
            # 
            if curkey is not None: 
                # 
                sys.stdout.write("{}\t{}\n".format(curkey, numeros)) 
 
            curkey = key 
            numeros = str(int(valor)) 
 
    sys.stdout.write("{}\t{}\n".format(curkey, numeros))