import random

tam_poblacion = int(input("Tam poblacion: "))
poblacion = []
poblacionFitness = []
count = 0

#Proceso de selección
def ruleta():
     #Generar recta
     recta = list(range(0, sumaTotal() + 1))
     print(f'Recta: {recta}')
    #Dividirla en subintervalos
     valor_previo = 0
     for i in poblacionFitness:
         subintervalo=recta[valor_previo:i]
         print(f'i: {i},prev: {valor_previo},Sub_i: {subintervalo}')
         valor_previo = i


def addFitness():
    aux = 0
    while (aux != tam_poblacion):
        poblacionFitness.append(fitness(poblacion[aux]))
        aux += 1

def sumaTotal():
    return sum(poblacionFitness)
    
def fitness(individuo):
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

addFitness()
print(f'Poblacion: {poblacionFitness}')
print(f'Suma Total: {sumaTotal()+1}')
ruleta()
