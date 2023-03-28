import turtle


num = int(input("cantidad"))
a = turtle.Turtle()
a.speed(0)
a.hideturtle()
screen = turtle.Screen()






act = 1
for i in range(num):
    for x in range(act):
        for p in range(2):
            a.dot(4)
            a.forward(5)
            a.left(90)
        act += 1

screen.exitonclick()
