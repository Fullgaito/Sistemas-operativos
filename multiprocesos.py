import multiprocessing
import time

def funcion_proceso(proceso_id):

    print(f"Proceso {proceso_id} iniciado")
    time.sleep(3)
    print(f"Proceso {proceso_id} terminado")

if __name__=="__main__":

    num_procesos=4

    procesos=[]

    for i in range(num_procesos):

        p=multiprocessing.Process(target=funcion_proceso,args=(i,))
        procesos.append(p)
        p.start()
    for p in procesos:
        p.join()
    print("Todos los procesos han terminado")
    