#ejercicio 7
import os
colores= ['amarillo','verde','azul','rojo','naranja','morado']
try:
    indice=(input('ingrese un color:\n'))
    idx=colores.index(indice)
    print(f'la posicion de su color en la lista es: {idx+1}')
except TypeError:
    print ('el color no esta en la lista')