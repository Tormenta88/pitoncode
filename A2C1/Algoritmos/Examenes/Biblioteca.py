from mhash import HasTable
class Libro:
    def __init__(self, nombre,autor,genero,editorial="default",ISBN="default"):
        self.nombre = nombre
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.id = ISBN
    @property
    def info(self):
        print(f"Nombre: {self.nombre}\nAutor: {self.autor}\nGenero: {self.genero}")
        if self.editorial != "default":
            print(f"Editorial: {self.editorial}")
        if self.id != "default":
            print(f"ISBN: {self.id}")
#1. Organizar los libros de tal manera que se puedan encontrar rápidamente según el título. (Tabla hash)
class Data_Base:
    def __init__(self, capacidad=100):
        self.base = HasTable(capacidad)
    def añadir_libro(self,libro):
        nombre = libro.nombre
        self.base.insertar(nombre, libro)
    def borrar_libro(self, nombre):
        self.base.borrar(nombre)
    def buscar_libro(self, nombre):
        return self.base.obtener(nombre)
    def info_libro(self, nombre):
        return self.base.obtener(nombre).info

#2. Implementar un sistema de seguimiento en tiempo real para los libros más populares, permitiendo añadir o retirar libros de la lista con gran eficiencia.
pass

#3. Diseñar un sistema de cola de espera para los libros que están actualmente prestados. (Cola)










primero = Libro("Hora", "De", "Aventuras")
base = Data_Base()
base.añadir_libro(primero)
print(base.buscar_libro("Hora"))
base.info_libro("Hora")