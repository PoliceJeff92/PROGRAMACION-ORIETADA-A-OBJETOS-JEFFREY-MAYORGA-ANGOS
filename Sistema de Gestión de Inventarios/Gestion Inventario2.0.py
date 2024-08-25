class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


import json

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_productos()

    def cargar_productos(self):
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                for producto in datos:
                    self.productos.append(Producto(**producto))
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            print("Error al leer el archivo de inventario. Datos corruptos.")

    def guardar_productos(self):
        with open(self.archivo, 'w') as f:
            json.dump([producto.__dict__ for producto in self.productos], f, indent=2)

    def añadir_producto(self, id, nombre, cantidad, precio):
        if any(p.get_id() == id for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
            return False
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        return True

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                return True
        return False

    def buscar_productos(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)


def menu_principal():
    inventario = Inventario()
    # Lista de productos iniciales
    productos_iniciales = [
        Producto("001", "Laptop Dell", 200, 1500),
        Producto("002", "Smartphone iPhone 14", 150, 1200),
        Producto("005", "Smartwatch Apple", 250, 350),
        Producto("006", "Consola PlayStation 5", 100, 550),
        Producto("007", "Monitor Curvo LG", 200, 300),
        Producto("008", "Teclado Mecánico Razer", 400, 120),
        Producto("009", "Ratón Gaming Logitech", 350, 80),
        Producto("010", "Impresora HP", 150, 250),
        Producto("003", "Tablet Samsung", 100, 400),
        Producto("004", "Auriculares Sony", 500, 80),]

# Agregar productos iniciales al inventario
    for producto in productos_iniciales:
        inventario.añadir_producto(producto.get_id(), producto.get_nombre(), producto.get_cantidad(),
                                   producto.get_precio())

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar productos")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            if inventario.añadir_producto(id, nombre, cantidad, precio):
                print("Producto añadido exitosamente.")

        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
            print("Producto eliminado.")

        elif opcion == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            if inventario.actualizar_producto(id, cantidad, precio):
                print("Producto actualizado exitosamente.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            productos = inventario.buscar_productos(nombre)
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

"""Jeffrey Jose Mayorga Angos"""
if __name__ == "__main__":
    menu_principal()