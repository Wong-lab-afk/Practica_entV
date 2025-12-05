import pandas as pd
import os

# Configuración
ARCHIVO_ENTRADA = 'mis_datos_recolectados.csv' # El archivo que generaste o conseguiste
COLUMNA_PARA_ORDENAR = 'Valor' # Cambia esto por el nombre REAL de tu columna (ej: 'Edad', 'Precio')

def main():
    # 1. Verificar si el archivo existe antes de leer
    if not os.path.exists(ARCHIVO_ENTRADA):
        print(f"Error: No encuentro el archivo '{ARCHIVO_ENTRADA}'")
        return

    print("--- Leyendo archivo CSV ---")
    df = pd.read_csv(ARCHIVO_ENTRADA)

    # 2. Ordenar los datos
    # ascending=True es de menor a mayor (A-Z, 0-9)
    # ascending=False es de mayor a menor (Z-A, 9-0)
    print(f"--- Ordenando por la columna: {COLUMNA_PARA_ORDENAR} ---")
    
    try:
        df_ordenado = df.sort_values(by=COLUMNA_PARA_ORDENAR, ascending=False)
        
        # 3. Mostrar resultados
        print(df_ordenado.head(10)) # Muestra las primeras 10 filas

        # Opcional: Guardar el resultado ordenado
        df_ordenado.to_csv('datos_ordenados.csv', index=False)
        print("\nSe ha guardado el archivo ordenado como 'datos_ordenados.csv'")

    except KeyError:
        print(f"Error: La columna '{COLUMNA_PARA_ORDENAR}' no existe en el CSV.")
        print(f"Columnas disponibles: {list(df.columns)}")

if __name__ == "__main__":
    main()

# --- 1. Definición de la Función ---
def leer_y_ordenar_csv(ruta_entrada, ruta_salida, columna_orden):
    """
    Lee un CSV, lo ordena por la columna especificada y guarda el resultado.
    Retorna True si funcionó, False si falló.
    """
    # Verificación de seguridad
    if not os.path.exists(ruta_entrada):
        print(f" Error: El archivo '{ruta_entrada}' no existe.")
        return False

    try:
        print(f" Leyendo archivo: {ruta_entrada}...")
        df = pd.read_csv(ruta_entrada)

        print(f" Ordenando datos por: '{columna_orden}' (Mayor a menor)...")
        # Aquí ocurre la magia del ordenamiento
        df_ordenado = df.sort_values(by=columna_orden, ascending=False)

        # Mostrar una vista previa en consola
        print("\n--- Vista Previa (Top 5) ---")
        print(df_ordenado.head(5))
        print("----------------------------\n")

        # Guardar el resultado
        df_ordenado.to_csv(ruta_salida, index=False)
        print(f"¡Éxito! Archivo guardado en: {ruta_salida}")
        return True

    except KeyError:
        print(f"Error: La columna '{columna_orden}' no existe en el archivo.")
        print(f"Columnas disponibles: {list(df.columns)}")
        return False
    except Exception as e:
        print(f" Error inesperado: {e}")
        return False

# --- 2. Bloque Principal (Execution) ---
if __name__ == "__main__":
    # Configuración de nombres de archivo
    INPUT = 'mis_datos_recolectados.csv'
    OUTPUT = 'datos_ordenados.csv'
    COLUMNA = 'Valor' # Cambia esto si quieres ordenar por 'ID' o 'Categoria'

    # Llamada a la función
    leer_y_ordenar_csv(INPUT, OUTPUT, COLUMNA)