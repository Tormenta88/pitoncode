
"""from os import system, name 
from time import sleep
idioma = 0

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


clear()

"""
idioma = int(input("Introduce el idioma en el que prefieres jugar.\n 1 Para Español 2 para ingles\n"))

while True:
    if idioma != 1 or idioma != 2:
     idioma = int(input("Introduce el idioma en el que prefieres jugar.\n 1 Para Español 2 para ingles\n"))
#    clear()
    else:
        break



        

if idioma == 2:
    print("Ingles")
elif idioma == 1:
    print("Español")




#sleep(5)
#clear()
