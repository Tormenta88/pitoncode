class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None
class Pila:
    def __init__(self) -> None:
        self.tope = None
    def push(self, valor) -> None:
        nodo = Nodo(valor=valor)
        nodo.siguiente = self.tope
        self.tope = nodo
    def pop(self):
        if self.is_empty():
            print("Error: la pila está vacía")
            return None
        valor = self.tope.valor
        self.tope = self.tope.siguiente
        return valor
    def peek(self) -> object:
        if self.is_empty():
            print("Error: la pila está vacía")
            return None
        valor = self.tope.valor
        return valor
    def is_empty(self) -> bool:
        if self.tope == None:
            return True
        return False 
    def __str__(self) -> str:
        elementos = []
        str_elementos = ""
        nodo_actual = self.tope
        while nodo_actual:
            elementos.append(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente
        return "->".join(elementos)
