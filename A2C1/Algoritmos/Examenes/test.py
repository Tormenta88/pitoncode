from Biblioteca import *



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