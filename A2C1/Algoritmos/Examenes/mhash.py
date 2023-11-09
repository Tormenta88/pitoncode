class HasTable:
    def __init__(self, capacidad=100):
        self.capacidad = capacidad
        self.tabla = [None] * capacidad
        self.cuantos_hay = 0

    def __hash__(self, clave):
        return sum(ord(char) for char in clave) % self.capacidad

    # put
    def insertar(self, clave, valor):
        indice = self.__hash__(clave)

        if not self.tabla[indice]:
            self.tabla[indice] = valor
            self.cuantos_hay += 1
        else:
            # Si la posicion ya etsa ocupada
            # Creamos una nueva
            lista = list(self.tabla[indice])
            lista.append(valor)
            self.tabla[indice] = lista
            self.cuantos_hay += 1

        # get
    def obtener(self, clave):
        return (self.tabla[self.__hash__(clave)])
    
    def borrar(self, clave):
        valor = self.obtener(clave)
        del valor
