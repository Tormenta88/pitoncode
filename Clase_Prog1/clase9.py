import math

inputa, inputb = int(input("Dime un número\n")), int(input("Dime otro número\n"))

def suma():
    print(inputa+inputb)

def resta():
    print(inputa-inputb)

def multiplicacion():
    print(inputa*inputb)

def sqrt():
    print(math.sqrt(inputa))


diccionario = {
    1 : suma,
    2 : resta,
    3 : multiplicacion,
    4 : sqrt
}

operacion = int(input("Dime que quieres hacer \nsuma = 1\nresta = 2\nmultiplicación = 3\nRaiz cuadrada = 4\n"))
diccionario[operacion]()

