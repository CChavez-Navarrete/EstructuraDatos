from estructuras.lineales.stack import Stack


class MenuStack:

    def __init__(self):
        self.pila = Stack()

    def mostrar_menu(self):
        print("\n========== MENÚ PILA ==========")
        print("1. Push (Insertar)")
        print("2. Pop (Eliminar)")
        print("3. Top (Ver cima)")
        print("4. Mostrar pila")
        print("5. Verificar si está vacía")
        print("6. Salir")
        print("===============================")

    def ejecutar_opcion(self, opcion):

        if opcion == "1":
            dato = input("Ingrese el dato: ")
            self.pila.push(dato)
            print(f"'{dato}' fue agregado a la pila.")

        elif opcion == "2":
            dato = self.pila.pop()

            if dato is None:
                print("La pila está vacía.")
            else:
                print(f"Se eliminó: {dato}")

        elif opcion == "3":
            dato = self.pila.top_of_stack()

            if dato is None:
                print("La pila está vacía.")
            else:
                print(f"Elemento en la cima: {dato}")

        elif opcion == "4":
            self.mostrar_pila()

        elif opcion == "5":
            if self.pila.is_empty():
                print("La pila está vacía.")
            else:
                print("La pila contiene elementos.")

        elif opcion == "6":
            self.salir()

        else:
            print("Opción no válida.")

    def mostrar_pila(self):

        if self.pila.is_empty():
            print("La pila está vacía.")
            return

        aux = self.pila.top

        print("\nTop -> ", end="")

        while aux is not None:
            print(aux.dato, end=" -> ")
            aux = aux.next

        print("None")

    def salir(self):
        print("Saliendo del programa...")

    def iniciar(self):

        while True:

            self.mostrar_menu()

            opcion = input("Seleccione una opción: ")

            if opcion == "6":
                self.salir()
                break

            self.ejecutar_opcion(opcion)