import threading

import random

def crear_arreglo_aleatorio(cantidad_hilos=4):
    # Crear una lista vacía
    arreglo = []

    # Definir el tamaño del arreglo
    tamano = 1000000

    # Rellenar con números aleatorios entre 1 y 100
    for i in range(tamano):
        arreglo.append(random.randint(1, 100))

    # Mostrar el arreglo
    print("Arreglo generado:", arreglo)
    suma=0
    for j in range(len(arreglo)):
        suma+=arreglo[j]
    print("La suma de los elementos del arreglo antes de particion es:", suma)


    tam=len(arreglo)//cantidad_hilos
    parte1=arreglo[:tam]
    parte2=arreglo[tam:2*tam]
    parte3=arreglo[2*tam:3*tam]
    parte4=arreglo[3*tam:]

    suma1=suma_parcial(parte1)
    suma2=suma_parcial(parte2)
    suma3=suma_parcial(parte3)
    suma4=suma_parcial(parte4)

    return parte1, parte2, parte3, parte4


def suma_parcial(parte, resultado, index):
    
    resultado[index] = sum(parte)

if __name__ == "__main__":
    cantidad_hilos = 4
    partes = crear_arreglo_aleatorio(cantidad_hilos)
    resultado = [0] * cantidad_hilos  # Lista para almacenar resultados parciales
    hilos = []

    # Crear y ejecutar los hilos para calcular sumas parciales
    for i in range(cantidad_hilos):
        hilo = threading.Thread(target=suma_parcial, args=(partes[i], resultado, i))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for i, hilo in enumerate(hilos):
        hilo.join()
        print(f"El hilo {i+1} ha terminado con suma parcial: {resultado[i]}")

    # Calcular la suma total
    suma_total = sum(resultado)
    print("La suma total del arreglo es:", suma_total)