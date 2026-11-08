# Ejercicio 10: Agenda de contactos

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        for contacto in self.contactos:
            if contacto["dni"] == dni:
                print(f"Error: Ya existe un contacto registrado con el DNI {dni}.")
                return False

        nuevo_contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "dni": dni
        }
        self.contactos.append(nuevo_contacto)
        print(f"Contacto '{nombre}' agregado exitosamente.")
        return True

    def mostrar_contactos(self):
        print("\n--- LISTA DE CONTACTOS EN LA AGENDA ---")
        if not self.contactos:
            print("La agenda está vacía.")
        for c in self.contactos:
            print(f"Nombre: {c['nombre']} | Teléfono: {c['telefono']} | Email: {c['email']} | DNI: {c['dni']}")
        print("-" * 40)

    def buscar_por_dni(self, dni):
        for c in self.contactos:
            if c["dni"] == dni:
                print(f"\n[Búsqueda DNI {dni}] ¡Encontrado!")
                print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}")
                return c
        print(f"\n[Búsqueda DNI {dni}] No se encontraron coincidencias.")
        return None


# Instanciar la agenda y agregar al menos tres contactos
mi_agenda = Agenda()
mi_agenda.agregar_contacto("Carlos Flores", "987654321", "carlos@mail.com", "72345678")
mi_agenda.agregar_contacto("Ana Gomez", "912345678", "ana@mail.com", "73456789")
mi_agenda.agregar_contacto("Luis Perez", "998877665", "luis@mail.com", "74567890")

# Intentar duplicar DNI para probar validación
mi_agenda.agregar_contacto("Pedro Copia", "911111111", "pedro@mail.com", "72345678")

# Mostrar la agenda completa
mi_agenda.mostrar_contactos()

# Ejecutar dos búsquedas: una existente y otra inexistente
mi_agenda.buscar_por_dni("73456789")  # Existente
mi_agenda.buscar_por_dni("00000000")  # Inexistente