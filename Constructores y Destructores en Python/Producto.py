class Producto:
    """
    Clase que representa un producto con nombre, precio y stock.

    Atributos:
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        stock (int): Stock disponible del producto.

    Métodos:
        __init__(self, nombre, precio, stock): Constructor para inicializar los atributos del producto.
        __del__(self): Destructor para imprimir un mensaje al eliminar el objeto.
        mostrar_informacion(self): Muestra la información del producto.
    """

    def __init__(self, nombre, precio, stock):
        """
        Constructor para inicializar los atributos del producto.

        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            stock (int): Stock disponible del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        print(f"Creando producto: {self.nombre}")

    def __del__(self):
        """
        Destructor para imprimir un mensaje al eliminar el objeto.
        """
        print(f"Eliminando producto: {self.nombre}")

    def mostrar_informacion(self):
        """
        Muestra la información del producto.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Stock: {self.stock}")
        print("-------------------")
# Crear un producto
producto1 = Producto("Camisa", 25.99, 10)

# Mostrar información del producto
producto1.mostrar_informacion()

# Eliminar el producto (activando el destructor)
del producto1

# Crear otro producto
producto2 = Producto("Pantalón", 39.99, 5)

# Mostrar información del producto
producto2.mostrar_informacion()
"""Jeffrey Jose Mayorga Angos"""