import multiprocessing

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calcular_primos(rango):
    inicio, fin = rango
    primos = [n for n in range(inicio, fin) if es_primo(n)]
    return primos

def main():
    num_procesos = 4  # Número configurable de procesos
    rango_total = (1, 12000)  # Rango total a evaluar
    tamanio_rango = (rango_total[1] - rango_total[0]) // num_procesos

    # Crear los rangos para cada proceso
    rangos = [(rango_total[0] + i * tamanio_rango, rango_total[0] + (i + 1) * tamanio_rango) for i in range(num_procesos)]
    rangos[-1] = (rangos[-1][0], rango_total[1])  # Ajustar el último rango para cubrir todo el intervalo

    with multiprocessing.Pool(num_procesos) as pool:
        resultados = pool.map(calcular_primos, rangos)
    
    # Imprimir los resultados
    for i, primos in enumerate(resultados):
        print(f"Proceso {i + 1}: {primos}\n\n")

if __name__ == "__main__":
    main()
