#ejercicio 29
palabras = ["hola", "mundo", "python", "codigo", "python", "lista", "mundo"]
indices_encontrados = []

buscar = input("Ingresa una palabra a buscar:\n")
for i, palabra in enumerate(palabras):
    if palabra == buscar:
        indices_encontrados.append(i)

if indices_encontrados:
    print(f"La palabra {buscar} se encontrò y su posicion/es en la lista original son:")
    print(indices_encontrados)
else:
    print('no se encontro la palabra')