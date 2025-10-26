import string

def frecuencia_palabras(lista_palabras, ruta_fichero):

    # Inicializamos 
    frecuencias = {palabra.lower(): 0 for palabra in lista_palabras}

    # Leemos el fichero
 
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        texto = f.read().lower()  # convertir a minúsculas


    # Eliminamos signos que interfieran
    for signo in string.punctuation:
        texto = texto.replace(signo, " ")

    # array de las palabras del texto
    palabras_en_texto = texto.split()

    # Contamos las frecuencias
    for palabra in palabras_en_texto:
        if palabra in frecuencias:
            frecuencias[palabra] += 1

    # Devolvemos el diccionario ordenado
    return dict(sorted(frecuencias.items()))


#  MAIN
if __name__ == "__main__":
    # Palabras a buscar
    lista = ["python", "programa", "texto", "frecuencia", "palabra", "ejemplo", "diccionario"]

    # Ruta al archivo de texto
    ruta = input("Introduce la ruta del archivo de texto: ").strip()

    try:
        resultado = frecuencia_palabras(lista, ruta)

        print("Frecuencia de palabras:\n")
        for palabra, frecuencia in resultado.items():
            print(f"{palabra}: {frecuencia}")
    except FileNotFoundError:
        print(f"El archivo {ruta} no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo {ruta  }: {e}")
