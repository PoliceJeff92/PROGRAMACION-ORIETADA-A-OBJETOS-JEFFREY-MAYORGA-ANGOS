def ingresar_temperaturas_diarias():
    """
    Esta función solicita al usuario que ingrese las temperaturas diarias de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas_diarias = []
    for dia in range(1, 8):
        temperatura_dia = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas_diarias.append(temperatura_dia)
    return temperaturas_diarias

def calcular_promedio_semanal(temperaturas_diarias):
    """
    Esta función calcula el promedio de las temperaturas diarias de la semana.
    Recibe como parámetro una lista con las temperaturas diarias.
    Retorna el promedio semanal.
    """
    suma_temperaturas = sum(temperaturas_diarias)
    promedio_semanal = suma_temperaturas / len(temperaturas_diarias)
    return promedio_semanal

def main():
    """
    Esta función principal llama a las funciones para ingresar datos y calcular el promedio.
    """
    temperaturas_diarias = ingresar_temperaturas_diarias()
    promedio_semanal = calcular_promedio_semanal(temperaturas_diarias)
    print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}")

if __name__ == "__main__":
    main()
