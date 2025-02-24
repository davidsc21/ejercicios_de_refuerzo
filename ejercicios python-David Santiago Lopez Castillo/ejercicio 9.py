#ejercicio 9
import os
numeros=[4,3,7,6,1,5,8,2,9]
print(f'{numeros}')
orden=input('de que forma desea ordenar la lista:\n1.ascendente\n2.descendente\n')
match orden:
    case '1':
        numeros.sort()
        print(f'el orden de la lista en forma ascendente es: {numeros}')
    case '2':
        numeros.sort(reverse=True)
        print(f'el orden de la lista en forma descendente es: {numeros}')    