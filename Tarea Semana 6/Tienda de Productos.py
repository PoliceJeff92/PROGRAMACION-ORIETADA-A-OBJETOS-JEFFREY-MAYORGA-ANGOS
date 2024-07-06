class Producto:
    """
    Clase base que representa un producto genérico.
    """

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_nombre(self):
        return self.nombre

    def obtener_precio(self):
        return self.precio

    def calcular_descuento(self, descuento):
        precio_final = self.precio * (1 - descuento)
        return precio_final

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}"


class Libro(Producto):
    """
    Clase derivada que representa un libro.
    """

    def __init__(self, nombre, precio, autor):
        super().__init__(nombre, precio)
        self.autor = autor

    def obtener_autor(self):
        return self.autor

    def __str__(self):
        return f"Libro: {self.nombre}, Autor: {self.autor}, Precio: ${self.precio:.2f}"


class Camisa(Producto):
    """
    Clase derivada que representa una camisa.
    """

    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.talla = talla

    def obtener_talla(self):
        return self.talla

    def __str__(self):
        return f"Camisa: {self.nombre}, Talla: {self.talla}, Precio: ${self.precio:.2f}"


# Ejemplo de uso

producto1 = Libro("El señor de los anillos", 50.00, "Jeffrey Jose Mayorga Angos")
producto2 = Camisa("Camisa deportiva", 25.00, "M")

print(producto1)  # Muestra información del libro
print(producto2)  # Muestra información de la camisa

descuento = 0.10  # Descuento del 10%

precio_final_libro = producto1.calcular_descuento(descuento)
precio_final_camisa = producto2.calcular_descuento(descuento)

print(f"Precio final del libro con descuento: ${precio_final_libro:.2f}")
print(f"Precio final de la camisa con descuento: ${precio_final_camisa:.2f}")

