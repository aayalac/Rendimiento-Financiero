# Rendimiento-Financiero

Herramienta para analizar el rendimiento financiero personal a partir de los ingresos y gastos registrados.

## Descripción

Este proyecto permite calcular y visualizar el desglose de gastos de un ciclo financiero (quincenal o mensual). A partir de un capital inicial y una lista de gastos, genera:

- **Total de gastos** del ciclo
- **Saldo disponible** después de los gastos
- **Porcentaje** que representa cada gasto respecto al total

## Estructura del proyecto

- `Rendimiento.py` - Script principal que procesa los datos y genera los cálculos
- `Datos.json` - Archivo de configuración con los datos de capital y gastos

## Formato de Datos.json

```json
{
    "Concepto": ["Gas", "Mercado", "Servicios", ...],
    "Debito": [50000, 150000, 80000, ...],
    "Capital": [2000000]
}
```

- `Concepto`: Lista de nombres de los gastos
- `Debito`: Montos de cada gasto (en la misma unidad)
- `Capital`: Capital total disponible para el ciclo

## Uso

1. Edita `Datos.json` con tus conceptos y montos de gasto, y tu capital
2. Ejecuta:

```bash
python Rendimiento.py
```

## Requisitos

- Python 3.8+
- pandas
- matplotlib
- seaborn

```bash
pip install pandas matplotlib seaborn
```
