#ejercicio 16
tareas=[]
menu="""
1.Agregar a la lista
2.Mostrar tareas
3.Eliminar tarea
4.salir
"""
while True:
    print(menu)
    while True:
        try:
            opcion=int(input('->'))
            break
        except ValueError:
            print('ingrese un valor valido')
    match opcion:
        case 1:
            new=input('ingrese la tarea que desea guardar:\n->').lower()
            tareas.append(new)
        case 2:
            print(tareas)
        case 3:
            name=input('ingrese nombre del elemento a eliminar:\n->').lower()
            if name in tareas:
                tareas.remove(name)
                print('elemento eliminado de la lista')
            else:
                print('elemento no econtrado')  
        case 4:
            print('hasta luego...')
            break
        case _:
            print('ingrese un valor valido')  