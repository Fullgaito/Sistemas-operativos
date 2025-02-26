import threading
import time

def contar():
    for i in range(1,11):
        print(f"Contando: {i}")
        time.sleep(1)

if __name__=="__main__":
    #Crear un hilo y ejecutarlo
    hilo=threading.Thread(target=contar)
    hilo.start()

    #Esperar a que el hilo termine
    hilo.join()

    print("El hilo ha terminado")