import readchar
import os
import random

perdido = False
my_position = [3, 4]
player = "@"
tail_length = int()
tail = []

#Obstacle definition 33 * 11
obstacle_definition = """\
######  #######    #### ####### #
######  ####     ######    #### #
######  #    ####### #  # ##### #
###            ####    #   #### #
      #     #####   ####        # 
####### ##  ###### ############ #
# ##### ##  #####    #### ##### #
####### ####     ######    #### #
####### #    ####### #  # ##### #
###            ####    #   #### #
      #     #####   ####        # 
######  ##  ##  ## #### ####### #\
"""

"""
obstacle_definition =\
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               \
"""

#Creating the map itself
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")] #no tengo ni idea de que hace esto deberia leerme algo sobre ello se ve interesante



#Game objects generation
game_objects = []
while len(game_objects) < 10:
    new_object = [random.randint(1, 19), random.randint(1, 14)]
    if new_object not in game_objects and new_object != my_position:
        game_objects.append(new_object)

#Main Loop
while True:
    #Map formation
    print("+" + "-" * len(obstacle_definition[0]) * 2 + "+")
    for y in range(len(obstacle_definition)):
        print("|", end="")
        for x in range(len(obstacle_definition[0])):

            char_to_draw = " "

            for a in game_objects:
                if a[0] == x and a[1] == y:
                    char_to_draw = "0"
                if a[0] == my_position[0] and a[1] == my_position[1]:
                    game_objects.remove(a)
                    tail_length += 1
            
            for trozo in tail:
                if trozo == my_position:
                    perdido = True
                if trozo[0] == x and trozo[1] == y:
                    char_to_draw = "@"

            if my_position[0] == x and my_position[1] == y:
                char_to_draw = "@"

            if obstacle_definition[y][x] == "#":
                char_to_draw = "#"

            print(" {}".format(char_to_draw), end="")
        print("|",)
        print(" ")
    print("+" + "-" * len(obstacle_definition[0]) * 2 + "+")



    #Movement
    movement = readchar.readchar()
    if movement == "w" and my_position != obstacle_definition[my_position[1] - 1][my_position[0]] != "#":
       tail.insert(0, my_position.copy())
       tail = tail[:tail_length]
       my_position[1] -= 1
       if my_position[1] == -1:
           my_position[1] = len(obstacle_definition) - 1
    elif movement == "s" and my_position != obstacle_definition[my_position[1] + 1][my_position[0]] != "#":
       tail.insert(0, my_position.copy())
       tail = tail[:tail_length]
       my_position[1] += 1
       if my_position[1] == len(obstacle_definition):
           my_position[1] = 0
    elif movement == "a" and my_position != obstacle_definition[my_position[1]][my_position[0] - 1] != "#":
       tail.insert(0, my_position.copy())
       tail = tail[:tail_length]
       my_position[0] -= 1
       if my_position[0] == -1:
           my_position[0] = len(obstacle_definition[0]) -1
    elif movement == "d" and my_position != obstacle_definition[my_position[1]][my_position[0] + 1] != "#":
       tail.insert(0, my_position.copy())
       tail = tail[:tail_length]
       my_position[0] += 1
       if my_position[0] == len(obstacle_definition[0]):
            my_position[0] = 0
    elif movement == "q":
        break

    while len(game_objects) < 10:
        new_object = [random.randint(1, 19), random.randint(1, 14)]
        if new_object not in game_objects and new_object != my_position:
            game_objects.append(new_object)

    
    if perdido == True:
        break
    #cleaning the screen after every movement
    os.system("clear")
print("has perdido")
















"""no entiendo como puede hacer tanto calor la verdad
13 de junio a las 2 de la tarde y el calor que hace ciertamente no es normal, 33 grados 
21 de junio ha llegado la nueva persona y es incluso más lenta que sandra a si que comprendo que vaya a tardar más pero
realmente es lenta, ademas de que se esfuerza demasiado y va demasiado al detalle, le ha limpiado hasta la silla ha mi hermana
todavia no pasa por mi habitacion y yo realmente me aburro mucho, pq cojones tengo la hora en negro ya vuelve y yo ciertamente no tengo ganas 
jodder realmente va a limpiar más nuestro baño de lo que he visto jamas, acaba de decir que mal huele y despues escupir?
no me pasa, """