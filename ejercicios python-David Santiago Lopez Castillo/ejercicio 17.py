#ejercicio 17
def evaluar_estado(msg)->int:
    try:
        x=input(msg)
        return x
    except ValueError:
        print('ingrese un valor valido')
        return(evaluar_estado)
nota=int(evaluar_estado('ingrese la nota del estudiante (0-10)\n->'))
if nota>=0 and nota<=10:
    match nota:
        case 10:
            print('Excelente')
        case 9:
            print('Muy bien')
        case 8:
            print('Muy bien')
        case 7:
            print('Bien')
        case 6:
            print('Bien')
        case 5:
            print('Regular')
        case 4:
            print('Regular')
        case _:
            print('Reprobado')
else:
    print('valor invalido, terminando el programa')