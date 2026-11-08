# Ejercicio 09: Cuenta bancaria

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        if saldo_inicial >= 0:
            self.saldo = saldo_inicial
        else:
            self.saldo = 0
            print("El saldo inicial no puede ser negativo. Se inicializa en 0.")

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso de S/{monto:.2f}. Saldo actual: S/{self.saldo:.2f}")
        else:
            print(f"Error: No se puede depositar S/{monto:.2f}. El monto debe ser mayor a cero.")

    def retirar(self, monto):
        if monto <= 0:
            print(f"Error: No se puede retirar S/{monto:.2f}. El monto debe ser mayor a cero.")
        elif monto > self.saldo:
            print(f"Error: Retiro denegado de S/{monto:.2f}. Saldo insuficiente (Disponible: S/{self.saldo:.2f}).")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso de S/{monto:.2f}. Saldo actual: S/{self.saldo:.2f}")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo final: S/{self.saldo:.2f}")

# Instanciar cuenta con María López y S/500 iniciales
cuenta_maria = CuentaBancaria("María López", 500)

print("\n--- Ejecutando depósitos ---")
cuenta_maria.depositar(150)
cuenta_maria.depositar(-50)
cuenta_maria.depositar(200)

print("\n--- Ejecutando intentos de retiro ---")
cuenta_maria.retirar(100)
cuenta_maria.retirar(1000)
cuenta_maria.retirar(0)

print("\n--- Estado Final ---")
cuenta_maria.mostrar_saldo()
