class HashTable:
    def __init__(self, capacidad = 100):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad
        self.cantidad = 0

    def __hash__(self, clave):
        return sum(ord(char) for char in clave % self.capacidad)
    
    def insertar(self, clave, valor):
        indice = self.__hash__(clave)

        if not self.tabla(indice):
            self.tabla[indice] = valor
            self.cantidadcantidad+=1

        else:
            lista = list(self.tabla[indice])
            lista.append(valor)
            self.tabla[clave] = lista
            self.cantidad +=1

    def obtener(self, clave):
        return self.tabla[self.__hash__(clave)]
    