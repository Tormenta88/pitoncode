ciertamente = 1
lista = ["hola", ciertamente, 1, [0,3]]

for x in lista:
    if x in lista:
        print(f"{x} Si esta")
