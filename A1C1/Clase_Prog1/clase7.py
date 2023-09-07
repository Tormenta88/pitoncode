lista = ["Mates", "Lengua", "Historia", "Probando", "Probando"]
i=0
for x in range(len(lista)):
    if int(input(f"Que nota has sacado en {lista[x-i]}\n")) < 5:
        lista.pop(x-i)
        i+=1


print(f"Has aprobado: {lista}")
