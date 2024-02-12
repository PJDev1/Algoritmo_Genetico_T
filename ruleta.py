import random as rnd 
import numpy as np
import math

#Poblacion(tam,precision)
tam_poblacion = int(input("Tam poblacion: "))
precision = int(input("Digitos de precisión: ")) #k
n_indtor = int(input("Individuos que pasan por torneo: ")) 
print("Intervalo de busqueda ")
a = float(input('a='))
b = float(input('b='))

#Definicion de tamaño de los individuos (n bits)
def numeroBits(inf, sup, k):
    return (math.log2(((sup-inf)*math.pow(10, k))+1))

t_ind= int(numeroBits(a,b,precision)+0.5)

#Poblacion inicial aleatoriamente
P = np.random.randint(2, size=(tam_poblacion,t_ind))

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
def torneo_p(p): #K=¿Cuantos? p = probabilidad
    #seleccionar 2 individuos
    two_ind = rnd.sample(Fitness, 2)
    gen_prob = np.random.sample()
    j = max(two_ind) if gen_prob < p else min(two_ind) 
    l = np.where(Fitness==j)[0][0]
    print(l)
    return l

#Repetir torneo hasta llenar los individuos deseados
_torlist = np.empty(n_indtor)
for i in range(n_indtor):
    selElem = Fitness[torneo_p(0.7)]
    _torlist[i] = selElem

def cruza():
    
    



#Cruza 
#Mutacion
