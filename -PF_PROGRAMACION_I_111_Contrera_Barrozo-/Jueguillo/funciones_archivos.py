import json

def cargar_categorias_palabras(archivo_json):
    categorias_palabras = {}
    try:
        with open(archivo_json, 'r') as archivo:
            categorias_palabras = json.load(archivo)
    except Exception as e:
        print(f"Error al cargar categorías y palabras: {e}")
    return categorias_palabras

def guardar_categorias_palabras(archivo_json, categorias_palabras):
    try:
        with open(archivo_json, 'w') as archivo:
            json.dump(categorias_palabras, archivo, indent=4)
    except Exception as e:
        print(f"Error al guardar categorías y palabras: {e}")

def cargar_puntuacion(archivo_csv):
    puntuacion = 0
    try:
        with open(archivo_csv, 'r') as archivo:
            contenido = archivo.read().strip()
            if contenido.isdigit():
                puntuacion = int(contenido)
    except Exception as e:
        print(f"Error al cargar puntuación: {e}")
    return puntuacion

def guardar_puntuacion(archivo_csv, puntuacion):
    try:
        with open(archivo_csv, 'w') as archivo:
            archivo.write(str(puntuacion))
    except Exception as e:
        print(f"Error al guardar puntuación: {e}")