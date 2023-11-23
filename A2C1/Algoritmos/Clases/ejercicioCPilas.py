from Pilas import Pila



pila = Pila()

pila.push("Prueba")
pila.push("Cierto")
print(pila.peek())



def comprobador(entrada) -> str:
    pila = Pila()
    for x in entrada:
        pila.push(x)


type(pila.__str__())