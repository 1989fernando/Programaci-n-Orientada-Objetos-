class CuentaBancaria:
    """Representa una cuenta bancaria con un saldo inicial y la capacidad de realizar depósitos y retiros."""

    def __init__(self, titular, saldo_inicial=0):
        """Constructor de la clase CuentaBancaria.

        Args:
            titular (str): Nombre del titular de la cuenta.
            saldo_inicial (float, optional): Saldo inicial de la cuenta. Defaults to 0.
        """
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Se ha creado una cuenta para {self.titular} con un saldo inicial de {self.saldo}")

    def depositar(self, cantidad):
        """Deposita una cantidad de dinero en la cuenta.

        Args:
            cantidad (float): Cantidad a depositar.
        """
        self.saldo += cantidad
        print(f"Se han depositado {cantidad} unidades. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        """Retira una cantidad de dinero de la cuenta, si es posible.

        Args:
            cantidad (float): Cantidad a retirar.
        """
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} unidades. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes")

    def __del__(self):
        """Destructor de la clase CuentaBancaria.
        Imprime un mensaje indicando que la cuenta ha sido cerrada.
        """
        print(f"La cuenta de {self.titular} ha sido cerrada.")

# Ejemplo de uso:
cuenta1 = CuentaBancaria("Juan Pérez", 1000)
cuenta1.depositar(500)
cuenta1.retirar(200)
# Cuando el objeto cuenta1 deje de ser utilizado, se llamará al destructor