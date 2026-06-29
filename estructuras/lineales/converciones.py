from estructuras.lineales.pila import Stack


class ConversorPosfijo:

    def __init__(self):
        self.pila = Stack()

    def prioridad(self, operador):
        prioridades = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '$': 3
        }
        return prioridades.get(operador, 0)

    def es_operador(self, caracter):
        return caracter in ['+', '-', '*', '/', '$']

    def convertir(self, expresion):

        # Reiniciar la pila
        self.pila = Stack()

        salida = ""

        for caracter in expresion.replace(" ", ""):

            # Si es operando (letra o número)
            if caracter.isalnum():
                salida += caracter

            # Paréntesis de apertura
            elif caracter == '(':
                self.pila.push(caracter)

            # Paréntesis de cierre
            elif caracter == ')':

                while (not self.pila.is_empty() and
                       self.pila.top_of_stack() != '('):

                    salida += self.pila.pop()

                # Eliminar '('
                if not self.pila.is_empty():
                    self.pila.pop()

            # Operadores
            elif self.es_operador(caracter):

                while (not self.pila.is_empty() and
                       self.pila.top_of_stack() != '(' and
                       self.prioridad(self.pila.top_of_stack()) >= self.prioridad(caracter)):

                    salida += self.pila.pop()

                self.pila.push(caracter)

        # Vaciar la pila
        while not self.pila.is_empty():
            salida += self.pila.pop()

        return salida