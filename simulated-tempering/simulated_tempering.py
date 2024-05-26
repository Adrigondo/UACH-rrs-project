import random
import math

problema=dict([("A",["B","C","D","E","H"]), ("B",["A","C","G","H"]), 
               ("C",["A","B","D","G"]), ("D",["A","C","E","F"]), 
               ("E",["A","D","F","H"]), ("F",["D","E"]),
               ("G",["B","C","H"]), ("H",["A","B","E","G"]) ])
valores=dict([("A",3), ("B",1), ("C",5), ("D",8), ("E",10), ("F",12), ("G",7), ("H",5)])

def siguiente(actual,T,opti,fopti,prob,valores):
    hijos = prob[actual]
    total = len(hijos)
    ind = round(total*(1-random.random()))
    if ind == 0:
        ind = 1
    nuevo = hijos[ind - 1]
    fnuevo = valores[nuevo]
    if fnuevo < fopti:
        opti = nuevo
        fopti = fnuevo
    else:
        delta = fnuevo - fopti
        proba = math.exp(-delta/T)
        nume = random.random()
        if nume > proba:
            opti = nuevo
            fopti = fnuevo
    return nuevo,opti,fopti

def temSim(ini, prob, valores):
    T = 30
    actual = ini
    tfin = 2
    mejor = None
    fmejor = float('inf')
    while T > tfin:
        actual,mejor,fmejor = siguiente(actual,T,mejor,fmejor,prob,valores)
        T = T * 0.25
    return mejor

def main(problema, valores):
    print("Busqueda por templado simulado")
    print("Indique el estado de inicio")
    ini = input().upper()
    mejor = temSim(ini,problema,valores)
    print("El mejor estado encontrado es " + mejor)

main(problema,valores)
