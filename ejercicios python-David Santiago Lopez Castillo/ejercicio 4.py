#ejercicio 4
import os
animales=['perro','gato','elefante','ardilla','jirafa']
print(f'a continuacion se le muestra la lista de animales:\n{animales}')
while True:    
    re=input('ingrese el animal que desea remover:\n').lower()
    if re not in animales:
        print('el animal ingresado no se encuentra en la lista')
    else:
        animales.remove(re)
        break
print(f'{animales}')    
