import re

er_telefono = re.compile("\d\d\d-\d\d\d-\d\d\d")

mismuertos = "mi telefono es 646-640-981"

resultado = er_telefono.search(mismuertos)


print("numero encontrado: ", resultado.group())




buscando = re.compile("probando")

frase = "la funcion se hace probando"

buscar = buscando.search(frase)

print("funcion encontrada: ", buscar.group())

