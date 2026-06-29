from PyQt5 import uic
from PyQt5.QtWidgets import (
    QMainWindow,
    QInputDialog,
    QMessageBox
)

from estructuras.lineales.lista_enlasada_simple import LinkedList


class Load(QMainWindow):

    def __init__(self):
        super().__init__()

        uic.loadUi("lista_enlazada.ui", self)

        self.lista = LinkedList()

        self.conectar_eventos()

    def conectar_eventos(self):

        # Menú Lista Enlazada
        self.actioninsertar_al_inicio_2.triggered.connect(self.insertar_inicio)
        self.actioninsertar_al_final_2.triggered.connect(self.insertar_final)
        self.actionbuscar_2.triggered.connect(self.buscar)
        self.actionimprimir_2.triggered.connect(self.imprimir)
        self.actionsalir_2.triggered.connect(self.close)


    def insertar_inicio(self):

        dato, ok = QInputDialog.getText(
            self,
            "Insertar",
            "Ingrese el dato:"
        )

        if ok and dato:

            self.lista.insert_at_beginning(dato)

            QMessageBox.information(
                self,
                "Correcto",
                "Elemento agregado al inicio."
            )

    def insertar_final(self):

        dato, ok = QInputDialog.getText(
            self,
            "Insertar",
            "Ingrese el dato:"
        )

        if ok and dato:

            self.lista.insert_at_end(dato)

            QMessageBox.information(
                self,
                "Correcto",
                "Elemento agregado al final."
            )

    def buscar(self):

        dato, ok = QInputDialog.getText(
            self,
            "Buscar",
            "Ingrese el dato:"
        )

        if ok:

            if self.lista.search(dato):

                QMessageBox.information(
                    self,
                    "Buscar",
                    "Elemento encontrado."
                )

            else:

                QMessageBox.warning(
                    self,
                    "Buscar",
                    "Elemento NO encontrado."
                )

    def imprimir(self):

        try:

            texto = self.lista.print_linked_list()

            QMessageBox.information(
                self,
                "Lista",
                str(texto)
            )

        except:

            QMessageBox.information(
                self,
                "Lista",
                "No hay elementos."
            )

    def eliminar_inicio(self):

        try:

            self.lista.delete_at_beginning()

            QMessageBox.information(
                self,
                "Eliminar",
                "Elemento eliminado."
            )

        except:

            QMessageBox.warning(
                self,
                "Eliminar",
                "La lista está vacía."
            )

    def eliminar_final(self):

        try:

            self.lista.delete_at_end()

            QMessageBox.information(
                self,
                "Eliminar",
                "Elemento eliminado."
            )

        except:

            QMessageBox.warning(
                self,
                "Eliminar",
                "La lista está vacía."
            )