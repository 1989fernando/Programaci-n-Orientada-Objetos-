# tienda_online.py

class Producto:
    """
    Clase que representa un producto en la tienda.
    """
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        """
        Reduce el stock del producto después de una compra.
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            print(f"No hay suficiente stock para {self.nombre}.")
            return False


class Cliente:
    """
    Clase que representa un cliente de la tienda.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []  # Lista de productos en el carrito

    def agregar_al_carrito(self, producto, cantidad):
        """
        Agrega un producto al carrito si hay suficiente stock.
        """
        if producto.reducir_stock(cantidad):
            self.carrito.append((producto, cantidad))
            print(f"{cantidad} unidades de {producto.nombre} han sido agregadas al carrito.")
        else:
            print(f"No se pudo agregar {producto.nombre} al carrito.")

    def ver_carrito(self):
        """
        Muestra los productos en el carrito.
        """
        print(f"Carrito de {self.nombre}:")
        for producto, cantidad in self.carrito:
            print(f"- {producto.nombre} x{cantidad} (${producto.precio * cantidad})")


class Tienda:
    """
    Clase que representa la tienda.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario de la tienda.
        """
        self.productos.append(producto)

    def listar_productos(self):
        """
        Lista los productos disponibles en la tienda.
        """
        print(f"Productos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(f"- {producto.nombre}: ${producto.precio} (Stock: {producto.stock})")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una tienda
    mi_tienda = Tienda("Tienda Online")

    # Agregar productos
    producto1 = Producto("Laptop", 1500, 10)
    producto2 = Producto("Auriculares", 50, 20)
    mi_tienda.agregar_producto(producto1)
    mi_tienda.agregar_producto(producto2)

    # Listar productos disponibles
    mi_tienda.listar_productos()

    # Crear un cliente
    cliente = Cliente("Juan")

    # Cliente agrega productos al carrito
    cliente.agregar_al_carrito(producto1, 2)  # Compra 2 laptops
    cliente.agregar_al_carrito(producto2, 5)  # Compra 5 auriculares

    # Ver carrito del cliente
    cliente.ver_carrito()

    # Ver inventario actualizado
    mi_tienda.listar_productos()
