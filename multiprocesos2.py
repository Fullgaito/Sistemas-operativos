import multiprocessing
import time

def worker_1():
    print("Subprocesos 1 ejecutandose")
    time.sleep(5)
    print("Subproceso 1 terminado")

def worker_2():
    print("Subprocesos 2 ejecutandose")
    time.sleep(3)
    print("Subproceso 2 terminado")

if __name__=="__main__":
    p1=multiprocessing.Process(target=worker_1)
    p2=multiprocessing.Process(target=worker_2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Ambos subprocesos han terminado")