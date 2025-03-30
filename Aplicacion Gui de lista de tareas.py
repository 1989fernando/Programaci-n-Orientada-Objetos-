import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Variables
        self.tareas = []
        self.tarea_entry = tk.Entry(root, width=40)
        self.tarea_entry.grid(row=0, column=0, padx=10, pady=10)

        # Botones
        self.agregar_btn = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.agregar_btn.grid(row=0, column=1, padx=5, pady=10)

        self.completar_btn = tk.Button(root, text="Marcar como Completada", command=self.completar_tarea)
        self.completar_btn.grid(row=1, column=1, padx=5, pady=10)

        self.eliminar_btn = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.eliminar_btn.grid(row=2, column=1, padx=5, pady=10)

        # Lista de tareas
        self.tareas_listbox = tk.Listbox(root, width=50, height=10)
        self.tareas_listbox.grid(row=1, column=0, rowspan=3, padx=10, pady=10)

        # Manejo de eventos
        self.tarea_entry.bind("<Return>", lambda event: self.agregar_tarea())  # Añadir tarea con Enter
        self.tareas_listbox.bind("<Double-1>", lambda event: self.completar_tarea()) # Opcional: Doble clic para completar

        self.actualizar_lista()

    def agregar_tarea(self):
        tarea = self.tarea_entry.get()
        if tarea:
            self.tareas.append({"tarea": tarea, "completada": False})
            self.tarea_entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def completar_tarea(self):
        seleccion = self.tareas_listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = True
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para completar.")

    def eliminar_tarea(self):
        seleccion = self.tareas_listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def actualizar_lista(self):
        self.tareas_listbox.delete(0, tk.END)
        for tarea_info in self.tareas:
            tarea = tarea_info["tarea"]
            if tarea_info["completada"]:
                tarea += " (Completada)"
            self.tareas_listbox.insert(tk.END, tarea)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()