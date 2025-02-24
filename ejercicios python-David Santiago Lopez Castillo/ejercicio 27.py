#ejercicio 27
calificaciones = []

while True:
        for i in range (1,9):
            try:
                calificacion = float(input("Ingresa una calificación (0 a 5, negativo terminara el proceso):\n"))
                if calificacion < 0:
                    break
                elif 0 <= calificacion <= 5:
                    calificaciones.append(calificacion)
                else:
                    print("Calificación fuera de rango. Intenta de nuevo.")
            except ValueError:
                print("opcion inválida. Ingrese un número válido.")
        break
if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Calificaciones ingresadas: {calificaciones}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron calificaciones válidas.")