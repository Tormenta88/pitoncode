import turtle
import random
import math

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

#Elegimos el tipo de espiral y la cantidad de números
type = input("Tipo\n")
num = int(input("Cantidad\n"))
primos(num)

#Definimos la tortuga y  la pantalla
screen = turtle.Screen()

a = turtle.Turtle()
a.speed(25)
a.pensize(5)
a.hideturtle()
a.penup()

#Creamos la espiral segun la elegida
if type == "1":
    for i in range(num):
        a.speed(40)
        a.pendown()
        a.dot(4)
        a.penup()
        a.forward(2+i/4)
        a.right(30-i/12)


elif type == "2":
    for i in range(num):
        if i in primelist:
            a.pendown()
            a.dot(4)
            a.penup()
        a.forward(2+i/4)
        a.right(30-i/12)


elif type == "3":
    for i in range(num):
        a.speed(0)
        vt = i / 30 * math.pi
        cordx = (vt * 2) * math.cos(vt)
        cordy = (vt * 2) * math.sin(vt)
        a.goto(cordx,cordy)
        a.dot(4)
    

elif type == "4":
    for i in range(num):
        vt = i / 10 * math.pi
        cordx = (vt * 2) * math.cos(vt)
        cordy = (vt * 2) * math.sin(vt)
        a.goto(cordx,cordy)
        if i in primelist:
            a.dot(4)





elif type == "5":
    dis = 5
    act = 1
    cant = 1
    for i in range(num):
        def ciclo():
            for r in range(cant):
                for p in range(2):
                    a.dot(4)
                    a.forward(dis)
            a.forward(dis)
            a.left(90)
            a.dot(4)
        if act == 1:
            ciclo()
            act +=1
        elif act == 2:
            ciclo()
            dis +=5
            act = 1







#(dot forward turn)*2 (dot forward dot forward turn)*2
"""act = 1
for i in range(num):
    for x in range(act):
        for p in range(2):
            a.dot(4)
            a.forward(5)
            a.left(90)"""


screen.exitonclick()


"""
tim = turtle.Turtle()
tim.color("red")
tim.pensize(5)
tim.shape("arrow")
tim.speed(50)
tim.hideturtle()


tim.circle(2)
for x in range(4):
    tim.penup()
    tim.left(90)
    tim.forward(20)
    tim.pendown()
    tim.circle(2)
"""
