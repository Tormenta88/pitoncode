class HashTable:
    def __init__(self, capacidad = 100):
        self.capacidad = capacidad
        #self.tabla = [None] * capacidad
        self.cantidad = 0
        self.tabla = [[] for _ in range(capacidad)]

    def __hash__(self, clave):
        return sum(ord(char) for char in clave % self.capacidad)
    
    def funcionHASH(self, clave):
        clave_str = str(clave)
        valor_hash = 0
        for x in clave_str:
            valor_hash = (valor_hash+ord(x))%self.capacidad
        A = 0.54656753287
        retorno = int(self.cantidad*((valor_hash*A)%1))

    def obtener(self, clave):
        return self.tabla[self.__hash__(clave)]
    
    def insertar(self, clave, valor):
        index = self.funcionHASH(clave)

        for aloja in self.tabla[index]:
            if aloja[0] != None:
                if aloja[0] == clave:
                    aloja[1] = valor
                    return
            else:
                aloja[0]= clave
                aloja[1] = valor
                self.cantidad +=1
        #self.tabla[index].append([clave,valor])


prueba = HashTable()

prueba.insertar("aver" ,"ciertamente")

prueba.obtener("aver")