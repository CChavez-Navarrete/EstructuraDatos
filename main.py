#from estructuras.menus.menu_lista_enlazada import menu_lista_enlazada
import sys
from PyQt5.QtWidgets import QApplication
from luad.load_ventana_principal import VentanaPrincipal

def main():
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()