import random
import numpy
import math
import matplotlib.pyplot as plt 

def fitness(poblacion):
    for individuo in poblacion:
        x = individuo[0]
        y = individuo[1]
        valor = (1 - x) ** 2 * math.exp(-x*2 - (y + 1)**2) - (x - x**3 - y**3) * math.exp(-x**2 - y*2)
        poblacionFitness.append(valor)

def mutacion():
    print(f"\nSe agregarán: {ciclo_mutacion} individuos nuevos\n")
    for _ in range(ciclo_mutacion):
        randInd = random.choice(P_μ)
        newInd = (randInd[0] + random.gauss(0,1), randInd[1] + random.gauss(0,1), 1, 1)
        
        if newInd[0] < a:
            newInd = (a, newInd[1], 1, 1)
        elif newInd[0] > b:
            newInd = (b, newInd[1], 1, 1)
            
        if newInd[1] < a:
            newInd = (newInd[0],a, 1, 1)
        elif newInd[1] > b:
            newInd = (newInd[0],b, 1, 1)
        P_λ.append(newInd)
        
def cruza():
    for _ in range(ciclo_cruza):
        ind_1 = random.choice(P_μ)
        ind_2 = random.choice(P_μ)
        cruza = (ind_1[0] + ind_2[0]) / 2, (ind_1[1] + ind_2[1]) / 2, (ind_1[2] + ind_2[2]) / 2, (ind_1[3] + ind_2[3]) / 2
        P_λ.append(cruza)

# >>>>>>> Variables Constantes <<<<<<<<<<<<
μ = int(input("Valor μ: "))
λ = int(input("Valor λ: "))
m = float(input("Valor m: "))
r = 1 - m
print(f"Valor r: {r}")
thresh = int(input("Repeticiones: "))
print("Intervalo de busqueda:")
a = int(input("Valor limite inferior a:"))
b = int(input("Valor limite superior b:"))
ciclo_mutacion = round(λ * m)
ciclo_cruza = round(λ * r)
P_μ = []
P_λ = []
poblacionFitness = []
promedioFitness = []
bestFitness = []

# Generar la población
for _ in range(μ):
    x = random.uniform(a,b)
    y = random.uniform(a,b)
    individuo = (x, y, 1, 1)
    P_μ.append(individuo)
    
print("\nPoblacion inicial\n")
for index, individuo in enumerate(P_μ):
    print(f"Inviduo {index+1}: {individuo}")
    
# Calcular Fitness 
fitness(P_μ)

print("\nFitness de la poblacion inicial\n")
for index, individuo in enumerate(poblacionFitness):
    print(f"Fitness {index+1}: {individuo}")
    
iteraciones = 1

while(iteraciones <= thresh):
    mutacion()
    cruza()
    fitness(P_λ)
    print(f"\nNuevos individuos a entrar a P_μ\n")
    for index, individuo in enumerate(P_λ):
        print(f"Individuo {index+1}: {individuo}")
        
    P_μ.extend(P_λ)
    print(f"\nP_λ con nuevos integrantes:\n")
    for index, individuo in enumerate(P_μ):
        print(f"Individuo {index+1}: {individuo}")
    
    print("\n Unión de individuo con respectivo fitness:\n")
    P = list(zip(poblacionFitness, P_μ))
    for index, individuo in enumerate(P):
        print(f"Individuo {index+1}: {individuo}")
        
    print("\n Ordenar elementos segun su fitness \n")
    P.sort(reverse=True)
    for index, individuo in enumerate(P):
        print(f"Individuo {index+1}: {individuo}")
        
    print("\n Conservar los mejores individuos \n")
    P = P[:-λ]
    for index, individuo in enumerate(P):
        print(f"Individuo {index+1}: {individuo}")
        
    # Limpiamos para evitar que en la siguiente iteracion se añadan elementos no deseados    
    poblacionFitness.clear()
    P_λ.clear()
    P_μ.clear()
    
    poblacionFitness = [individuo[0] for individuo in P]
    P_μ = [individuo[1] for individuo in P]
    
    promedio = numpy.mean(poblacionFitness)
    promedioFitness.append(promedio)
    
    best = numpy.amax(poblacionFitness)
    bestFitness.append(best)
    
    iteraciones += 1
    
# ----------------------- Graficar ------------------------------

bestMax = numpy.amax(bestFitness)
promMax = numpy.amax(promedioFitness)
plt.plot(promedioFitness)
plt.xlabel("Iteraciones")
plt.ylabel("Fitness")
plt.show()