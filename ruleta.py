import random as rnd 
import numpy as np
import math
import matplotlib.pyplot as plt


#Poblacion(tam,precision)
tam_poblacion = int(input("Tam poblacion: "))
precision = int(input("Digitos de precisión: ")) #k
print("Intervalo de busqueda ")
a = float(input('a='))
b = float(input('b='))
r = float(input('Porcentaje de cruza(decimal): ')) 
m = float(input('Porcentaje de muta(decimal): '))
threshold = int(input('Ingrese n iteraciones: ')) 

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

def nSeleccionD():
    return round((1-r)*tam_poblacion)

Fitness = np.zeros(tam_poblacion)
Fitness = fitness()
print(Fitness)
def torneo_p(p):
    #seleccionar 2 individuos
    two_ind = rnd.sample(Fitness, 2)
    gen_prob = np.random.sample()
    j = max(two_ind) if gen_prob < p else min(two_ind) 
    l = np.where(Fitness==j)[0][0]
    return l

#r(pares de cruza)
cross_r = round((r*tam_poblacion)/2) #Indica cuantos pares NECESITO
print(f'Necesito: {cross_r} par') #2

mut_i = round((m*tam_poblacion))
print(f'NInd a mutar: {mut_i}')
#Cruza
def cruza():
    punto_cruza = rnd.randint(0, t_ind-1)
    indexP1 = torneo_p(0.7)
    indexP2 = torneo_p(0.7)
    #Padres
    padre_1 = P[indexP1]
    padre_2 = P[indexP2]
    hijo_1 = np.concatenate([padre_1[:punto_cruza], padre_2[punto_cruza:]])
    hijo_2 = np.concatenate([padre_2[:punto_cruza], padre_1[punto_cruza:]])
    hijos = np.array((hijo_1,hijo_2))
    return hijos


#Sacamos los n hijos necesarios y los metemos a la nueva poblacion
poblacionNueva = np.empty((0,t_ind), dtype=int)
n_pase_directo = nSeleccionD()
for i in range(cross_r):
    parHijos = cruza() #Arreglo con 2 arreglos dentro
    poblacionNueva = np.append(poblacionNueva, parHijos, axis=0)
    
print(f'NewP_array: \n{poblacionNueva}')


i = 1
while( i != n_pase_directo):
    rand_ind = rnd.choice(P)
    print(f'Nuevo individuo = ',rand_ind)
    poblacionNueva = np.append(poblacionNueva, rand_ind.reshape(1, -1), axis=0)
    i+=1

print(f'len({len(poblacionNueva)})')

#Mutacion
def mutacion():
    randInd = rnd.choice(poblacionNueva) #Seleccion de individuo de forma aleatoria de la poblacion
    print(f'Individuo a mutar = {randInd}')
    bitMuta = rnd.randint(0, t_ind - 1)
    if randInd[bitMuta] == 0:
        randInd[bitMuta] = 1
    else:
        randInd[bitMuta] = 0
    print("Individuo mutado: ", randInd)
       
for _ in range(mut_i):
    mutacion()

#while (max(Fitness) < threshold):