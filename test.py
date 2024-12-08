import os

from datetime import datetime 

fecha=datetime.now()

print(f"fecha {fecha}")

dt_string=fecha.strftime("%d/%m/%Y %H:%M:%S")

print("Fecha y hora",dt_string)

file=open("logfecha.txt","w")

file.write("Fecha de inicio: "+ os.linesep)

file.write(dt_string)

file.close()