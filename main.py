import pandas as pd
import random
from faker import Faker
import numpy as np
from datetime import date

fake = Faker("es_ES")  # nombres en español

# Definimos categorías y productos de supermercado con rangos de precios
productos = {
    "Granos": ["Arroz", "Frijoles", "Lentejas", "Garbanzo"],
    "Abarrotes": ["Aceite", "Azúcar", "Sal", "Café"],
    "Lácteos": ["Leche", "Queso", "Yogurt", "Mantequilla"],
    "Panadería": ["Pan", "Galletas", "Tortillas", "Pastel"],
    "Carnes": ["Pollo", "Carne de Res", "Cerdo", "Pescado"],
    "Frutas": ["Manzanas", "Bananas", "Naranjas", "Peras"],
    "Verduras": ["Papas", "Zanahorias", "Tomates", "Cebollas"],
    "Bebidas": ["Agua", "Jugo", "Refresco", "Cerveza"],
    "Aseo": ["Jabón", "Detergente", "Shampoo", "Papel Higiénico"]
}

ciudades = [
    "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
    "Cúcuta", "Bucaramanga", "Pereira", "Santa Marta", "Ibagué"
]

estados = ["Cerrado", "Pendiente", "Cancelado"]

# Cantidad de registros
n = 100_000

# Generación de datos
clientes = [fake.name() for _ in range(n)]
vendedores = [fake.name() for _ in range(n)]
ciudades_data = [random.choice(ciudades) for _ in range(n)]
estados_data = [random.choice(estados) for _ in range(n)]

# Fechas de 2025
start_date = date(2025, 1, 1)
end_date = date(2025, 12, 31)
fechas = [fake.date_between(start_date=start_date, end_date=end_date) for _ in range(n)]

# Selección de productos, categorías y precios aleatorios
categorias = []
producto_nombre = []
precio = []
for _ in range(n):
    categoria = random.choice(list(productos.keys()))
    categorias.append(categoria)
    prod = random.choice(productos[categoria])
    producto_nombre.append(prod)
    precio.append(random.randint(1000, 50000))  # precio aleatorio por unidad

cantidad = np.random.randint(1, 21, size=n)
valor_venta = [precio[i] * cantidad[i] for i in range(n)]
comision = [round(valor_venta[i] * 0.05, 2) for i in range(n)]

# Crear DataFrame
df = pd.DataFrame({
    "CLIENTE": clientes,
    "PRODUCTO": producto_nombre,
    "PRECIO": precio,
    "CANTIDAD": cantidad,
    "CIUDAD": ciudades_data,
    "VENDEDOR": vendedores,
    "FECHA": fechas,
    "ESTADO": estados_data,
    "VALOR_VENTA": valor_venta,
    "COMISION": comision,
    "CATEGORIA": categorias
})

# Guardar a CSV
df.to_csv("ventas_100k.csv", index=False, encoding="utf-8-sig")
print("Archivo generado: ventas_100k.csv ✅")
