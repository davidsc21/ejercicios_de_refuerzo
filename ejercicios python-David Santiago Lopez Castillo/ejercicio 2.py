#ejercicio 2
import os
numeros=[1,2,3]
cantidad=3
while True:    
    numero=(input('ingrese tres numeros:\n'))
    try:
        number=(list(map(int,numero.split())))
        break
    except ValueError:
        print('ingrese un valor numerico entero')    
numeros.extend(number)         
print(f'{numeros}')