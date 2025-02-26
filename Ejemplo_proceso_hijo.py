import subprocess
import multiprocesos

#comando para ejecutar una aplicacion

command1=["notepad.exe"]

command2=["calc.exe"]

hijo1=subprocess.Popen(command1)

hijo2=subprocess.Popen(command2)

hijo1.wait()

print("Ambos procesos han finalizado")
multiprocesos.funcion_proceso(1)