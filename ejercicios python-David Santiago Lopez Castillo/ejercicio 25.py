#ejercicio 25
palabras = []
for _ in range(5):
    palabra = input("Ingrese una palabra: ").upper()
    palabras.append(palabra)
print("Lista de introducida: ", palabras)
palabras.sort()
print("Lista ordenada alfabeticamente:", palabras)
palabra_eliminar = input("Ingrese una palabra para eliminar: ").upper()
if palabra_eliminar in palabras:
    palabras.remove(palabra_eliminar)
    print(f"La palabra '{palabra_eliminar}' ha sido eliminada.")
else:
    print("La palabra no se encuentra en la lista.")

print("Lista final:", palabras)
