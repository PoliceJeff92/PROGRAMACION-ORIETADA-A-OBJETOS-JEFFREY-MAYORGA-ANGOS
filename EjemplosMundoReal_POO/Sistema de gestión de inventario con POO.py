class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def agregar_cantidad(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se han agregado {cantidad} unidades de {self.nombre}.")
        else:
            print("La cantidad a agregar debe ser mayor que 0.")

    def eliminar_cantidad(self, cantidad):
        if cantidad > 0 and self.cantidad >= cantidad:
            self.cantidad -= cantidad
            print(f"Se han eliminado {cantidad} unidades de {self.nombre}.")
        elif cantidad <= 0:
            print("La cantidad a eliminar debe ser mayor que 0.")
        else:
            print(f"No hay suficientes unidades de {self.nombre} para eliminar {cantidad}.")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Cantidad disponible: {self.cantidad}")

# Crear algunos productos de ejemplo
producto1 = Producto("Camiseta", 15.99, 10)
producto2 = Producto("Pantalón", 29.95, 5)
producto3 = Producto("Zapatos", 44.99, 12)

# Agregar cantidad a un producto
producto1.agregar_cantidad(3)

# Eliminar cantidad de otro producto
producto2.eliminar_cantidad(2)

# Mostrar información de un producto
producto3.mostrar_informacion()
