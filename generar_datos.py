import pandas as pd
import random

# Creamos datos ficticios
data = {
    'ID': range(1, 21),  # Del 1 al 20
    'Producto': [f'Producto {i}' for i in range(1, 21)],
    # Precios aleatorios
    'Valor': [random.randint(100, 5000) for i in range(20)],
    'Categoria': [random.choice(['A', 'B', 'C']) for i in range(20)]
}

df = pd.DataFrame(data)

# Guardamos el archivo que tu script main espera encontrar
df.to_csv('mis_datos_recolectados.csv', index=False)

print("¡Archivo 'mis_datos_recolectados.csv' creado con 20 filas!")
