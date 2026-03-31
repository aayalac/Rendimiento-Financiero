import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Definir los datos
datos = {
    'Concepto': ['Gas', 'Claro', 'Mercado', 'HVTV', 'Mercado Mama', 
                 'Administracion', 'Abono gafas', 'Retenedores', 'Cuota'],
    'Debito': [100000, 81049, 150000, 83000, 150000, 194000, 430000, 150000, 1000000]
}

capital = 2367888

# 2. Crear el DataFrame (la tabla de Python)
df = pd.DataFrame(datos)

# 3. Cálculos rápidos
total_gastos = df['Debito'].sum()
saldo_ciclo = capital - total_gastos
df['Porcentaje %'] = (df['Debito'] / total_gastos * 100).round(2)

print(f"Total Gastos: ${total_gastos:,}")
print(f"Saldo del Ciclo: ${saldo_ciclo:,}")
print("\nDesglose de Gastos:")
print(df)