class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Usamos una tupla para los atributos inmutables
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo_autor[0]}' por {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para los libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        libros = ', '.join([libro.titulo_autor[0] for libro in self.libros_prestados]) or "No tiene libros prestados"
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {libros}"
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y Usuario como valor
        self.historial_prestamos = []  # Lista para registrar el historial de préstamos

    def añadir_libro(self, libro):
        if libro.isbn in self.libros_disponibles:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido con éxito.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"El usuario con ID {id_usuario} no se encuentra registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return
        if isbn not in self.libros_disponibles:
            print(f"Libro con ISBN {isbn} no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros_disponibles.pop(isbn)
        usuario.prestar_libro(libro)
        self.historial_prestamos.append((id_usuario, isbn))
        print(f"Libro '{libro.titulo_autor[0]}' prestado a '{usuario.nombre}'.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        libro = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
        if libro:
            usuario.devolver_libro(libro)
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' devuelto por '{usuario.nombre}'.")
        else:
            print(f"El usuario no tiene prestado el libro con ISBN {isbn}.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (titulo and titulo.lower() in libro.titulo_autor[0].lower()) or \
               (autor and autor.lower() in libro.titulo_autor[1].lower()) or \
               (categoria and categoria.lower() == libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            print(f"Libros prestados por {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"  - {libro}")
        else:
            print(f"Usuario con ID {id_usuario} no registrado.")
# Crear biblioteca
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Ficción", "1234567890")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Ficción", "0987654321")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("María García", "002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("001", "1234567890")
biblioteca.listar_libros_prestados("001")
biblioteca.devolver_libro("001", "1234567890")
biblioteca.listar_libros_prestados("001")

"""Jeffrey Jose Mayorga Angos"""
# Buscar libros
resultados = biblioteca.buscar_libro(titulo="Soledad")
for libro in resultados:
    print(libro)
