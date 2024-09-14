"""
Aplicación GUI para gestionar datos.

Esta aplicación permite a los usuarios agregar información a través de un campo de texto y un botón "Agregar".
La información se muestra en una tabla dentro de la GUI. También incluye un botón "Limpiar" que borra la información ingresada.

Componentes:
- Etiqueta: "Ingrese información:"
- Campo de texto para ingresar datos.
- Botón "Agregar" para añadir datos a la tabla.
- Botón "Limpiar" para borrar los datos de la tabla.
- Tabla para mostrar los datos agregados.

Eventos:
- Clic en el botón "Agregar" llama a la función add_data.
- Clic en el botón "Limpiar" llama a la función clear_data.

Uso:
- Ejecute el script para abrir la aplicación GUI.
- Ingrese información en el campo de texto y haga clic en "Agregar" para añadirla a la tabla.
- Haga clic en "Limpiar" para borrar todos los datos de la tabla.
"""

import tkinter as tk
from tkinter import ttk

class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Datos")

        # Etiqueta y campo de texto
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=5)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        # Botón Agregar
        self.add_button = tk.Button(root, text="Agregar", command=self.add_data)
        self.add_button.pack(pady=5)

        # Botón Limpiar
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_data)
        self.clear_button.pack(pady=5)

        # Tabla para mostrar datos
        self.tree = ttk.Treeview(root, columns=("Datos"), show='headings')
        self.tree.heading("Datos", text="Datos")
        self.tree.pack(pady=5)

    def add_data(self):
        data = self.entry.get()
        if data:
            self.tree.insert("", "end", values=(data,))
            self.entry.delete(0, tk.END)

    def clear_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
