import os
from dotenv import load_dotenv
from main import leer_y_ordenar_csv  # Importamos tu función del otro archivo

def iniciar_programa():
    # 1. Cargar las variables del archivo .env
    print(" Cargando variables de entorno...")
    load_dotenv()

    # 2. Obtener los valores (Si no existen, devuelve None)
    entrada = os.getenv('RUTA_ENTRADA')
    salida = os.getenv('RUTA_SALIDA')
    columna = os.getenv('COLUMNA_OBJETIVO')

    # Validación: Asegurarnos de que leímos bien el .env
    if not entrada or not salida:
        print(" Error: Faltan variables en el archivo .env")
        return

    print(f"   --> Archivo a leer: {entrada}")
    print(f"   --> Columna a ordenar: {columna}")

    # 3. Llamar a la función que ya tenías en main.py
    print(" Ejecutando proceso...")
    exito = leer_y_ordenar_csv(entrada, salida, columna)

    if exito:
        print(" ¡Proceso finalizado correctamente desde app.py!")
    else:
        print(" Hubo un problema en el proceso.")

if __name__ == "__main__":
    iniciar_programa()