import random

tam_poblacion = int(input("Tam poblacion: "))
poblacion = []
count = 0

#Llenar poblacion 
while(count < tam_poblacion):
   poblacion.append(genera_individuo())
   count += 1

print(poblacion)

#Funcion para generar individuo
def genera_individuo():
    count = 0
    individuo = ""
    while(count != 32):
        temp = str(random.randint(0,1)) 
        individuo += temp
        count += 1
    
    return individuo
