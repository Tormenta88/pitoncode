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

    def buscar(self, dato):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.dato == dato:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return False
    
    def actualizar(self, posicion, nuevo_dato):
        nodo_actual = self.cabeza
        indice = 0
        while nodo_actual: 
            if indice == posicion:
                nodo_actual = nuevo_dato

            nodo_actual = nodo_actual.siguiente
            indice += 1
    
    #Devuelve una lista python con todos los datos
    def recorrer(self):
        todos_los_datos = []
        nodo_actual = self.cabeza
        while nodo_actual:
            todos_los_datos.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return todos_los_datos
    
    #Uso del algoritmo de la burbuja
    def ordenar(self):
        if self.cabeza == None:
            return
        nodo_actual = self.cabeza

        while nodo_actual:
            nodo_siguiente = nodo_actual.siguiente
            while nodo_siguiente:
                if nodo_siguiente.dato < nodo_actual.dato:
                    auxiliar = nodo_siguiente.dato
                    nodo_siguiente.dato = nodo_actual.dato
                    nodo_actual.dato = auxiliar
                    #Bien
                    nodo_actual.dato, nodo_siguiente.dato = nodo_siguiente.dato, nodo_actual.dato

                    nodo_siguiente = nodo_siguiente.siguiente
                nodo_actual = nodo_actual.siguiente


    def estaVacia(self):
        if self.cabeza == None:
            return True
        return False

    def estaVacia(self,nodo):
        return True if nodo.siguiente == None else False


#OTROXXd
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista_pila:
    def __init__(self):
        self.cabeza = Nodo(None)
        self.ultimo = self.cabeza
        self.cantidad = 0

    def esVacia(self):
        if self.cabeza.siguiente == None:
            return True
        return False


    def insertar_definitivomismuertospisadostuputamadremamahuevazodeloscojones(self, nuevo_nodo):
        nuevo_nodo.siguiente = self.cabeza.siguiente
        self.cabeza.siguiente = nuevo_nodo

    def buscar_por_dato(self, dato):
        nodo_actual = self.cabeza.siguiente
        while nodo_actual:
            if nodo_actual.dato == dato:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return
    
    def eliminar_por_dato(self,dato):
        if self.esVacia():
            return False
        nodo_actual = self.cabeza

        while nodo_actual.siguiente:
            if nodo_actual.siguiente.dato == dato:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return True
            nodo_actual = nodo_actual.siguiente
        return False
