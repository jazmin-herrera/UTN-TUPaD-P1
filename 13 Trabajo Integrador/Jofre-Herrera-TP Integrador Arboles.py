def crear_nodo(valor):
    return [valor, None, None]  # [valor, izquierda, derecha]

def buscar_nodo(nodo, valor):
    if nodo is None:
        return None
    if nodo[0] == valor:
        return nodo
    izq = buscar_nodo(nodo[1], valor)
    if izq:
        return izq
    return buscar_nodo(nodo[2], valor)

def buscar_padre(nodo, valor, padre=None, direccion=None):
    if nodo is None:
        return None, None
    if nodo[0] == valor:
        return padre, direccion
    encontrado, dir_izq = buscar_padre(nodo[1], valor, nodo, 1)
    if encontrado:
        return encontrado, dir_izq
    return buscar_padre(nodo[2], valor, nodo, 2)

def insertar_izquierda(nodo_padre, valor):
    if nodo_padre[1] is None:
        nodo_padre[1] = crear_nodo(valor)
    else:
        nuevo_nodo = crear_nodo(valor)
        nuevo_nodo[1] = nodo_padre[1]
        nodo_padre[1] = nuevo_nodo

def insertar_derecha(nodo_padre, valor):
    if nodo_padre[2] is None:
        nodo_padre[2] = crear_nodo(valor)
    else:
        nuevo_nodo = crear_nodo(valor)
        nuevo_nodo[2] = nodo_padre[2]
        nodo_padre[2] = nuevo_nodo

def eliminar_nodo(padre, direccion):
    hijo = padre[direccion]
    if hijo is None:
        print("No hay nodo para eliminar.")
        return
    if hijo[1] is None and hijo[2] is None:
        padre[direccion] = None
    elif hijo[1] is not None and hijo[2] is None:
        padre[direccion] = hijo[1]
    elif hijo[1] is None and hijo[2] is not None:
        padre[direccion] = hijo[2]
    else:
        print("No se puede eliminar un nodo con dos hijos.")

def contar_hojas(nodo):
    if nodo is None:
        return 0
    if nodo[1] is None and nodo[2] is None:
        return 1
    return contar_hojas(nodo[1]) + contar_hojas(nodo[2])

def altura(nodo):
    if nodo is None:
        return 0
    alt_izq = altura(nodo[1])
    alt_der = altura(nodo[2])
    return 1 + max(alt_izq, alt_der)

def preorden(nodo):
    if nodo:
        print(nodo[0], end=" ")
        preorden(nodo[1])
        preorden(nodo[2])

def inorden(nodo):
    if nodo:
        inorden(nodo[1])
        print(nodo[0], end=" ")
        inorden(nodo[2])

def postorden(nodo):
    if nodo:
        postorden(nodo[1])
        postorden(nodo[2])
        print(nodo[0], end=" ")

# Visualización del árbol
def visualizar(nodo, prefijo="", es_izquierda=True):
    if nodo is not None:
        if nodo[2] is not None:
            visualizar(nodo[2], prefijo + ("│   " if es_izquierda else "    "), False)
        print(prefijo + ("└── " if es_izquierda else "┌── ") + str(nodo[0]))
        if nodo[1] is not None:
            visualizar(nodo[1], prefijo + ("    " if es_izquierda else "│   "), True)

# Menú principal
def main():
    raiz_valor = input("Ingresa el valor de la raíz: ")
    arbol = crear_nodo(raiz_valor)

    while True:
        print("\nOpciones:")
        print("1. Insertar a la izquierda")
        print("2. Insertar a la derecha")
        print("3. Visualizar árbol")
        print("4. Recorrido preorden")
        print("5. Recorrido inorden")
        print("6. Recorrido postorden")
        print("7. Eliminar nodo (hoja o con un hijo)")
        print("8. Contar hojas")
        print("9. Calcular altura")
        print("10. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion in ["1", "2"]:
            valor_padre = input("Ingresa el valor del nodo padre: ")
            nodo_padre = buscar_nodo(arbol, valor_padre)
            if nodo_padre:
                nuevo_valor = input("Ingresa el valor a insertar: ")
                if opcion == "1":
                    insertar_izquierda(nodo_padre, nuevo_valor)
                else:
                    insertar_derecha(nodo_padre, nuevo_valor)
            else:
                print("Nodo padre no encontrado.")

        elif opcion == "3":
            print("\nVisualización del árbol:")
            visualizar(arbol)

        elif opcion == "4":
            print("Recorrido preorden:")
            preorden(arbol)
            print()

        elif opcion == "5":
            print("Recorrido inorden:")
            inorden(arbol)
            print()

        elif opcion == "6":
            print("Recorrido postorden:")
            postorden(arbol)
            print()

        elif opcion == "7":
            valor = input("Ingresa el valor del nodo a eliminar: ")
            padre, direccion = buscar_padre(arbol, valor)
            if padre is None:
                print("No se puede eliminar la raíz o el nodo no fue encontrado.")
            else:
                eliminar_nodo(padre, direccion)

        elif opcion == "8":
            total = contar_hojas(arbol)
            print(f"Total de hojas: {total}")

        elif opcion == "9":
            h = altura(arbol)
            print(f"Altura del árbol: {h}")

        elif opcion == "10":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
