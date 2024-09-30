import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        # Configuración inicial de la ventana principal
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        # Crear un marco para organizar los widgets
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        # Campo de entrada para añadir nuevas tareas
        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=0, padx=10)
        # Asignar la función add_task al evento de presionar "Enter"
        self.task_entry.bind("<Return>", self.add_task)

        # Botón para añadir tareas
        self.add_button = tk.Button(self.frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Botón para marcar tareas como completadas
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tareas
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Asignar atajos de teclado para completar y eliminar tareas, y cerrar la aplicación
        self.root.bind("<c>", self.complete_task)
        self.root.bind("<d>", self.delete_task)
        self.root.bind("<Escape>", lambda event: root.quit())

    def add_task(self, event=None):
        # Obtener el texto del campo de entrada
        task = self.task_entry.get()
        if task != "":
            # Añadir la tarea a la lista si no está vacía
            self.task_listbox.insert(tk.END, task)
            # Limpiar el campo de entrada
            self.task_entry.delete(0, tk.END)
        else:
            # Mostrar advertencia si se intenta añadir una tarea vacía
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self, event=None):
        try:
            # Obtener el índice de la tarea seleccionada
            selected_task_index = self.task_listbox.curselection()[0]
            # Obtener el texto de la tarea seleccionada
            task = self.task_listbox.get(selected_task_index)
            # Eliminar la tarea de la lista
            self.task_listbox.delete(selected_task_index)
            # Añadir la tarea como completada al final de la lista
            self.task_listbox.insert(tk.END, f"{task} - Completada")
        except IndexError:
            # Mostrar advertencia si no hay ninguna tarea seleccionada
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            # Obtener el índice de la tarea seleccionada
            selected_task_index = self.task_listbox.curselection()[0]
            # Eliminar la tarea de la lista
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            # Mostrar advertencia si no hay ninguna tarea seleccionada
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    # Crear la ventana principal y ejecutar la aplicación
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
