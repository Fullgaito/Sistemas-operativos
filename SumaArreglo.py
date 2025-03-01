import threading
import random

def crear_arreglo_aleatorio(cantidad_hilos=4):
    """
    Genera un arreglo con números aleatorios y lo divide en partes iguales.
    :param cantidad_hilos: Número de partes en que se dividirá el arreglo.
    :return: Lista de partes del arreglo.
    """
    tamano = 1000000
    arreglo = [random.randint(1, 100) for _ in range(tamano)]  # Generar el arreglo con números aleatorios

    # Mostrar la suma total antes de partición
    suma_total = sum(arreglo)
    print("La suma de los elementos del arreglo antes de partición es:", suma_total)

    # Calcular tamaño de cada parte
    tam = len(arreglo) // cantidad_hilos
    partes = [arreglo[i * tam: (i + 1) * tam] for i in range(cantidad_hilos)]
    partes[-1] += arreglo[cantidad_hilos * tam:]  # Asegurar que la última parte tenga los elementos restantes
    
    return partes

def suma_parcial(parte, resultado, index):
    """
    Calcula la suma de una parte del arreglo y la almacena en un índice de una lista compartida.
    :param parte: Sublista de números.
    :param resultado: Lista compartida donde almacenar la suma parcial.
    :param index: Índice donde almacenar el resultado.
    """
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
