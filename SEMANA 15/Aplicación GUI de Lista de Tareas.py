import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Crear el campo de entrada para nuevas tareas
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

# Crear la lista de tareas
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Crear los botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_add_task = tk.Button(frame_buttons, text="Añadir Tarea", command=lambda: add_task())
button_add_task.pack(side=tk.LEFT)

button_complete_task = tk.Button(frame_buttons, text="Marcar como Completada", command=lambda: complete_task())
button_complete_task.pack(side=tk.LEFT)

button_delete_task = tk.Button(frame_buttons, text="Eliminar Tarea", command=lambda: delete_task())
button_delete_task.pack(side=tk.LEFT)
# Función para añadir una tarea
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

# Función para marcar una tarea como completada
def complete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(task_index)
        listbox_tasks.delete(task_index)
        listbox_tasks.insert(tk.END, task + " ✔")
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")

# Función para eliminar una tarea
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea.")
# Permitir añadir tareas con la tecla Enter
entry_task.bind("<Return>", lambda event: add_task())

# Ejecutar la aplicación
root.mainloop()
