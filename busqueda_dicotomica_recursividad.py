def busqueda_dicotomica(tabla, elemento, inicio=0, fin=None):
    if fin is None:
        fin = len(tabla) - 1

    if inicio > fin:
        return -1  # Elemento no encontrado

    medio = (inicio + fin) // 2

    if tabla[medio] == elemento:
        return medio  # Elemento encontrado en la posición medio

    if tabla[medio] < elemento:
        return busqueda_dicotomica(tabla, elemento, medio + 1, fin)
    else:
        return busqueda_dicotomica(tabla, elemento, inicio, medio - 1)

# Solicitar al usuario ingresar la lista de elementos ordenados
def menu():
    print("Bienvenido a la búsqueda dicotómica")
    print("Seleccione una opción:")
    print("1. Ingresar la lista de elementos ordenados")
    print("2. Ingresar el elemento a buscar")
    print("3. Salir")
    opcion = int(input("Opción: "))
    return opcion

elementos_ordenados = []
elemento_buscado = None

while True:
    opcion = menu()

    if opcion == 1:
        elementos_ordenados = input("Ingrese la lista de elementos ordenados separados por espacios: ").split()
        elementos_ordenados = [int(e) for e in elementos_ordenados]
    elif opcion == 2:
        if not elementos_ordenados:
            print("Por favor, primero ingrese la lista de elementos ordenados.")
        else:
            elemento_buscado = int(input("Ingrese el elemento que desea buscar: "))
            indice = busqueda_dicotomica(elementos_ordenados, elemento_buscado)
            if indice != -1:
                print(f"El elemento {elemento_buscado} se encuentra en la posición {indice+1}.")
            else:
                print(f"El elemento {elemento_buscado} no se encuentra en la lista.")
    elif opcion == 3:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")



