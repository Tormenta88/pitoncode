primelist = []


    def primos(d): #Devuelve una lista de numeros primos
    #Creamos la lista de números primos
        for d in range(2,d):
            prime = True
            for i in range(2,d):
                if (d%i==0):
                    prime = False
            if prime:
                primelist.append(d)
        return primelist


spiralso = [] # Lista de números sin ordenar, cada lista en su interior va a ser una fila, 
giro = 1
dirección = 0 # direccion siempre va a indicar hacia donde se mueve la lista, siendo 0 derecha 1 arriba 2 izquierda 3 abajo.
ronda = 0


def spiral(z):
    while z % 2 != 0: #siempre que sea distinto de cero (osea los impares) se ejecuta
        while ronda < 2:
            if ronda > 3:
                ronda = 1
        for x in range(z): #lista de números hasta z
            if dirección == 0:


                dirección +=1
            elif dirección == 1:
            

                dirección +=1
            elif dirección == 2:
            

                dirección +=1
            elif dirección == 3:


                dirección = 0





print(primos(input("Dame un nº impar")))
