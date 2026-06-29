from estructuras.lineales.stack import Stack


def menu():

    pila = Stack()

    while True:

        print("\n====== PILA ======")
        print("1. Push")
        print("2. Pop")
        print("3. Ver cima")
        print("4. Mostrar pila")
        print("5. Tamaño")
        print("6. Vaciar pila")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            dato = input("Ingrese el dato: ")
            pila.push(dato)
            print("Elemento agregado.")

        elif opcion == "2":

            dato = pila.pop()

            if dato is None:
                print("La pila está vacía.")
            else:
                print("Elemento eliminado:", dato)

        elif opcion == "3":

            dato = pila.top_of_stack()

            if dato is None:
                print("La pila está vacía.")
            else:
                print("Elemento en la cima:", dato)

        elif opcion == "4":

            print(pila.print_stack())

        elif opcion == "5":

            print("Cantidad de elementos:", pila.size())

        elif opcion == "6":

            pila.clear()
            print("La pila fue vaciada.")

        elif opcion == "7":

            print("Programa finalizado.")
            break

        else:

            print("Opción no válida.")


if __name__ == "__main__":
    menu()