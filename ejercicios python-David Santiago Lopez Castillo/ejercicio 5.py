#ejercicio 5
import os
numeros=[1,2,3,4,5]
print(f'la lista de hoy es:\n{numeros}')
while True:    
    opcion=input('que desea hacer querido usuario?\n1.hacer pop sin indice\n2.hacer pop con indice\n3.salir\n')    
    match opcion:
            case "1":
                ultimo=numeros.pop()
                print(f'{ultimo}\n se ha eliminado de la lista el ultimo elemento, por esto la lista queda de la siguiente forma:\n{numeros}')
            case "2":
                while True:
                    try:
                        indice=int(input('ingrese el numero del indice:\n'))
                        break
                    except ValueError:
                        print ('ingrese un valor valido')    
                resultado=numeros.pop(indice-1)
                print(f'{resultado}\n se ha eliminado de la lista el numero con el indice seleccionado, por esto la lista queda de la siguiente forma:\n{numeros}')       
            case "3":
                print ('hasta luego...')
                break
                
            