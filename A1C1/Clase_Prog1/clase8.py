"""def funcion(a, b):
    if a > b:
        return a
    else:
        return b

print(funcion(2,2))"""

"""def funcion(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
print(funcion(2,3,4))
"""

#inversa
"""def funcion(a):
    invertido = []
    for x in a:
        invertido.append(x)
    for i in range(1, len(a) + 1):
        invertido[i-1] = a[-i]
    if a == "".join(invertido):
        print("Es un palindromo")
    else:
        print("No es un palindromo")
funcion("olo")"""

"""
s = "ciertamente"
result = ""
for x in range(len(s)-1, -1, -1):
    result += s[x]
print(result)
"""

#Histograma que tome una lista de enteros y devuelva un histograma en la pantalla
def funcion(a):
    a = str(a)
    for i in range(len()):
        print(i*"x")



funcion(231)