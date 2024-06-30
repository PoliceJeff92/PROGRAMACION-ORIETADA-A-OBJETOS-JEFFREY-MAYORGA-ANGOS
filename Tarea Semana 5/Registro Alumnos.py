def registrar_alumno():
  """Función para registrar un nuevo alumno."""
  nombre = input("Ingrese el nombre del alumno: ")
  edad = int(input("Ingrese la edad del alumno: "))
  curso = input("Ingrese el curso del alumno: ")
  promedio = float(input("Ingrese el promedio del alumno: "))

  alumno = {
    "nombre": nombre,
    "edad": edad,
    "curso": curso,
    "promedio": promedio
  }

  return alumno

def mostrar_alumno(alumno):
  """Función para mostrar la información de un alumno."""
  print(f"Nombre: {alumno['nombre']}")
  print(f"Edad: {alumno['edad']}")
  print(f"Curso: {alumno['curso']}")
  print(f"Promedio: {alumno['promedio']}")

def main():
  """Función principal del programa."""
  alumno = registrar_alumno()
  mostrar_alumno(alumno)

"""Jeffrey Jose Mayorga Angos"""

if __name__ == "__main__":
  main()
