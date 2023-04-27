import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except:
            print("Error: Numero no valido")
        else:
            if valor >= ini and valor <= fin:
                break
    return valor

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos numeros quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Como quieres redondear los numeros? [1]Al alza [2]A la baja [3]Normal: ")
    listado_numeros = [random.uniform(0, 100) for i in range(numeros)]
    lista_redondear = []
    for i in listado_numeros:
        if modo == 1:
            lista_redondear.append(math.ceil(i))
        elif modo == 2:
            lista_redondear.append(math.floor(i))
        elif modo == 3:
            lista_redondear.append(round(i))
    print("Lista original: ", listado_numeros)
    print("Lista redondeada: ", lista_redondear)

if __name__ == "__main__":
    generador()


