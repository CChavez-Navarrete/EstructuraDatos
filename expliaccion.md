El programarecorre la expresión carácter por carácter y usa la pila para almacenar temporalmente los operadores hasta que puedan agregarse al resultado Cada vez que se crea un objeto ConversorPosfijo, se inicializa una pila vacía donde se almacenarán los operadores durante la conversión 

Este método asigna una prioridad a cada operador matemático 
prioridades = {
   '+': 1,
   '-': 1,
   '*': 2,
   '/': 2,
   '$': 3
}

Verifica si un carácter corresponde a un operador válidp
return caracter in ['+', '-', '*', '/', '$']
Ejemplos:
'A' → False
'+' → True
'/' → True

Este es el método principal del algoritmo.
def convertir(self, expresion):
Recibe una expresión en notación infija y devuelve su equivalente en notación posfija.
self.pila = Stack()
Si anteriormente se convirtió otra expresión, se crea una nueva pila vacía para evitar datos residuales.
salida = ""
Aquí se almacenará la expresión posfija.
for caracter in expresion.replace(" ", ""):
Primero elimina los espacios.
Ejemplo:
A + B * C
se convierte en
A+B*C
Luego analiza cada carácter.

Cuando encuentra un "(", simplemente lo guarda en la pila.
Ejemplo
(A+B)
Pila
(
Cuando encuentra un ")" comienza a sacar operadores.
while (not self.pila.is_empty() and
      self.pila.top_of_stack() != '('):

   salida += self.pila.pop()
Va extrayendo operadores hasta encontrar el "(".
Después elimina el paréntesis.
Se crea una pila vacía.
Se recorre la expresión carácter por carácter.
Los operandos (letras o números) se agregan directamente a la salida.
Los operadores se almacenan en la pila respetando su prioridad.
Los paréntesis controlan el orden de las operaciones; no aparecen en el resultado.
Al finalizar, se vacía la pila para completar la expresión posfija.
