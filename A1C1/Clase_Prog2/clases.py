"""
class perro:
    
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        self.trucos = []


    def ladrar(self):
        print(self.nombre, "esta ladrando")

    def mover_cola(self):
        print(self.nombre, "esta moviendo la cola")

    def nuevo_truco(self, truco):
        self.trucos.append(truco)



alfonso = perro("Alfonso", "Mastín", )
alfonso.nuevo_truco("saltar")


prueba = perro("ciertamente", "Pastor Alemán")
prueba.nuevo_truco("Mover la cola")

print(prueba.trucos)
"""







"""
class bag:
    def __init__(self):
        self.data = []
    
    def add(self,x):
        self.data.append(x)
    
    def addd(self,x):
        self.add(x)
        self.add(x)


b = bag()
b.add(1)
b.add(2)
print(b.data)

c = bag()
c.addd(3)
print(c.data)
"""






"""
class Virus:
    def __init__(self,name,seq,strain):
        self.name = name
        self.seq = seq
        self.strain = strain

    strain_map = {"alpha" : (0,"a","t"), "beta" : (1,"t","c"), "gamma" : (2,"g","c"), "delta" : (3, "c","a"),
    "epsilon" : (4,"t","a"), "zeta" : (5,"g","t"), "eta" : (6,"a","c"), "theta" : (7, "g","a"),
    "iota" : (8,"c","g"),"kappa" : (9,"t","g")}

    def compare_lists(self,seq1,seq2):
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                for strain,val in self.strain_map.items():
                    if val[0] == i and (val[1] == seq1[i] and val[2] == seq2[i]):
                        print(strain)

name = "COVID"
seq = ["a","t","g","c","t","a","g","c","g","t"]
strain = "WT"
v = Virus(name,seq,strain)
v.compare_lists(seq,seq)
"""





"""
class virus:
    def __init__(self, nombre, seq, strain):
        self.nombre = nombre
        self.sequencia = seq
        self.sequencia = list(self.sequencia)
        print(self.sequencia)
        self.strain = strain
        self.strain_map = {"alpha" : (0,"a","t"), "beta" : (1,"t","c"), "gamma" : (2,"g","c"), "delta" : (3, "c","a"), "epsilon" : (4,"t","c"), "dseta" : (5,"g","a"), "ita" : (6,"a","c"), "zeta" : (7, "g","a"), "iota" : (8,"c","t"),"kappa" : (9,"t","g")}
        self.wt = list(["a","t","g","c","t","g","c","g","c","t"])
    
    def mostrar(self):
        print(f"El virus {self.nombre} tiene la secuencia: {self.sequencia} y es una strain tipo {self.strain}")
    
    def ojala(self):
        print(self.wt[0])



    def comparar(self):
        for x in range(len(self.wt)):
            #print(x)
            #print(self.wt[1]+self.wt[2])
            if self.strain_map[x][2] == self.sequencia[x]:
                print(f"Es cepa tipo {x} que es: {self.strain_map[x]}")
                



prueba = virus("Juanito", ["t","c","c","c","t","g","c","g","c","t"], "nada")

prueba.comparar()



diccionario = {"hola" : "quetal"}

print(diccionario.values(()))
"""





"""
class clases:
    def __init__(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, nuevo_valor):
        if nuevo_valor < 0:
            raise ValueError("Debe ser mayor o igual que 0")
        self._valor = nuevo_valor

objeto = clases(42)
objeto.valor = 10
print(objeto.valor)
"""







"""
class listadoBebidas:
    def __init__(self, bebida):
        self._bebida = bebida
        self._bebidas_validas = ["coke", "beer"]
    
    @property
    def bebida(self):
        return f"la bebida es {self._bebida}"
    @bebida.setter
    def bebida(self, bebida):
        if bebida in self._bebidas_validas:
            self._bebida = bebida
        else:
            raise ValueError(f"la bebida no esta en la lista")
    

prueba = listadoBebidas("coke")
prueba.bebida = "agua"
print(prueba.bebida)
"""




"""
class persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad
        else:
            raise ValueError(f"La edad nueva no puede ser negativa")
        
persona1 =persona("Juan",25)

nombre1 = persona1.nombre
edad1 = persona1.edad

print(nombre1)
print(edad1)

persona1.edad = -5

nueva_edad1 = persona1.edad
print(nueva_edad1)
"""




"""
class book:
    def __init__(self,title, author):
        self._title = title
        self._author = author
    
    @property
    def title(self):
        return self._title
    @title.setter
    def set_title(self,newtitle):
        self._title = newtitle
    
    @property
    def author(self):
        return self._author
    @author.setter
    def set_author(self, valor):
        self._author = valor


prueba = book("Vale", "Isaac")
prueba.title = "Okay"
print(prueba.title)
"""


"""
class formasGeometricas:
    def area(self):
        pass
    def perimetro(self):
        pass

class triangulo(formasGeometricas):
    def __init__(self, lado, altura):
        self.lado = lado
        self.altura = altura
    def area(self):
        return self.lado * self.altura
    def perimetro(self):
        return self.lado * 2 + self.altura * 2

"""

"""
class vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class coche(vehicle):
    def __init__(self, make,model,year,num_wheels,num_passengers,speed):
        super().__init__(make,model,year)
        self.num_wheels = num_wheels
        self.num_passengers = num_passengers
        self.speed = speed

    def print_info(self):
        super().print_info()
        print(f"El número de ruedas es: {self.num_wheels}, El número de pasajeros es: {self.num_passengers} y la velocidad maxima es: {self.speed}")


honda = coche("Honda", "civic", 2020, 4, 5, 180)
honda.print_info()"""



"""
class trabajador:
    def __init__(self, identificacion, nombre, salario):
        self.identificacion = identificacion
        self.nombre = nombre
        self.salario = salario

    def mostrar(self):
        print(self.identificacion, self.nombre, self.salario)
    

class tiempo_completo(trabajador):
    def __init__(self, identificacion, nombre, salario, beneficios):
        super().__init__(identificacion, nombre, salario)
        self.beneficios = beneficios

    def mostrar(self):
        super().mostrar()
        print(self.beneficios)


class tiempo_parcial(trabajador):
    def __init__(self, identificacion, nombre, salario, horas_semanales):
        super().__init__(identificacion, nombre, salario)
        self.horas_semanales = horas_semanales

    def mostrar(self):
        super().mostrar()
        print(self.horas_semanales)


class contratista(trabajador):
    def __init__(self, identificacion, nombre, salario, duracion_contrato):
        super().__init__(identificacion, nombre, salario)
        self.duracion_contrato = duracion_contrato

    def mostrar(self):
        super().mostrar()
        print(self.duracion_contrato)

class animal_domestico:
    def __init__(self, nombre_mascota, edad, tipo):
        self.nombre = nombre_mascota
        self.edad = edad
        self.tipo = tipo


class mascota_trabajador(animal_domestico, trabajador):
    def __init__(self, nombre_mascota, edad, tipo, identificacion, salario)
    super().__init__(nombre)
    animal_domestico.__init__()"""









"""
class prueba():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return("({},{})".format(self.x, self.y))

    def __add__(self, otro):
        return prueba(self.x + otro.x, self.y + otro.y)
    

p1 = prueba(3,4)
p2 = prueba(4,2)

print(p1 + p2)
print(p1)
"""


"""
print(len("Programa")) # = 9

print(len(["Python", "Java", "C"])) # = 3

print(len({"Names":"Jhon", "Adress":"Nepal"})) # = 2
"""
"""
lista = [True, 3.2, 3, "a", "b"]

print(lista.sort())
                    
  
  
  
               
  
  
  
                   
"""






"""
class gato():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        print(self.nombre, self.edad)
    
    def sonido(self):
        print("Meow")
        
    

class perro():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        return self.nombre, self.edad
    
    def sonido(self):
        print("Guau")

gato1 = gato("Aurelio", 78)
perro1 = perro("Sigmoidea", 2)

gato1.info()
gato1.sonido()

"""

"""
class estudiante():
    def describir(self):
        print("Soy un buen estudiante")




class docente():
    def describir(self):
        print("Me dedico a la docencia")


class trabajador():
    def describir(self):
        print("Trabajo en una multinacional")


def describirRandom(persona):
    persona.describir()


doc1 = docente()
describirRandom(doc1)"""



"""
from math import pi

class forma:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return("Soy una forma bidimensional")
    def __str__(self):
        return self.name
    
class bebida:
    def __init__(self, name, temp):
        self.name = name
        self.temp = temp
    
    def __str__(self):
        return f"{self.name} ({self.temp} degrees)"

    def serve(self):
        print(f"Here is your {self.name} served")

class coffee(bebida):
    def __init__(self,name,temperature,roast):
        super().__init__(name,temperature)
        self.roast = roast

    def __str__ (self):
        return f"{self.roast} {self.name} Is here or smth"""



class persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    

    @property
    def nombre(self):
        print(self._nombre)
    @nombre.setter
    def nombre(self, nuevo):
        self._nombre = nuevo

    def cagar(self):
        print("He cagado")

class animal:
    def __init__(self, tipo):
        self.tipo = tipo
    
    

class profesion(persona, animal):
    def __init__(self,nombre, edad, tipo, trabajo):
        persona.__init__(self, nombre, edad)
        animal.__init__(self, tipo)
        self._trabajo = trabajo

    def __str__(self):
        return f"Esta persona se llama: {self._nombre}, tiene {self._edad} años y se dedica a la {self._trabajo}, siendo un {self.tipo}"
    
    @property
    def trabajo(self):
        print(self._trabajo)
    
    @trabajo.setter
    def trabajo(self, nuevo):
        self._trabajo = nuevo

    def informacion(self):
        print(f"{self._nombre} es {self._trabajo}")
    
    def cagar(self):
        persona.cagar(self)



persona1 = profesion("Aura", 27, "Huamno", "Informatica")
persona1
persona1.cagar()

lmao = 2
lmao = 3




