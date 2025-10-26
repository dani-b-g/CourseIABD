# Programa principal: Trabajo con conjuntos

if __name__ == "__main__":
    print("=== Trabajo con Conjuntos ===\n")

    # Pedir las dos listas al usuario
    print("Introduce las dos listas de números:\n")
    lista1 = input("Primera lista de números (separados por espacios): ").strip().split()
    lista2 = input("Segunda lista de números (separados por espacios): ").strip().split()

    # Convierto los numeros a enteros
    lista1 = [int(x) for x in lista1]
    lista2 = [int(x) for x in lista2]

    # Convertir las listas en conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Calcular los resultados con operaciones de conjuntos
    # NOTA: importante operadores nuevos que no conocia.
    # & para encontrar la intersección AKA elementos comunes
    # | para la unión AKA todos los elementos sin duplicados
    # ^ para la diferencia simétrica AKA elementos en uno u otro conjunto pero no en ambos
    interseccion = conjunto1 & conjunto2
    union = conjunto1 | conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2

    # Crear el diccionario con los resultados
    resultados = {
        "interseccion": interseccion,
        "union": union,
        "diferencia_simetrica": diferencia_simetrica
    }

    # Mostrar resultados
    print("\n=== Resultados ===")
    for clave, valor in resultados.items():
        print(f"{clave}: {valor}")
