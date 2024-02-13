import struct
import random as rnd 
import numpy as np
import math

#Poblacion(tam,precision)
tam_poblacion = int(input("Tam poblacion: "))
precision = int(input("Digitos de precisión: ")) #k
r = float(input('Porcentaje de cruza: '))
print("Intervalo de busqueda ")
a = float(input('a='))
b = float(input('b='))

#Definicion de tamaño de los individuos (n bits)
def numeroBits(inf, sup, k):
    return (math.log2(((sup-inf)*math.pow(10, k))+1))

t_ind= int(numeroBits(a,b,precision)+0.5)

#Poblacion inicial aleatoriamente
P = np.random.randint(2, size=(tam_poblacion,t_ind))

print(f'P={P}')
#Convertir a decimal
dec = np.zeros(tam_poblacion) #Creamos arreglo de ceros

#Llenado del array de zeros
for i in range(tam_poblacion):
    dec[i] = int("".join(str(x) for x in P[i]),2)

#Calculamos x
def calcX(a, b, n): #n = tam_individuo
    return [a + dec[i]*((b-a)/(math.pow(2, n)-1)) for i in range(tam_poblacion)]

#Calculamos fitness
def fitness():
    return [x*math.sin(10*math.pi*x)+1 for x in calcX(a, b, t_ind)]


Fitness = np.zeros(tam_poblacion)
Fitness = fitness()
def torneo_p(p):
    #seleccionar 2 individuos
    two_ind = rnd.sample(Fitness, 2)
    gen_prob = np.random.sample()
    j = max(two_ind) if gen_prob < p else min(two_ind) 
    l = np.where(Fitness==j)[0][0]
    return l

#r(pares de cruza)
cross_r = round((r*tam_poblacion)/2)

#Repetir torneo hasta llenar los individuos deseados
_torlist = np.empty(tam_poblacion)
for i in range(tam_poblacion):
    selElem = Fitness[torneo_p(0.7)]
    _torlist[i] = selElem


print(_torlist)

#Cruza
def onePointCross():
    poblacionNueva = []
    for _ in range(cross_r):
        punto_cruza = rnd.randint(1, t_ind - 1)
        print(t_ind,punto_cruza)
        indexP1 = torneo_prueba(0.7)
        indexP2 = torneo_prueba(0.7)
        hijo_1 = P[indexP1][:punto_cruza] + P[indexP2][punto_cruza:]
        hijo_2 = P[indexP2][:punto_cruza] + P[indexP1][punto_cruza:]
        poblacionNueva.extend([hijo_1, hijo_2])
        print(poblacionNueva)
        
onePointCross()
#Mutacion