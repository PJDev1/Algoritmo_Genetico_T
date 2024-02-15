import random
import numpy
import math
from math import log
from math import pi
from math import sin
import matplotlib.pyplot as plt

# --------------------Declaracion de las funciones a utilizar-----------------------------
def intervalo():
    return abs(li) + abs(ls)

def numeroBits():
    return round(log(inter * 10 ** precis + 1, 2))

def binarioDecimal(binario):
    decimal = 0
    for posicion, digito_string in enumerate(binario[::-1]):
        decimal += int(digito_string) * 2 ** posicion
    return decimal

def representacionIntervalo(decimal):
    return li + decimal * ((ls-li)/(2 ** nBits - 1))

def fitnessPoblacion(x):
    return (x * sin(10 * pi * x) + 1)

def numeroSeleccion():
    return round((1-r)*n)

def seleccionDirecta():
    for x in range(seleccion):
        nr = random.random()
        print("Numero generado aleatoriamente ------------------------------------------>", nr)
        for x in pctFitness:
            if nr <= x:
                indice = pctFitness.index(x) #Saca el indice de la posicion de la ruleta para seleccionar el individuo de la poblacion original
                pobNueva.append(pob[indice]) #Individuo seleccionado pasa directamente a la nueva poblacion
                break

        print("Individuo seleccionado de la poblacion original por su indice ----------->", indice, "\n")

def seleccionCruza():
    for x in range(individuosCruza):
        nr = random.random()
        print("\nNumero generado aleatoriamente ------------------------------------------>", nr)
        for x in pctFitness:
            if nr <= x:
                indice = pctFitness.index(x) #Saca el indice de la posicion de la ruleta para seleccionar el individuo de la poblacion original
                pobCruza.append(pob[indice]) #Individuo seleccionado pasa a poblacion de cruza
                break

        print("Individuo seleccionados de la poblacion original por su indice ----------->", indice, "\n")

    print("\nIndividuos seleccionados para la cruza: \n")
    i = 1
    for cadena in pobCruza:
        print("Individuo", i, ":", "".join(map(str, cadena)))
        i += 1

def cruza():
    i = 0
    p = 0
    for x in range(numPares):
        padre1 = pobCruza[i]
        padre2 = pobCruza[i + 1]
        print("\nPar de padres", p, ":", padre1, padre2)
        corte = random.randint(1, nBits)
        print("\nPunto de corte para la cruza: ", corte)
        hijo1 = padre1[:corte] + padre2[corte:nBits]
        pobNueva.append(hijo1)
        hijo2 = padre2[:corte] + padre1[corte:nBits]
        pobNueva.append(hijo2)
        print("\nPar de hijos", p, ":", hijo1, hijo2)
        p += 1
        i += 2

def mutacion():
    for x in range(nMutacion):
        individuoMutado = random.choice(pobNueva)
        print("\nIndividuo a mutar:", individuoMutado)

        bitMutacion = random.randint(0, nBits-1)
        print("Posicion de bit a mutar: ", bitMutacion)

        if individuoMutado[bitMutacion] == 0:
            individuoMutado[bitMutacion] = 1
        else:
            individuoMutado[bitMutacion] = 0

        print("Individuo mutado: ", individuoMutado)



print("\nNumero de individuos (poblacion): ")
n = int(input())

print("\nIngrese el limite inferior: ")
li = int(input())

print("\nIngrese el limite superior: ")
ls = int(input())

while ls <= li:
    print("\n¡Limite superior debe ser mayor a limite inferior!")
    print("Ingrese nuevamente el limite superior: ")
    ls = int(input());

print("\nIngrese el valor de precision: ")
precis = int(input())

print("\nFracción de la población que será reemplazada por cruza?(r): ")
r = float(input())

print("\nFracción de la población que será reemplazada por mutación?(m): ")
m = float(input())

print("\nNumero de generaciones(iteraciones): ")
it = int(input())

# --------------------Inicio del programa-----------------------------

promedioFitness = [] # Lista donde se almacenara el promedio de todos los fitness en cada iteración
iteraciones = 1 # Contador de iteraciones

inter = intervalo() #Calcular intervalo de los limites
print("\nIntervalo entre", li, "y", ls, ": ", inter)

nBits = numeroBits() #Calcular en numero de bits para representar a los individuos
print("\nNumero de bits de representacion: ", nBits)


# --------------------Generar individuos binarios aleatorios para la poblacion-----------------------------

pob = [[random.randint(0, 1) for x in range(nBits)] for x in range(n)]

# --------------------Ciclamos el algoritmo el numero de veces que se pidio-----------------------------
while iteraciones <= it:

    print("\nPoblacion generada aleatoriamente (binario): \n")
    i = 1
    for cadena in pob:
        print("Individuo", i, ":", "".join(map(str, cadena)))
        i += 1

    # ---------------------Pasar poblacion a numeros decimales-----------------------------
    pobDecimal = []
    i = 1
    print("\nPoblacion (decimal):\n")
    for binario in pob:
        x = binarioDecimal(binario)
        pobDecimal.append(x)
        print("Individuo", i, ":", x)
        i += 1

    # ---------------------Representacion de los valores de x dentro del intervalo---------
    print("\nValor de representacion dentro del intervalo de búsqueda [li <-----> ls]:\n")
    pobRepresentacion = []
    i = 1
    for individuo in pobDecimal:
        x = representacionIntervalo(individuo)
        pobRepresentacion.append(x)
        print("X", i, ":", x)
        i += 1

    # ---------------------Calcular el valor de fitnes de cada individuo-----------------------------
    print("\nValor de fitness por individuo:\n")
    pobFitness = []
    i = 1
    for individuo in pobRepresentacion:
        f = fitnessPoblacion(individuo)
        pobFitness.append(f)
        print("Fitness ( h", i, "): ", f)
        i += 1

    # ---------------------Fitness negativos cambiarlos a valor de 0-----------------------------

    for individuo in range(len(pobFitness)):
        if pobFitness[individuo] < 0:
            pobFitness[individuo] = 0

    print("\nValor de fitness por individuo (eliminando valores negativos):\n")
    i = 1
    for individuo in pobFitness:
        print("Fitness ( h", i, "): ", individuo)
        i += 1

    # ---------------------Dividir cada fitness / sumatoria total de fitness-----------------------------
    sumaFitness = sum(pobFitness)
    print("\nSumatoria de todos los fitness:", sumaFitness)

    print("\nDivision de cada fitness sobre la sumatoria total de fitness:\n")
    divFitness = []
    i = 1
    for x in pobFitness:
        w = x/sumaFitness
        divFitness.append(w)
        print("Fh", i, ": ", w)
        i += 1

    interval = sum(divFitness)
    print("\nIntervalo 0 a FT = ", interval)

    # ---------------------Generar la ruleta-----------------------------
    print("\nValores (%) correspondientes de la ruleta:\n")
    pctFitness = []
    i = 1
    s = 0
    for x in divFitness:
        s += x
        pctFitness.append(s)
        print("Fh", i, ": ", s)
        i += 1

    # ---------------------Seleccion de individuos que pasan directo a la nueva poblacion-----------------------------
    seleccion = numeroSeleccion()
    print("\nNumero de individuos a seleccionar: ", seleccion)

    print("\nIndividuos seleccionados con ruleta:\n")

    pobNueva = []
    indice = 0

    seleccionDirecta()

    print("\nIndividuos que pasan directamente a la nueva poblacion: \n")
    i = 1
    for cadena in pobNueva:
        print("Individuo", i, ":", "".join(map(str, cadena)))
        i += 1

    #-------------Calcular pares, seleccion de individuos para la cruza y cruza---------------------------
    numPares = math.ceil((r * n) / 2)
    print("\nNumero de pares necesarios para la cruza: ", numPares)
    individuosCruza = numPares * 2
    pobCruza = []

    seleccionCruza()

    cruza()

    print("\nIndividuos de la nueva poblacion: \n")
    i = 1
    for individuo in pobNueva:
        print("Individuo", i, ":", "".join(map(str, individuo)))
        i += 1

    if len(pobNueva) > len(pob):
        pobNueva.pop()

    print("\nIndividuos de la nueva poblacion: \n")
    i = 1
    for individuo in pobNueva:
        print("Individuo", i, ":", "".join(map(str, individuo)))
        i += 1

    # -------------Calcular mutacion, seleccion de individuos para la mutacion y mutacion---------------------------
    nMutacion = math.ceil(m * n)

    print("\nNumero de individuos a mutar: ", nMutacion)

    mutacion()

    print("\nIndividuos de la nueva poblacion: \n")
    i = 1
    for cadena in pobNueva:
        print("Individuo", i, ":", "".join(map(str, cadena)))
        i += 1

    # -------------Calcular el promedio de todos los fitness en cada iteracion---------------------------
    promedio = numpy.mean(pobFitness)
    print("\nEl promedio de los fitness en la iteracion", iteraciones, "es:", promedio, "\n")
    promedioFitness.append(promedio)

    # -------------Poblacion nueva se vuelve la poblacion original---------------------------
    pob = pobNueva

    print("Nueva poblacion generada: \n")
    i = 1
    for linea in pobNueva:
        print("Individuo", i, ":", "".join(map(str, linea)))
        i += 1

    iteraciones += 1 #Contador iteraciones

# -------------Lista de todos los promedios de fitness y su gráfica---------------------------
print("\nLista de fitness (promedios) despues de", iteraciones-1, "iteraciones: \n")
print(promedioFitness)
r *= 100
m *= 100
plt.plot(promedioFitness)
plt.title("Tamaño de la poblacion = %i" %n + "\nPorcentaje de Cruza = %i%%" %r+ "\nPorcentaje de Mutacion = %i%%" %m,
          fontsize=10, loc='left')
plt.xlabel("Número de Iteraciones")
plt.ylabel("Promedio Fitness")
plt.show()