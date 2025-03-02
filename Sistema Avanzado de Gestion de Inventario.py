import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getter y setter
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_nombre(self): return self.nombre
    def set_nombre(self, nombre): self.nombre = nombre
    def get_cantidad(self): return self.cantidad
    def set_cantidad(self, cantidad): self.cantidad = cantidad
    def get_precio(self): return self.precio
    def set_precio(self, precio): self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado.")

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].set_cantidad(nueva_cantidad)
        else:
            print("Producto no encontrado.")

    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].set_precio(nuevo_precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre_producto):
        resultados = [producto for producto in self.productos.values() if nombre_producto.lower() in producto.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            productos_serializados = {id: producto.__dict__ for id, producto in self.productos.items()}
            json.dump(productos_serializados,archivo)

    def cargar_inventario(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                productos_serializados = json.load(archivo)
                for id, datos_producto in productos_serializados.items():
                    self.productos[int(id)] = Producto(**datos_producto)
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Creando uno nuevo.")

# Interfaz de usuario
def menu():
    inventario = Inventario()
    inventario.cargar_inventario("inventario.json")

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar producto")
        print("6. Mostrar inventario")
        print("7. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = int(input("ID del producto: "))
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(id, cantidad)
        elif opcion == "4":
            id = int(input("ID del producto: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_precio(id, precio)
        elif opcion == "5":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "6":
            inventario.mostrar_inventario()
        elif opcion == "7":
            inventario.guardar_inventario("inventario.json")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()