filas  = int(input("dime el número de filas que va a tener la sala\n"))
asientos = int(input("dime el número de asientos que van a tener dichas filas\n"))
asientosocupados = []
fin = "si"

while fin == "si":
    disponibles = 0
    ocupados = 0
    print("\033c")
    print("Los # representa un asiento ocupado mientras que los 0 representa un asiento vacio.\nEstos son los asientos que quedan vacios")
    print("  : ", end="")
    for x in range(asientos):
        print(str(x)+" ", end="")
    print("")
    for x in range(filas):
        print(f"{x} : ", end="")
        for y in range(asientos):
            if [x,y] in asientosocupados:
                print("# ", end="")
                ocupados += 1
            else:
                print("0 ", end="")
                disponibles += 1
        print("")
    
    print(f"hay {ocupados} asientos ocupados y {disponibles} asientos disponibles")
    cantidad = int(input("¿Cuanta gente va a sentarse?\n"))
    juntos = input("¿Vais a querer sentaros juntos? (si/no)\n").lower()
    maxRow = int(input("Elige la fila maxima en la que os quereis sentar (maxRow)"))
    #Mirar y decir al usuario si estan disponibles esta cantidad de asientos juntos, si estan juntos, preguntarle si los va a querer
    disponiblesseguidos = 0
    if juntos == "si":
        sentados = False
        for x in range(filas):
            for y in range(asientos):
                if [x,y] in asientosocupados:
                    disponiblesseguidos = 0
                else:
                    disponiblesseguidos += 1
                    if disponiblesseguidos >= cantidad and x <= maxRow:
                        for i in range(cantidad-1, -1, -1):
                            asientosocupados.append([x,y-i])
                            cantidad -= 1
                        sentados = True
            disponiblesseguidos = 0
        if sentados == False:
            print("No os podeis sentar juntos siendo tantos o no quedan asientos, tambien puede ser que no se cumpla vuestro maxRow")
            input("Presiona enter para continuar\n")
        else:
            print("Se os ha sentado correctamente")
            input("Presiona enter para continuar\n")
    else:
        sentados = False
        for x in range(filas):
            for y in range(asientos):
                if [x,y] not in asientosocupados and cantidad > 0 and x <= maxRow and disponibles >= cantidad:
                    asientosocupados.append([x,y])
                    cantidad -= 1
                    sentados = True
                elif x> maxRow:
                    sentados = False
        if sentados == False:
            print("No se os ha podido sentar debido a que no hay espacio o no se puede cumplir vuestro maxRow")
                
    fin = input("¿Va a seguir llegando más gente? (si/no)").lower()
