class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    # Métodos para obtener y establecer atributos
    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio
import json

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos

    def añadir_producto(self, producto):
        if producto.obtener_id() in self.productos:
            print(f"El producto con ID {producto.obtener_id()} ya existe.")
        else:
            self.productos[producto.obtener_id()] = producto
            print(f"Producto {producto.obtener_nombre()} añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
        else:
            print(f"No se encontró ningún producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].establecer_precio(precio)
            print(f"Producto con ID {id_producto} actualizado exitosamente.")
        else:
            print(f"No se encontró ningún producto con ID {id_producto}.")

    def buscar_producto_por_nombre(self, nombre):
        productos_encontrados = [str(prod) for prod in self.productos.values() if nombre.lower() in prod.obtener_nombre().lower()]
        if productos_encontrados:
            for producto in productos_encontrados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_inventario(self, archivo):
        try:
            with open(archivo, 'w') as f:
                inventario_serializado = {id_producto: producto.__dict__ for id_producto, producto in self.productos.items()}
                json.dump(inventario_serializado, f, indent=4)
            print("Inventario guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                inventario_deserializado = json.load(f)
                for id_producto, datos_producto in inventario_deserializado.items():
                    self.productos[id_producto] = Producto(**datos_producto)
            print("Inventario cargado exitosamente.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
def menu():
    inventario = Inventario()

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar vacío si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (dejar vacío si no desea cambiarlo): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            archivo = input("Ingrese el nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(archivo)

        elif opcion == "7":
            archivo = input("Ingrese el nombre del archivo desde el que cargar el inventario: ")
            inventario.cargar_inventario(archivo)

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")
#Jeffrey Mayorga Angos
if __name__ == "__main__":
    menu()
