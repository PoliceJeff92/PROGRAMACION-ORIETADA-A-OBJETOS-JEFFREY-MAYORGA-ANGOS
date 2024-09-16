import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Crear el Treeview para mostrar los eventos
tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Crear los campos de entrada
tk.Label(root, text="Fecha:").pack()
date_entry = DateEntry(root)
date_entry.pack()

tk.Label(root, text="Hora:").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Label(root, text="Descripción:").pack()
desc_entry = tk.Entry(root)
desc_entry.pack()

# Crear los botones
def add_event():
    tree.insert("", "end", values=(date_entry.get(), time_entry.get(), desc_entry.get()))

def delete_event():
    selected_item = tree.selection()[0]
    tree.delete(selected_item)

tk.Button(root, text="Agregar Evento", command=add_event).pack()
tk.Button(root, text="Eliminar Evento Seleccionado", command=delete_event).pack()
tk.Button(root, text="Salir", command=root.quit).pack()

root.mainloop()

# Crear un frame para los campos de entrada
input_frame = tk.Frame(root)
input_frame.pack()

tk.Label(input_frame, text="Fecha:").grid(row=0, column=0)
date_entry = DateEntry(input_frame)
date_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Hora:").grid(row=1, column=0)
time_entry = tk.Entry(input_frame)
time_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Descripción:").grid(row=2, column=0)
desc_entry = tk.Entry(input_frame)
desc_entry.grid(row=2, column=1)

# Crear un frame para los botones
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Agregar Evento", command=add_event).grid(row=0, column=0)
tk.Button(button_frame, text="Eliminar Evento Seleccionado", command=delete_event).grid(row=0, column=1)
tk.Button(button_frame, text="Salir", command=root.quit).grid(row=0, column=2)
# Función para agregar un evento a la lista
def add_event():
    # Insertar el evento en el Treeview
    tree.insert("", "end", values=(date_entry.get(), time_entry.get(), desc_entry.get()))

# Función para eliminar el evento seleccionado
def delete_event():
    # Obtener el elemento seleccionado
    selected_item = tree.selection()[0]
    # Eliminar el elemento del Treeview
    tree.delete(selected_item)

