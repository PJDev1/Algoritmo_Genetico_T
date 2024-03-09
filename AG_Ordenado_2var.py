import random as rnd
import numpy as np
import math
import matplotlib.pyplot as plt

# Definición de funciones
def numeroBits(inf, sup, k):
    return int(math.log2(((sup - inf) * math.pow(10, k)) + 1) + 0.5)

def calcXv1(a, b, n):
    return [a + decimales1var_()[i] * ((b - a) / (math.pow(2, n) - 1)) for i in range(tam_poblacion)]

def calcX(a, b, n):
    return [a + decimales2var_(True)[i] * ((b - a) / (math.pow(2, n) - 1)) for i in range(tam_poblacion)]

def calcY(a, b, n):
    return [a + decimales2var_(False)[i] * ((b - a) / (math.pow(2, n) - 1)) for i in range(tam_poblacion)]

def decimales2var_(var):
        dec_x = np.zeros(tam_poblacion)
        dec_y = np.zeros(tam_poblacion)
        
        for i in range(tam_poblacion):
            dec_x[i] = int("".join(str(x) for x in P[i][:t_ind_x]), 2) #x
            dec_y[i] = int("".join(str(y) for y in P[i][t_ind_y:]), 2) #y
            
        
        if(var == True):
            return dec_x
        elif(var == False):
            return dec_y
        
def decimales1var_():
    dec = np.zeros(tam_poblacion)
    for i in range(tam_poblacion):
        dec[i] = int("".join(str(x) for x in P[i]), 2)
    return dec

def fitness_xy(opcion,k):
    PoblacionFitness = []
    if(opcion == 1):
         return [x * math.sin(10 * math.pi * x) + 1 for x in calcXv1(a, b, t_ind)]
    elif(opcion == 2):
        x_form_vals = calcX(ax,bx,t_ind_x)
        y_form_vals = calcY(ay,by,t_ind_y)
        for x,y in zip(x_form_vals, y_form_vals):
            function = 21.5 + x * np.sin(4 * np.pi * x) + y * np.sin(20 * np.pi * y)
            PoblacionFitness.append(function)
        return PoblacionFitness
    elif(opcion == 3):
        x_form_vals = calcX(ax,bx,t_ind_x)
        y_form_vals = calcY(ay,by,t_ind_y)
        for x,y in zip(x_form_vals, y_form_vals):
            function = ((1 - x) ** 2) * (np.exp(-x ** 2 - (y + 1) ** 2)) - (x - x ** 3 - y ** 3) * (np.exp(-x ** 2 - y ** 2))
            PoblacionFitness.append(function)
        return PoblacionFitness
    elif(opcion == 4):
        x_form_vals = calcX(ax,bx,t_ind_x)
        y_form_vals = calcY(ay,by,t_ind_y)
        for x,y in zip(x_form_vals, y_form_vals):
            function = (16*x*(1-x)*y*(1-y)*np.sin(k*np.pi*x)*np.sin(k*np.pi*y))**2
            PoblacionFitness.append(function)
        return PoblacionFitness
        
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
    indexP1 = torneo_p(probaTorneo)
    indexP2 = torneo_p(probaTorneo)
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
print("Seleccione una opción:")
print("1. Funcion 1 variable ")
print("2. Funcion 1 de 2 variables ")
print("3. Funcion 2 de 2 variables ")
print("4. Funcion 3 de 2 variables ")
opcion = int(input())
if(opcion != 1 and opcion < 5):
    print("Intervalo de busqueda ")
    ax = float(input('a_x='))
    bx = float(input('b_x='))
    ay = float(input('a_y='))
    by = float(input('a_y='))
    t_ind_x = int(numeroBits(ax, bx, precision))
    t_ind_y = int(numeroBits(ay, by, precision))
    t_ind = t_ind_x + t_ind_y
    k=0
    if(opcion == 4):
        k = int(input("Ingrese k: "))
    
else:
    print("Intervalo de busqueda ")
    a = float(input('a='))
    b = float(input('b='))
    k = 0
    t_ind = int(numeroBits(a, b, precision))
r = float(input('Porcentaje de cruza(decimal): '))
m = float(input('Porcentaje de muta(decimal): '))
threshold = int(input('Ingrese n iteraciones: '))
fitnessPromedio = np.empty((0, threshold))
probaTorneo = float(input('Probabilidad Torneo: '))

# Población inicial aleatoria
P = np.random.randint(2, size=(tam_poblacion, t_ind))

#Division de la poblacion.
# x_values = []
# y_values = []
# for ind in P:
#     x_part = ind[:t_ind_x]
#     y_part = ind[t_ind_y:]
#     x_values.append(x_part)
#     y_values.append(y_part)
    
# x_values = np.asarray(x_values)
# y_values = np.asarray(y_values)


# Parámetros de cruce y mutación
cross_r = round((r * tam_poblacion) / 2)
mut_i = round((m * tam_poblacion))
mejor_fitness = -np.inf
#Ciclar Algoritmo
contador = 1
while  contador <= threshold:
    Fitness = np.zeros(tam_poblacion)
    Fitness = fitness_xy(opcion,k)
    
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
    if promedio > mejor_fitness:
        mejor_fitness = promedio
    print(f'{contador}.-Promedio de fitness: {promedio}')
    print(f'{contador}: Mejor fitness promedio encontrado: {mejor_fitness} ')
    fitnessPromedio = np.append(fitnessPromedio, promedio)
    P = poblacionNueva

    contador += 1

# -----------------------------------------> Graficación <-----------------------------------------------------
r *= 100
m *= 100
probaTorneo *= 100
plt.plot(fitnessPromedio)
plt.title(f'Tamaño de la poblacion = {tam_poblacion} Porcentaje de cruza {r}% Porcentaje de muta = {m}%\n Torneo:{probaTorneo}%', fontsize = 10)
plt.xlabel("Número de Iteraciones")
plt.ylabel("Promedio Fitness")
plt.show()