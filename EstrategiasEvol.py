import random as rnd
import numpy as np
import math 
import matplotlib.pyplot as plt

def fitness(x,y):
    return ((1-x)**2)*np.exp((-x**2)-(y+1)**2)-(x-x**3-y**3)*np.exp(-x**2-y**2)

def genPop(a,b):
    poblacion = []
    for _ in range(μ):
        x = rnd.uniform(a,b)
        y = rnd.uniform(a,b)
        poblacion.extend([[[x,y],[d_1,d_2]]])
    return poblacion

def mutacion():
    rand_ind = rnd.choice(P)
    x = rand_ind[0][0]
    y = rand_ind[0][1]
    random_normal = rnd.gauss(0,d_1)
    new_x = x + random_normal
    new_y = y + random_normal
    if(new_x < a):
        new_x = a
        rand_ind[0][0] = new_x
        
    elif(new_x > b):
        new_x = b
        rand_ind[0][0] = new_x
        
    if(new_y < a):
        new_y = a
        rand_ind[0][1] = new_y
    elif(new_y > b):
        new_y = b
        rand_ind[0][1] = new_y
        
    print(rand_ind)
    return rand_ind

    
μ = int(input("μ: "))
λ = int(input("λ: "))
r = float(input("r: "))
m = 1 - r
print(f'm: {m}')
choose_cross = round(r * λ)
choose_mut = round(m * λ)
d_1 = 1
d_2 = 1
print("Intervalo de busqueda: ")
a = int(input("a: "))
b = int(input("b: "))
threshold = int(input("Iteraciones: "))
fitnessPromedio = []

P = genPop(a,b)

contador = 0
while contador < threshold:
    Fitness = []
    for individuo in P:
        x = individuo[0][0]
        y = individuo[0][1]
        val_fitness = fitness(x,y)
        Fitness.append(val_fitness)
            
    #print(f'Lista_Fitness: {Fitness}')
    print(f'\nTamaño de Poblacion Inicial: {len(P)}')
    print(f'\nPoblacion inicial: {P}')
    P_λ = P
    print(f'Tamaño de Poblacion_λ: {len(P_λ)}')
    print(f'Nueva población antes de agregar ind mutados: \n{P_λ}')
    
    for _ in range(choose_mut):
        P_λ.append(mutacion())
    print(f'\nNueva Población con ind mutados: \n{P_λ}')
    print(f'\nTamaño de Poblacion_λ con ind mutados: {len(P_λ)}')

    for individuo in P_λ:
        x = individuo[0][0]
        y = individuo[0][1]
        val_fitness = fitness(x,y)
        if not val_fitness in Fitness:
            Fitness.append(val_fitness)
            
    #print(f'\nLista_Fitness_Update: {sorted(Fitness)}')
    
    for _ in range(choose_mut):
        worst_index = Fitness.index(min(Fitness))
        print(f'index_peor_ind: {worst_index}')
        print(f'Elemento de P eliminado: {P_λ[worst_index]}')
        print(f'Elemento de Fitness eliminado: {Fitness[worst_index]}')
        del P_λ[worst_index]
        del Fitness[worst_index]

    #print(f'New_Fitness: {Fitness}')
    #print(f'New_Pop: {P_λ}')
    
    promedio = np.mean(Fitness)
    #print(f'{contador}.-Promedio de fitness: {promedio}')
    fitnessPromedio.append(promedio)
    P = P_λ

    contador += 1

# ---------------------------------------------------------------------------------------------
r *= 100
m *= 100
plt.plot(fitnessPromedio)
plt.title(f'Tamaño de la poblacion = {μ} Porcentaje de cruza {r}% Porcentaje de muta = {m}%', fontsize = 10)
plt.xlabel("Número de Iteraciones")
plt.ylabel("Promedio Fitness")
plt.show()

