import pandas as pd

df = pd.read_csv("ventas_100k.csv")


# 1. ¿Cuántos registros (ventas) hay en total?
print("Total de registros (ventas)", len(df))

# 2. ¿Cuántas ventas fueron "Cerradas", "Pendientes" y "Canceladas"?
print("2.Ventas por estado \n", df["ESTADO"].value_counts())

# 3. ¿Cuál es el valor total de ventas realizadas?
print("3.Valor total de ventas", f"{df['VALOR_VENTA'].sum():,.0f}")

# 4. ¿Cuál es el promedio de comisión pagada por venta cerrada?
print("4.Promedio comisión en ventas cerradas", f"{df[df['ESTADO'] == 'Cerrado']['COMISION'].mean():,.2f}")

# 5. ¿Qué ciudad generó el mayor número de ventas cerradas?
print("5.Ciudad con mayor número de ventas cerradas \n",
      df[df['ESTADO'] == 'Cerrado']['CIUDAD'].value_counts().head(1))

# 6. ¿Cuál es el valor total de ventas por ciudad?
print("6.Valor total de ventas por ciudad \n",
      df.groupby('CIUDAD')['VALOR_VENTA'].sum())

# 7. ¿Cuáles son los 5 productos más vendidos (por número de registros)?
print("7.Top 5 productos más vendidos \n",
      df['PRODUCTO'].value_counts().head(5))

# 8. ¿Cuántos productos únicos fueron vendidos?
print("8.Cantidad de productos únicos vendidos", df['PRODUCTO'].nunique())

# 9. ¿Cuál es el vendedor con mayor número de ventas cerradas?
print("9.Vendedor con mayor número de ventas cerradas \n",
      df[df['ESTADO'] == 'Cerrado']['VENDEDOR'].value_counts().head(1))

# 10. ¿Cuál es la venta con el mayor valor y qué cliente la realizó?
print("10.Venta con mayor valor \n",
      df.loc[df['VALOR_VENTA'].idxmax(), ['CLIENTE', 'VALOR_VENTA']])

# --- Conversión de FECHA a datetime (para evitar errores con .dt) ---
df['FECHA'] = pd.to_datetime(df['FECHA'], errors='coerce')

# 11. ¿Existen ventas con valor o comisión nula o negativa?
ventas_valor_invalidas = df[(df['VALOR_VENTA'] <= 0) | (df['VALOR_VENTA'].isna())]
ventas_comision_invalidas = df[(df['COMISION'] <= 0) | (df['COMISION'].isna())]
print("11.")
print("Ventas con valor nulo o negativo (muestra):\n", ventas_valor_invalidas.head())
print("Cantidad de ventas con valor nulo o negativo:", len(ventas_valor_invalidas))

print("Ventas con comisión nula o negativa (muestra):\n", ventas_comision_invalidas.head())
print("Cantidad de ventas con comisión nula o negativa:", len(ventas_comision_invalidas))

# 12. ¿Cuál es la media de ventas por mes?
print("12.Media de ventas por mes \n",
      df.groupby(df['FECHA'].dt.month)['VALOR_VENTA'].mean())

# 13. ¿Cuál fue el mes con más ventas cerradas?
print("13.Mes con más ventas cerradas \n",
      df[df['ESTADO'] == 'Cerrado'].groupby(df['FECHA'].dt.month)['VALOR_VENTA'].count().idxmax())

# 14. ¿Cuántas ventas se realizaron en cada trimestre del año?
print("14.Ventas por trimestre \n",
      df.groupby(df['FECHA'].dt.to_period('Q'))['VALOR_VENTA'].count())

# 15. ¿Qué productos han sido vendidos en más de 3 ciudades diferentes?
print("15.Productos vendidos en más de 3 ciudades \n",
      df.groupby('PRODUCTO')['CIUDAD'].nunique()[df.groupby('PRODUCTO')['CIUDAD'].nunique() > 3])

# 16. ¿Existen duplicados en los datos? ¿Cómo los identificarías?
print("16.")
print("Cantidad de filas duplicadas:", df.duplicated().sum())
print("Filas duplicadas (muestra):\n", df[df.duplicated()].head())

# 17. Eliminar las filas que tengan valores nulos en columnas clave (CLIENTE, PRODUCTO, VALOR_VENTA).
df = df.dropna(subset=['CLIENTE', 'PRODUCTO', 'VALOR_VENTA'])
print("17.Cantidad de registros después de eliminar nulos en columnas clave:", len(df))

# 18. Crear nueva columna UTILIDAD (95% del VALOR_VENTA) y analizar cuál producto dejó mayor utilidad total.
df['UTILIDAD'] = df['VALOR_VENTA'] * 0.95
print("18.Producto con mayor utilidad total \n",
      df.groupby('PRODUCTO')['UTILIDAD'].sum().sort_values(ascending=False).head(1))

# ✅ ¿Cuál es el valor total de ventas por ciudad?
print("Valor total de ventas por ciudad \n",
      df.groupby('CIUDAD')['VALOR_VENTA'].sum())

# ✅ ¿Cuál es el promedio de comisión por vendedor?
print("Promedio de comisión por vendedor \n",
      df.groupby('VENDEDOR')['COMISION'].mean())

# ✅ ¿Cuál es el número de ventas por estado y por ciudad?
print("Número de ventas por estado y ciudad \n",
      df.groupby(['ESTADO', 'CIUDAD'])['VALOR_VENTA'].count())

# ✅ ¿Qué categoría de producto tiene el mayor valor de ventas?
print("Categoría con mayor valor total de ventas \n",
      df.groupby('CATEGORIA')['VALOR_VENTA'].sum().sort_values(ascending=False).head(1))

# ✅ ¿Cuál es el total de ventas mensuales por ciudad?
print("Total de ventas mensuales por ciudad \n",
      df.groupby([df['FECHA'].dt.to_period('M'), 'CIUDAD'])['VALOR_VENTA'].sum())

# ✅ ¿Cuántas ventas cerradas hizo cada vendedor por ciudad?
print("Ventas cerradas por vendedor y ciudad \n",
      df[df['ESTADO'] == 'Cerrado'].groupby(['VENDEDOR', 'CIUDAD'])['VALOR_VENTA'].count())
