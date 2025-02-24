#ejercicio 8
import os
x=['manzana','pera','manzana','uva','arandanos','arandanos','manzana']
seleccion=input('ingrese el nombre de la fruta que desea consultar:\n')
if x.count(seleccion)== 0:
    print('la fruta esta agotada en nuestro inventario')
else:
    print(f'la cantidad que nos queda de esa fruta en nuestro inventario es de: {x.count(seleccion)}')