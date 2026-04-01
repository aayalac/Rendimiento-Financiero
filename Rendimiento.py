import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar los datos desde el archivo JSON
with open('Datos.json', encoding='utf-8') as f:
    raw = json.load(f)

datos = {
    'Concepto': raw['Concepto'],
    'Debito': raw['Debito'],
}

capital = raw['Capital'][0]

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