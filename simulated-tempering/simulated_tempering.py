import random
import math

problema=dict([("A",["B","C","D","E","H"]), ("B",["A","C","G","H"]), 
               ("C",["A","B","D","G"]), ("D",["A","C","E","F"]), 
               ("E",["A","D","F","H"]), ("F",["D","E"]),
               ("G",["B","C","H"]), ("H",["A","B","E","G"]) ])

valores=dict([("A",3), ("B",1), ("C",5), ("D",8), ("E",10), ("F",12), ("G",7), ("H",5)])
# Hay 2 E que se repiten en el documento asi que cambie la E que tiene valor de 5 por una H

def f(estado):
    return valores[estado]

def vecindad(estado):
    return problema[estado]

def simulated_tempering(tini, tfin, alpha, ini, f, vecindad):
    t = tini
    actual = ini
    mejor = None
    fmejor = -10
    t_mejor = t

    while t >= tfin:
        vecinos = vecindad(actual)
        nuevo = max(vecinos, key=f)

        if f(nuevo) > f(actual):
            actual = nuevo
        else:
            r = random.random()
            p = math.exp((f(nuevo) - f(actual)) / t)
            if r < p:
                actual = nuevo

        if f(actual) > fmejor:
            mejor = actual
            fmejor = f(actual)
            t_mejor = t

        print(f"Temperatura: {t:.2f}, Estado Actual: {actual}, Valor: {f(actual)}")

        t *= alpha
    return mejor, t_mejor

if __name__ == "__main__":
    tini = 100
    tfin = 1
    alpha = random.random()
    ini = None
    ini = input("Ingresa el estado de inicio: ")
    mejor_estado, temp_mejor_estado = simulated_tempering(tini, tfin, alpha, ini, f, vecindad)
    print(f"El mejor estado encontrado es: {mejor_estado} con un valor de: {f(mejor_estado)}")
    print(f"El mejor estado se encontró a una temperatura de: {temp_mejor_estado:.2f}")
