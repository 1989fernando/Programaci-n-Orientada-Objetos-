import os

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, {self.cantidad}, {self.precio}"

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario()

    def agregar_producto(self, producto):
        self.productos[producto.nombre] = producto
        self.guardar_inventario()
        print(f"Producto '{producto.nombre}' añadido con éxito.")

    def actualizar_producto(self, nombre, cantidad, precio):
        if nombre in self.productos:
            self.productos[nombre].cantidad = cantidad
            self.productos[nombre].precio = precio
            self.guardar_inventario()
            print(f"Producto '{nombre}' actualizado con éxito.")
        else:
            print(f"Error: Producto '{nombre}' no encontrado.")

    def eliminar_producto(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado con éxito.")
        else:
            print(f"Error: Producto '{nombre}' no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as archivo:
                for producto in self.productos.values():
                    archivo.write(f"{producto.nombre},{producto.cantidad},{producto.precio}\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def cargar_inventario(self):
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            return

        try:
            with open(self.archivo, "r") as archivo:
                for linea in archivo:
                    nombre, cantidad, precio = linea.strip().split(",")
                    self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
            print("Inventario cargado con éxito.")
        except FileNotFoundError:
            print("Error: Archivo de inventario no encontrado.")
        except ValueError:
            print("Error: Archivo de inventario corrupto. Se creará uno nuevo.")
            self.productos = {}  # Reiniciar el inventario si el archivo está corrupto
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

def main():
    inventario = Inventario()

    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(nombre, cantidad, precio))
        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "4":
            inventario.mostrar_inventario()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()