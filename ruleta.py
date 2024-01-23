import random

tam_poblacion = int(input("Tam poblacion: "))
poblacion = []
poblacionFitness = []
count = 0

def ruleta(individuo):
    recta = range(0, total_sum())
    section = 0
    for section in recta:
        print(section)
        section += 1

def total_sum():
    aux = 0
    while (aux != tam_poblacion):
        poblacionFitness.append(fitness(poblacion[aux]))
        aux += 1
    totalFitness = sum(poblacionFitness)
    return totalFitness
    
def fitness(individuo): #Fitness es un valor: "fitness = 34"
    decimal = int(individuo, 2)
    return decimal  

#Funcion para generar individuo
def genera_individuo():
    count = 0
    individuo = ""
    while(count != 6):
        temp = str(random.randint(0,1)) 
        individuo += temp
        count += 1
    
    return individuo #Cadena de 0's y 1's

#Llenar poblacion 
while(count < tam_poblacion):
   poblacion.append(genera_individuo())
   count += 1



