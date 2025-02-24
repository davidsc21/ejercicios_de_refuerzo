#ejercicio 28
animales=[]
mamiferos=['perro','gato', 'elefante','caballo','ornitorrinco']
insectos=['saltamontes','mariquita','hormiga','mantis religiosa']
print(mamiferos)
print(insectos)
while True:   
    try:
        opcion=int(input('desea juntar las listas?\n1.Si\n2.No\n'))
        break
    except ValueError:
        print('ingrese una opcion valida')
match opcion:
    case 1:
        animales.extend(mamiferos)
        animales.extend(insectos)
        print(animales)
    case 2:
        print('hasta luego...')
    case _:
        print('opcion invalida, terminando el programa')