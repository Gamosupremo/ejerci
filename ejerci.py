import random


def punto_aleatorio():
    return (random.random(),random.random())


def esta_dentro(punto):
    return (punto[0]**2 + punto[1]**2)<1


def puntos_dentro_y_fuera(puntos):
    p=[esta_dentro(punto_aleatorio()) for i in range(puntos)]
    return p.count(True),p.count(False)

def calcular_pi(n):
    a=puntos_dentro_y_fuera(n)
    return 4* (a[0]/n)


def calcular_pis(n):
    pis=[]
    for i in (n):
        a=puntos_dentro_y_fuera(i)
        pi=4 * (a[0]/i)
        pis.append(pi)
    return pis

print(calcular_pis([10,100,1000,10000,100000]))

