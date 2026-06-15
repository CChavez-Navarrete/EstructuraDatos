from estructuras.lineales.nodo import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_beginning(self, dato):
        #crear el  nuevo nodo con el dato proporcionado
        new_node = Node(dato)
        #si la lista esta vacia, el nuevo nodo es tanto la cabeza como la cola
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #enlazar el nuevo nodo con la cabeza actual
            new_node.next = self.head
            #actualizar la cabeza para que apunte al nuevo nodo
            self.head = new_node
    
    def print_linked_list(self):
        temp = self.head
        print("head -> ", end="")
        while temp is not None:
            print(temp.dato, "->", end=" ")
            temp = temp.next
        print("<- tail")
        
    def insert_at_end(self, dato):
        #crear el nuevo nodo con el dato proporcionado
        new_node = Node(dato)
        #si la lista esta vacia, el nuevo nodo es tanto la cabeza como la cola
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #enlazar la cola actual con el nuevo nodo
            self.tail.next = new_node
            #actualizar la cola para que apunte al nuevo nodo
            self.tail = new_node
            
    def search(self, dato):
        #paso 1 iniciar un nodo temporal en la cabeza de la lista
        temp = self.head
        #paso 2 recorrer la lista mientras el nodo temporal no sea None
        while temp is not None:
            #paso 3 comparar el dato del nodo temporal con el dato buscado
            if temp.dato == dato:
                #paso 4 si se encuentra el dato, retornar True
                return True
            else:
                temp = temp.next
        return False