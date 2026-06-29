from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from estructuras.lineales.lista_enlasada_simple import LinkedList
from estructuras.lineales.pila import Stack


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi("ui/menu_principal.ui", self)

        # Estructuras de datos
        self.lista = LinkedList()
        self.pila = Stack()

        # Conectar acciones del menú
        self.conectar_eventos()

    def conectar_eventos(self):
        """Conecta todas las acciones del menú."""

        # Lista enlazada
        self.actioninsertar_al_inicio_2.triggered.connect(self.insertar_inicio)
        self.actioninsertar_al_final_2.triggered.connect(self.insertar_final)
        self.actionbuscar_2.triggered.connect(self.buscar)
        self.actionimprimir_2.triggered.connect(self.imprimir_lista)
        self.actionsalir_2.triggered.connect(self.close)

        # Pila
        self.actionpush.triggered.connect(self.abrir_push)
        self.actionpop.triggered.connect(self.pop)
        self.actiontop_of_stack.triggered.connect(self.top)
        self.actioningresar.triggered.connect(self.mostrar_pila)
        self.actionsalir_3.triggered.connect(self.close)


    def insertar_inicio(self):
        print("Insertar al inicio")

    def insertar_final(self):
        print("Insertar al final")

    def buscar(self):
        print("Buscar")

    def imprimir_lista(self):
        print("Imprimir lista")

    def abrir_push(self):
        print("Abrir ventana Push")

    def pop(self):
        dato = self.pila.pop()

        if dato is None:
            print("La pila está vacía.")
        else:
            print("Elemento eliminado:", dato)

    def top(self):
        dato = self.pila.top_of_stack()

        if dato is None:
            print("La pila está vacía.")
        else:
            print("Elemento en la cima:", dato)

    def mostrar_pila(self):
        if self.pila.is_empty():
            print("La pila está vacía.")
            return

        aux = self.pila.top

        print("Top -> ", end="")

        while aux is not None:
            print(aux.dato, end=" -> ")
            aux = aux.next

        print("None")