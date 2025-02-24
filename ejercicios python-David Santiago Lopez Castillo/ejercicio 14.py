#ejercicio 14
import os
number_list=[]
print('Bienvenido usuario, ingrese 5 numeros:\n')
for n in range (1,6,1):
    while True:
        try:
            numero=int(input(f'ingrese numero {n}:\n'))
            break
        except ValueError:
            print('ingrese un valor valido')    
    number_list.append(numero)
for impares in number_list:
    if  impares%2!=0:
        print(f'los numeros impares son: {impares}',end=',')
print('\n')
for pares in number_list:
    if  pares%2==0:
        print(f'los numeros pares son: {pares}',end=',')