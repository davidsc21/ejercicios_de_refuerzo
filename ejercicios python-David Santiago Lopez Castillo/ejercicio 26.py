#ejercicio 26
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def estadisticas(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    promedio = sum(numeros) / len(numeros)
    return maximo, minimo, promedio

max_num, min_num, prom = estadisticas(numeros)
print(f"Número máximo: {max_num}")
print(f"Número mínimo: {min_num}")
print(f"Promedio: {prom}")

