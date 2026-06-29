from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox

from estructuras.lineales.nemu_stack import Stack


class Load(QDialog):

    def __init__(self):
        super().__init__()

        uic.loadUi("Stack.ui", self)

        # Crear la pila
        self.pila = Stack()

        # Conectar botón
        self.calcular.clicked.connect(self.procesar)

    def procesar(self):

        # Obtener el texto ingresado
        texto = self.ingreso_de_datos.toPlainText().strip()

        if texto == "":
            QMessageBox.warning(
                self,
                "Advertencia",
                "Ingrese una expresión."
            )
            return

        # Vaciar la pila
        self.pila = Stack()

        # Insertar cada carácter en la pila
        for caracter in texto:
            self.pila.push(caracter)

        # Mostrar el contenido de la pila
        cadena = "Top -> "

        aux = self.pila.top

        while aux is not None:
            cadena += str(aux.dato) + " -> "
            aux = aux.next

        cadena += "None"

        self.resultado.setText(cadena)