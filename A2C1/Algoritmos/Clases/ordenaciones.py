def inter(lista, posSigMin, PosMin):
    lista[posSigMin], lista[PosMin] = lista[PosMin], lista[posSigMin]

def ordenacio_seleccion_directa(lista):
    n = len(lista)
    posMin = 0
    for i in range(n-1):
        min = lista[i]
        for j in range(i+1, n):
            if lista[j] < min:
                posMin = j
        inter(lista, i, posMin)

def busqueda_lineal(lista, elemento):
    for i in len(lista):
        if lista[i] == elemento:
            return i

def insercion_directa(lista):
    n = len(lista)
    for i in range(n-1, -1, -1):
        base = lista[i]
        j = i - 1
        if base < lista[j]:
            lista[j], lista[i] = lista[i], lista[j]

def busqueda_binaria(lista, elemento):
    izquierda = 0
    derecha = len(lista) -1
    while izquierda <= derecha:
        centro = (izquierda+derecha) // 2
        if lista[centro] == elemento:
            return centro
        elif lista[centro] < elemento:
            izquierda = centro +1
        else:
            derecha = centro -1

    return -1

def burbujacorta(lista: list) -> None:
    





listilla = [2,3,1,4,3567,321,6,8,3,12]
print(listilla)
insercion_directa(listilla)
print(listilla)