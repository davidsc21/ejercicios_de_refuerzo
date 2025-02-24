#ejercicio 20
numeros = list(range(1, 11))
def filtrar_lista(numeros, tipo):
    lista_filtrada = []  
    for numero in numeros:
        if tipo== "pares" and numero%2 == 0:  
            lista_filtrada.append(numero)
        elif tipo== "impares" and numero%2 != 0:  
            lista_filtrada.append(numero)
    return lista_filtrada
pares = filtrar_lista(numeros, "pares")
print(f'Números pares: {pares}')
impares= filtrar_lista(numeros, "impares")
print(f'Números impares: {impares}')
