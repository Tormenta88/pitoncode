#############################################
###        BFS Breadth First Search       ###
#############################################

# Recorrido
def bfs(self, inicio):
    visitados = set()
    cola = {inicio}
    while cola:
        nodo_actual = cola.pop(0)
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            cola.extend(self.vecinos(nodo_actual)) - visitados
    return visitados




def bfsb(self, inicio, criterio_busqueda):
    visitados = set()
    cola = {inicio}
    while cola:
        nodo_actual = cola.pop(0)
        if nodo_actual == criterio_busqueda:
            return nodo_actual
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            cola = cola.union(self.vecinos(nodo_actual)) - visitados
    return None



#recorrido dfs?

def dfs(grafo, inicio, visitados=None)
    if visitados is None:
        visitados = set()

    visitados.add(inicio)

    for vecino in grafo(inicio):
        if vecino not in visitados:
            dfs(grafo,vecino,visitados)
    return visitados

