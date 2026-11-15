#conversion de soles a dolares
tipo_cambio = 3.78

monto1 = 180.00
monto2 = 340.00
monto3 = 500.00

# Conversiones individuales
usd1 = monto1 / tipo_cambio
usd2 = monto2 / tipo_cambio
usd3 = monto3 / tipo_cambio

# Totales
total_soles = monto1 + monto2 + monto3
total_usd = total_soles / tipo_cambio

# Conversión
print(f"Tipo de cambio: S/{tipo_cambio:.2f}")
print(f"Monto 1: S/{monto1:.2f} = USD {usd1:.2f}")
print(f"Monto 2: S/{monto2:.2f} = USD {usd2:.2f}")
print(f"Monto 3: S/{monto3:.2f} = USD {usd3:.2f}")
print(f"Total en soles: S/{total_soles:.2f}")
print(f"Total en dólares: USD {total_usd:.2f}")