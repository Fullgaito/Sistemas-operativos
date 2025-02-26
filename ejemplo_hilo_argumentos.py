import threading
import time

def saludo(nombre):
    print(f"Hola {nombre} bienvenido")
    time.sleep(2)

if __name__=="__main__":
    #Crear un hilo y ejecutarlo
    hilo=threading.Thread(target=saludo,args=("Pedro",))
    hilo.start()

    #Esperar a que el hilo termine
    hilo.join()

    print("El hilo ha terminado")