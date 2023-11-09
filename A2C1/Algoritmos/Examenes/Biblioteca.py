from mhash import HasTable
from Cola import ListaCola
class Libro:
    def __init__(self, nombre,autor,genero, cantidad=0,editorial="default",ISBN="default"):
        self.nombre = nombre
        self.autor = autor
        self.genero = genero
        self.cantidad = cantidad
        self.editorial = editorial
        self.id = ISBN
    #Definimos un getter para nuestro libro que nos devuelva todos los valores del mismo
    @property
    def info(self):                                                                     #Prestamos atención a si quedan en existencia, si no es el caso devolvemos que en digital
        print(f"Nombre: {self.nombre}\nAutor: {self.autor}\nGenero: {self.genero}\nDisponibilidad: {'Digital' if self.cantidad < 1 else self.cantidad}")
        #Hacemos 2 filtros por si los valores editorial y ISBN se han dejado en blanco
        if self.editorial != "default":
            print(f"Editorial: {self.editorial}")
        if self.id != "default":
            print(f"ISBN: {self.id}")
#1. Organizar los libros de tal manera que se puedan encontrar rápidamente según el título. (Tabla hash)
class Data_Base:
    #Creamos nuestra hash table con una capacidad default de 100 libros
    def __init__(self, capacidad=100):
        self.base = HasTable(capacidad)
    #Accedemos a nuestra clase libro definiendo el nombre del libro con el atributo nombre y insertamos como valor el propio objeto
    def añadir_libro(self,libro):
        nombre = libro.nombre
        self.base.insertar(nombre, libro)
    def borrar_libro(self, nombre):
        self.base.borrar(nombre)
    def buscar_libro(self, nombre):
        #Miramos si el libro existe y si si lo devolvemos.
        if self.base.obtener(nombre):
            return self.base.obtener(nombre)
        else:
            return "Libro no encontrado"
    def info_libro(self, nombre):
        #Llamamos al getter de la clase Libro
        return self.base.obtener(nombre).info

#2. Implementar un sistema de seguimiento en tiempo real para los libros más populares, permitiendo añadir o retirar libros de la lista con gran eficiencia.
pass

#3. Diseñar un sistema de cola de espera para los libros que están actualmente prestados. (Cola)
class Prestar():
    def __init__(self, db):
        self.db = db
        self.cola = ListaCola()
        #A la hora de implementar los tiempos de prestamos de libro yo implementaria un diccionario donde clave = nombre_libro y valor = dias, pero no me va a dar tiempo.
    
    def prestar(self, nombre_libro):
        #Primero miramos si tenemos de ese libro para poder prestarlo:
        if self.db.buscar_libro(nombre_libro).cantidad > 0:
            #Si si podemos lo metemos a la cola de los prestados
            self.cola.insertar(nombre_libro)
            #Y quitamos uno de la cantidad que tenemos en reserva
            self.db.buscar_libro(nombre_libro).cantidad -= 1
            print(f"Libro {nombre_libro} ha sido prestado correctamente")
        else:
            print(f"No quedan existencias del libro: {nombre_libro}")
    
    def buscar_prestamo(self, libro):
        #Filtramos para ver si el libro existe dentro de nuestra cola de prestados
        if self.cola.buscar(libro):
            print(f"El libro {libro} si ha sido prestado y quedan: {self.db.buscar_libro(libro).cantidad}")
        else:
            #Si no esta entre los prestados miramos si el libro existe en la base de datos
            if self.db.buscar_libro(libro):
                print(f"El libro {libro} no ha sido prestado y quedan: {self.db.buscar_libro(libro).cantidad}")
            else:
                print("El libro no figura en la base de datos")
    
    def devolver(self, libro, duracion):
        #Eliminamos de la cola de prestados y devolvemos el tiempo del prestamo.
        self.cola.eliminar(libro)
        print(f"Libro {libro} devuelto con exito tras {duracion} dias")
        #Volvermos a añadirlo a la cantidad de los que tenemos en reserva
        self.db.buscar_libro(libro).cantidad +=1
    
    def prestados(self):
        #Mostramos todos los libros que hemos prestado
        print(self.cola.recorrer())









primero = Libro("Hora", "De", "Aventuras", 1)

base = Data_Base()
base.añadir_libro(primero)
print(base.buscar_libro("Hora"))
base.info_libro("Hora")

presto = Prestar(base)
presto.prestar("Hora")
presto.buscar_prestamo("ora")
presto.prestados()
presto.devolver("Hora", 365)