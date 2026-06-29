from estructuras.lineales.nodo import Node


class Stack:

    def __init__(self):
        self.top = None

    def push(self, dato):
        """Inserta un elemento en la cima."""
        nuevo = Node(dato)
        nuevo.next = self.top
        self.top = nuevo

    def pop(self):
        """Elimina y retorna el elemento de la cima."""
        if self.is_empty():
            return None

        dato = self.top.dato
        self.top = self.top.next
        return dato

    def top_of_stack(self):
        """Retorna el elemento de la cima sin eliminarlo."""
        if self.is_empty():
            return None

        return self.top.dato

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return self.top is None

    def size(self):
        """Retorna la cantidad de elementos."""
        contador = 0
        aux = self.top

        while aux is not None:
            contador += 1
            aux = aux.next

        return contador

    def clear(self):
        """Vacía completamente la pila."""
        self.top = None

    def print_stack(self):
        """Devuelve una cadena con el contenido de la pila."""

        if self.is_empty():
            return "La pila está vacía."

        texto = "Top -> "
        aux = self.top

        while aux is not None:
            texto += f"{aux.dato} -> "
            aux = aux.next

        texto += "None"

        return texto