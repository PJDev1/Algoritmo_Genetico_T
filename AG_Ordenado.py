import random as rnd
import numpy as np
import math
import matplotlib.pyplot as plt

# Definición de funciones
def numeroBits(inf, sup, k):
    return int(math.log2(((sup - inf) * math.pow(10, k)) + 1) + 0.5)

def calcX(a, b, n):
    return [a + dec[i] * ((b - a) / (math.pow(2, n) - 1)) for i in range(tam_poblacion)]

def fitness():
    return [x * math.sin(10 * math.pi * x) + 1 for x in calcX(a, b, t_ind)]

def nSeleccionD():
    return round((1 - r) * tam_poblacion)

def torneo_p(p):
    two_ind = rnd.sample(Fitness, 2)
    gen_prob = np.random.sample()
    j = max(two_ind) if gen_prob < p else min(two_ind)
    l = np.where(Fitness == j)[0][0]
    return l

def cruza():
    punto_cruza = rnd.randint(0, t_ind - 1)
    indexP1 = torneo_p(0.7)
    indexP2 = torneo_p(0.7)
    padre_1 = P[indexP1]
    padre_2 = P[indexP2]
    hijo_1 = np.concatenate([padre_1[:punto_cruza], padre_2[punto_cruza:]])
    hijo_2 = np.concatenate([padre_2[:punto_cruza], padre_1[punto_cruza:]])
    hijos = np.array((hijo_1, hijo_2))
    return hijos

def mutacion():
    randInd = rnd.choice(poblacionNueva)
    bitMuta = rnd.randint(0, t_ind - 1)
    if randInd[bitMuta] == 0:
        randInd[bitMuta] = 1
    else:
        randInd[bitMuta] = 0

# Parámetros de entrada
tam_poblacion = int(input("Tam poblacion: "))
precision = int(input("Digitos de precisión: "))  # k
print("Intervalo de busqueda ")
a = float(input('a='))
b = float(input('b='))
r = float(input('Porcentaje de cruza(decimal): '))
m = float(input('Porcentaje de muta(decimal): '))
threshold = int(input('Ingrese n iteraciones: '))
fitnessPromedio = np.empty((0, threshold))

# Cálculo del tamaño de los individuos (n bits)
t_ind = int(numeroBits(a, b, precision))

# Población inicial aleatoria
P = np.random.randint(2, size=(tam_poblacion, t_ind))

# Parámetros de cruce y mutación
cross_r = round((r * tam_poblacion) / 2)
mut_i = round((m * tam_poblacion))

#Ciclar Algoritmo

contador = 1
while  contador <= threshold:
    dec = np.zeros(tam_poblacion)
    for i in range(tam_poblacion):
        dec[i] = int("".join(str(x) for x in P[i]), 2)

    Fitness = np.zeros(tam_poblacion)
    Fitness = fitness()
    
    poblacionNueva = np.empty((0, t_ind), dtype=int)
    n_pase_directo = nSeleccionD()
    for i in range(cross_r):
        parHijos = cruza()
        poblacionNueva = np.append(poblacionNueva, parHijos, axis=0)

    i = 1
    
    while (i <= n_pase_directo):
        rand_ind = rnd.choice(P)
        poblacionNueva = np.append(poblacionNueva, rand_ind.reshape(1, -1), axis=0)
        i += 1

    for _ in range(mut_i):
        mutacion()
        
    promedio = np.mean(Fitness)
    fitnessPromedio = np.append(fitnessPromedio, promedio)
    P = poblacionNueva

    contador += 1

# --------------> Graficación <--------------------
r *= 100
m *= 100
plt.plot(fitnessPromedio)
plt.title(f'Tamaño de la poblacion = {len(P)} Porcentaje de cruza {r}% Porcentaje de muta = {m}')
plt.xlabel("Número de Iteraciones")
plt.ylabel("Promedio Fitness")
plt.show()