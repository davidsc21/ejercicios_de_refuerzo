#ejercicio 1
import os
import sys
frutas=[]
cantidad=3
def varitexto(msg):
    x=input(msg)
    if x.isalpha():
        return x
    else:
        print('la informacion ingresada contiene valores no alfabeticos')
        return varitexto(msg)
def limpiar_pantalla():
    if sys.platform== 'linux' or sys.platform=='darwin':
        os.system('clear')
    else:
        os.system('cls') 
limpiar_pantalla           
for i in range(1,cantidad+1,1):
    fruta=varitexto(f'ingrese el nombre de la fruta numero {i}:\n')
    frutas.append(fruta)
print(f'{frutas}')
