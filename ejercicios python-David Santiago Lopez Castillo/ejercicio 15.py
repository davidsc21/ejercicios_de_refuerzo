#ejercicio 15
try:
    opcion=int(input('ingrese la opcion a realizar\n1.imprimir un texto\n2.imprimir texto 2\n'))
    pass
except ValueError:
    print('ingrese una opcion valida')

match opcion:
    case 1:
        print('usted seleciono la opcion 1')
    case 2:
        print('usted selecciono la opcion 2')
    case _:
        print('opcion invalida, terminando el programa')