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

# 4. Graficado de resultados
plt.figure(figsize=(10, 6))
colors = sns.color_palette("husl", len(df))

plt.subplot(1, 2, 1)
plt.pie(df['Debito'], labels=df['Concepto'], autopct='%1.1f%%', colors=colors, startangle=80)
plt.title('Distribución de Gastos')

plt.subplot(1, 2, 2)
plt.barh(df['Concepto'], df['Debito'], color=colors)
plt.xlabel('Monto')
plt.title('Gastos por Concepto')
for i, v in enumerate(df['Debito']):
    plt.text(v + total_gastos * 0.01, i, f'${v:,}', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('grafico_gastos.png', dpi=150, bbox_inches='tight')
print("\nGráfico guardado como 'grafico_gastos.png'")
plt.close()
