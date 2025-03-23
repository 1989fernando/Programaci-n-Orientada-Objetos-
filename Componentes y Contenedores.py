import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la entrada de datos
        frame_entrada = ttk.Frame(root, padding="10")
        frame_entrada.pack(fill=tk.X)

        # Fecha
        ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, sticky=tk.W)
        self.fecha = DateEntry(frame_entrada)
        self.fecha.grid(row=0, column=1)

        # Hora
        ttk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, sticky=tk.W)
        self.hora = ttk.Entry(frame_entrada)
        self.hora.grid(row=1, column=1)

        # Descripción
        ttk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, sticky=tk.W)
        self.descripcion = ttk.Entry(frame_entrada)
        self.descripcion.grid(row=2, column=1)

        # Botones
        frame_botones = ttk.Frame(root, padding="10")
        frame_botones.pack(fill=tk.X)

        ttk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT)
        ttk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).pack(side=tk.LEFT)
        ttk.Button(frame_botones, text="Salir", command=root.destroy).pack(side=tk.LEFT)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def agregar_evento(self):
        fecha = self.fecha.get()
        hora = self.hora.get()
        descripcion = self.descripcion.get()

        if fecha and hora and descripcion:
            self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
            self.fecha.delete(0, tk.END)
            self.hora.delete(0, tk.END)
            self.descripcion.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            respuesta = messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar el evento seleccionado?")
            if respuesta:
                for item in seleccion:
                    self.tree.delete(item)
        else:
            messagebox.showerror("Error", "Seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()