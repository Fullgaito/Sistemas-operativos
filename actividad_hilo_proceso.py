import threading
import multiprocessing
import time

def contar():
    for i in range(1,11):
        print(f"contando: {i}")
        time.sleep(1)

if __name__=="__main__":
    #crear un hilo y ejecutarlo
    hilo=threading.Thread(target=contar)
    hilo.start()

    #crear y ejecutar un proceso
    proceso=multiprocessing.Process(target=contar)
    proceso.start()

    #Esperar que ambos terminen
    hilo.join()
    proceso.join()

    print(f"Hilo y proceso han finalizado")