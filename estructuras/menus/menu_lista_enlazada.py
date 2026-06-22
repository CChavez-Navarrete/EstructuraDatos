from estructuras.lineales.lista_enlasada_simple import LinkedList
class menu_lista_enlazada(object):
    def __init__(self):
        self.lista = LinkedList()
    
    def mostrar_menu(self):
        print("Menú de Lista Enlazada")
        print("1. agregar elemento al inicio")
        print("2. Insertar al final")
        print("3. Buscar elemento")
        print("4. mostrar lista")
        print("5. Eliminar elemento del inicio")
        print("6. Eliminar elemento del final")
        print("7. Salir")
    
    def ejecutar_opcion(self, opcion):
        if opcion == "1":
            elemento = input("Ingrese el elemento a agregar al inicio: ")
            self.lista.insert_at_beginning(elemento)
            print(f"El elemento {elemento} ha sido agregado al inicio de la lista.")
        elif opcion == "2":
            elemento = input("Ingrese el elemento a insertar al final: ")
            self.lista.insert_at_end(elemento)
            print(f"El elemento {elemento} ha sido insertado al final de la lista.")
        elif opcion == "3":
            elemento = input("Ingrese el elemento a buscar: ")
            encontrado=self.lista.search(elemento)
            if encontrado:
                print(f"El elemento {elemento} se encuentra en la lista.")
            else:
                print(f"El elemento {elemento} no se encuentra en la lista.")
        elif opcion == "4":
            self.lista.print_linked_list()
        elif opcion == "5":
            self.lista.delete_at_beginning()
        elif opcion == "6":
            self.lista.delete_at_end()
        elif opcion == "7":
            self.salir()
        else:
            print("Opción no válida.")
            
    def iniciar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = input("Seleccione una opción: ")
                if opcion == "7":
                    self.ejecutar_opcion(opcion)
                    break
                self.ejecutar_opcion(opcion)
            except ValueError:
                print("Opción no válida. Por favor, ingrese un número del 1 al 7.")
    
    def eliminar_final(self):
        # Lógica para eliminar el último elemento de la lista enlazada
        if self.lista.tail:
            dato = self.lista.tail.dato
            self.lista.delete_from_end()
            print(f"El dato {dato} ha sido eliminado de la lista.")
        else:
            print("La lista está vacía.")

    def buscar_elemento(self):
        # Lógica para buscar un elemento en la lista enlazada
        dato = input("Ingrese el dato a buscar: ")
        if self.lista.search(dato):
            print(f"El dato {dato} se encuentra en la lista.")
        else:
            print(f"El dato {dato} no se encuentra en la lista.")
            
    def eliminar_inicio(self):
        # Lógica para eliminar el primer elemento de la lista enlazada
        if self.lista.head:
            dato = self.lista.head.dato
            self.lista.delete_at_beginning()
            print(f"El dato {dato} ha sido eliminado de la lista.")
        else:
            print("La lista está vacía.")

    def salir(self):
        print("Saliendo del programa.")