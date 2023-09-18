# Nodo:

class Nodo:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.siguiente = None

class ListaSimplementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.cantidadNodos = 0 #Para contar cuantos nodos tenemos en todo momento

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = None
        #Ver si esta vacia
        if not self.cabeza: #Lista esta vacia
            self.cabeza = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.cantidadNodos +=1
            return
        else: #Lista no esta vacia
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.cantidadNodos += 1

    def eliminar(self, dato):
        nodo_actual = self.cabeza
        if nodo_actual and nodo_actual.dato == dato:
            self.cabeza = nodo_actual.siguiente
            nodo_actual = None
        previo = None
        while nodo_actual and nodo_actual.dato != dato:
            previo = nodo_actual
            nodo_actual = nodo_actual.siguiente
        
        if nodo_actual is None:
            return
        previo.siguiente = nodo_actual.siguiente
        nodo_actual = None

    def estaVacia(self):
        if self.cabeza == None:
            return True
        return False

    def estaVacia(self,nodo):
        return True if nodo.siguiente == None else False



