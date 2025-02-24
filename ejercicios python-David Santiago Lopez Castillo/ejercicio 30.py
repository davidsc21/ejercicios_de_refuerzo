#ejercicio 30
numeros = [1,2,3,4,5,6,7,8,9,10]

def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])

resultado = suma_lista(numeros)
print(f"La suma de la lista:\n{numeros}\nes: {resultado}")
