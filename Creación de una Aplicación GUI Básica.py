import tkinter as tk

def agregar_dato():
    dato = entrada_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_dato.delete(0, tk.END)

def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")

# Componentes GUI
etiqueta_dato = tk.Label(ventana, text="Ingrese un dato:")
etiqueta_dato.pack()

entrada_dato = tk.Entry(ventana)
entrada_dato.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack()

lista_datos = tk.Listbox(ventana)
lista_datos.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

# Bucle principal de la aplicación
ventana.mainloop()