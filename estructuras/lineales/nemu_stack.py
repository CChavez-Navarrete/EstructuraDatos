from estructuras.lineales.nodo import Node

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, dato):
        new_node = Node(dato)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.top is None:
            print("La pila está vacía. No se puede realizar pop.")
            return None
        else:
            dato = self.top.dato
            self.top = self.top.next
            return dato
        
    def top_of_stack(self):
        if self.top is None:
            print("La pila está vacía. No hay elemento en la cima.")
            return None
        else:
            return self.top.dato
        
    def print_stack(self):
        temp = self.top
        print("Top -> ", end="")
        while temp is not None:
            print(temp.dato, "->", end=" ")
            temp = temp.next
        print("None")
        
    def is_empty(self):
        return self.top is None
    
        