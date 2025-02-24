#ejercicio 22
def sumar(a, b):
    return a + b

while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    except ValueError:
        print("Entrada no válida. Intente de nuevo.")
        continue
    
    repetir = input("¿Desea realizar otra operación? (si/no): ").strip().lower()
    if repetir == "no":
        break
    else:
        pass

    
