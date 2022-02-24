import csv

nombre_archivo = 'CallesMedellin.csv'

with open(nombre_archivo,newline = '\n') as f:
    datos = csv.reader(f, delimiter = ';')

    calles = list(datos)


print(calles[1]) 

