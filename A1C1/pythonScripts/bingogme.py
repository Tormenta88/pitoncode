import random


#variables
inpot = ""
varo = 0
carton = [[], [], []]
columnas = [[], [], []]
nms = []
rng = 0
for x in range(0, 100):
    nms.append(x)

#Formación del carton
for x in range(3):
    for y in range(3):
        varo = int(input("Dame un número no repetido"))
        while varo in carton[0] or varo in carton[1] or varo in carton[2] or varo > 100:
            print("Ese número no es valido o ya ha sido seleccionado")
            varo = int(input("Dame un número no repetido"))
        else:
            carton[x].append(varo)

#Establecemos las columnas
for x in range(len(carton)):
    for y in range(len(carton)):
        columnas[x].append(carton[y][x])

#funcion para poder simplemente llamar al carton actual
def scarton():
    for x in range(len(carton)):
        print(carton[x])
    
for x in range(len(carton)):
    print(carton[x])
    



while True:
    inpot = input("Pulsela letra B")
    if inpot == "B" or inpot == "b":
        rng = random.choice(nms)
        print(rng)
        nms.remove(rng)
        #eliminamos ademas el número de carton
        for x in range(3):
            if rng in carton[x]:
                carton[x].remove(rng)
                if carton == [[], [], []]:
                    print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡BINGO!!!!!!!!!!!!!!!!!")
                    break
                elif carton[x] == []:
                    print("LINEA")
                
        scarton()