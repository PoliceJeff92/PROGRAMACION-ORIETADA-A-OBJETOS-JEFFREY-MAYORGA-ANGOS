class Dia:
    """
    Esta clase representa la información diaria del clima.
    """

    def __init__(self, fecha, temperatura):
        """
        Constructor de la clase Dia.
        Inicializa los atributos `fecha` y `temperatura` con los valores proporcionados.
        """
        self.fecha = fecha
        self.temperatura = temperatura

    def __str__(self):
        """
        Método de representación de la clase Dia.
        Devuelve una cadena con la información del día (fecha y temperatura).
        """
        return f"Fecha: {self.fecha}, Temperatura: {self.temperatura:.2f}"

class RegistroSemanal:
    """
    Esta clase representa un registro semanal de información del clima.
    Almacena una lista de objetos `Dia` y proporciona métodos para ingresar datos y calcular el promedio semanal.
    """

    def __init__(self):
        """
        Constructor de la clase RegistroSemanal.
        Inicializa una lista vacía llamada `dias` para almacenar los objetos `Dia`.
        """
        self.dias = []

    def ingresar_dia(self, fecha, temperatura):
        """
        Este método agrega un nuevo día al registro semanal.
        Crea un nuevo objeto `Dia` con la fecha y temperatura proporcionadas, y lo agrega a la lista `dias`.
        """
        nuevo_dia = Dia(fecha, temperatura)
        self.dias.append(nuevo_dia)

    def calcular_promedio_semanal(self):
        """
        Este método calcula el promedio semanal de temperaturas.
        Si no hay días registrados, retorna `None`.
        De lo contrario, calcula la suma de las temperaturas y la divide por la cantidad de días, retornando el promedio.
        """
        if not self.dias:
            return None

        suma_temperaturas = sum([dia.temperatura for dia in self.dias])
        promedio_semanal = suma_temperaturas / len(self.dias)
        return promedio_semanal

    def imprimir_registro(self):
        """
        Este método imprime el registro semanal de información del clima.
        Imprime la información de cada día (fecha y temperatura) y luego imprime el promedio semanal.
        """
        print("Registro Semanal del Clima:")
        for dia in self.dias:
            print(dia)

        promedio_semanal = self.calcular_promedio_semanal()
        if promedio_semanal is not None:
            print(f"Promedio semanal de temperaturas: {promedio_semanal:.2f}")

def main():
    """
    Esta función principal crea un objeto `RegistroSemanal` y lo utiliza para ingresar datos y calcular el promedio semanal.
    """
    registro_semanal = RegistroSemanal()

    # Ingreso de datos diarios
    for dia in range(1, 8):
        fecha = input(f"Ingrese la fecha del día {dia} (formato dd/mm/aaaa): ")
        try:
            temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        except ValueError:
            print("Error: La temperatura debe ser un número válido.")
            continue

        registro_semanal.ingresar_dia(fecha, temperatura)

    # Impresión del registro semanal
    registro_semanal.imprimir_registro()

if __name__ == "__main__":
    main()
