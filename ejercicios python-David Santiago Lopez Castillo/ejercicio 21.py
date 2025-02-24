#ejercicio 21
pares = []
contador = 0

while contador < 3:
    for _ in range(1):
        try:
            numero = int(input("Ingrese un número par entero: "))
        except ValueError:
            print('elemento no valido')
            break
        if numero % 2 == 0:
            pares.append(numero)
            print(f"Número par agregado: {numero}")
            contador += 1
        else:
            print("ingrese un numero par")

print("Lista final de números pares:", pares)
