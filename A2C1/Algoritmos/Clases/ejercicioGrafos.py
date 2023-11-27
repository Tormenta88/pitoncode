class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.relaciones = []


# !Construir un grafo ponderado en Python que represente la relación entre productos basándose en cuántas veces son comprados juntos.
#! Luego, realizar análisis básicos sobre este grafo para obtener insights sobre la co-compra de productos.

transacciones = [
    ["Pan", "Leche"],
    ["Pan", "Mermelada"],
    ["Leche", "Galletas"],
    ["Pan", "Leche", "Galletas"],
    ["Mermelada", "Galletas"]
]



class Grafo:
    def __init__(self):
        self.grafo = {}

    def añadir(self, dato, rels=list):
        self.grafo[dato] = Nodo(dato)
        self.grafo[dato].relaciones.extend(rels)


gr = Grafo

gr.añadir('caca', ['Manzana', 'Arboles'])

print(gr.grafo)