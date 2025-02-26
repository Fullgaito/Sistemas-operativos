import subprocess

#comando para ejecutar una app

command=["notepad.exe"]

process=subprocess.Popen(command)

process.wait()

print("Proceso ha termiando")