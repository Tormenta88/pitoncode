#Importamos las librerias usadas
import random
import os
import sys
import string

#Definimos los colores
DEFAULT = '\033[0m'
GREEN = '\033[92m'
YELLOW = '\033[33m'

#Selección de palabra aleatoria
idioma = 0
lista_palabras = ['SALIR', 'TENER', 'TOCAR', 'GOLPE', 'HACER', 'NUEVO', 'DESEO', 'APOYO', 'VALOR', 'PODER', 'CREAR', 'MIEDO', 'PERRO', 'SUBIR', 'ORDEN', 'MUCHO', 'SABER', 'COMER', 'TOMAR', 'LARGO', 'PEDIR', 'SACAR' 'PONER', 'CAUSA', 'AMIGO', 'BAJAR', 'MUJER', 'KARMA', 'ARMAR', 'PARTE', 'MUNDO', 'NIVEL', 'MEJOR', 'GRUPO', 'FELIZ', 'DONDE', 'HECHO', 'JUGAR', 'DECIR', 'CARTA', 'DULCE', 'BELLA', 'CLARO', 'FINAL', 'MAYOR', 'LUEGO', 'SNACK', 'BUENO', 'REGLA', 'LUGAR', 'ETAPA', 'SABIO', 'ANTES', 'FORMA', 'DEJAR', 'MIRAR', 'TENAZ', 'COGER', 'TAREA', 'CALMA', 'AYUDA', 'AHORA', 'VIAJE', 'DEBER', 'CERCA', 'IDEAL', 'NORMA', 'FALTA', 'DICHA', 'LLENO', 'HUECO', 'TANTO', 'CAMPO', 'NUNCA', 'PAPEL', 'GIRAR', 'FRASE', 'SUAVE', 'PUNTO', 'LIBRO', 'VOLAR', 'LENTO', 'SALUD', 'DOTAR', 'TARDE', 'LIBRE', 'CULPA', 'PASAR', 'DOLOR', 'BREVE', 'FRIKI', 'YERNO', 'FLUJO', 'LINDO', 'CAPAZ', 'VENTA', 'CIELO', 'HABER', 'TRAER', 'PLUMA', 'ABRIR', 'VIEJO', 'MATAR', 'BANAL', 'LOCAL', 'ICONO', 'FLACO', 'OVEJA', 'LABOR', 'RUMBO', 'GLOBO', 'TOTAL', 'GRITO', 'FIRME', 'DENSO', 'POBRE', 'COPIA', 'ESTAR', 'IGUAL', 'OSADO', 'VIVIR', 'GORDO', 'SENDA', 'CHICO', 'CIEGO', 'VASTO', 'CLASE', 'TEMOR', 'PARAR', 'PAGAR', 'CREER', 'SERIO', 'VELOZ', 'LEJOS', 'MISMO', 'HONOR', 'OPTAR', 'SOBRE', 'BASAR', 'MORIR', 'MEDIO', 'AUDAZ', 'ERROR', 'COLOR', 'MOTOR', 'CURAR', 'JOVEN', 'OCASO', 'PARCO', 'DIETA', 'SUELO', 'JUSTO', 'CORTE', 'PLANO', 'BURDO', 'GANAR', 'ECHAR', 'GRAVE', 'GRATO', 'BROMA', 'GENTE', 'PIEZA', 'SUCIO', 'VISTO', 'AJENO', 'GOZAR', 'TEXTO', 'CULTO', 'DONAR', 'FUROR', 'QUEJA', 'CORTO', 'CLAVE', 'DURAR', 'USTED', 'BRISA', 'VALLA', 'HOGAR', 'FONDO', 'OBVIO', 'GUSTO', 'BELLO', 'METER', 'HACER', 'CAUTO', 'LISTO', 'SELLO', 'MEDIR', 'MOVER', 'GUAPA', 'HASTA', 'FLUIR', 'RUEDA', 'PAUSA', 'LECHO', 'TONTO', 'CELOS', 'LEGAL', 'CASTA', 'AROMA', 'STOCK', 'PEGAR', 'PUNTA', 'DICHO', 'CINTA', 'PASTO', 'BEBER', 'CICLO', 'REGAR', 'PADRE', 'TURNO', 'NOCHE', 'PLAYA', 'DANZA', 'CALOR', 'JUEGO', 'ANDAR', 'LOGRO', 'LUCHA', 'BINGO', 'OASIS', 'ROBAR', 'TEJER', 'RECTO', 'AZADA', 'MADRE', 'NEGRO', 'VERDE', 'SUMAR', 'AGRIO', 'RESTA', 'VORAZ', 'ENOJO', 'VICIO', 'PESAR', 'PELEA', 'FRUTO', 'CERDO', 'BURLA', 'FALSO', 'CIFRA', 'ACTOR', 'FIJAR', 'BURRO', 'DUDAR', 'JUNTO', 'CARRO', 'MONTE', 'DEUDA', 'HUEVO', 'SIGNO', 'TAPAR', 'TENUE', 'SUTIL', 'MENTE', 'CARGO', 'PISAR', 'RUBRO', 'PISTA', 'CLIMA', 'CLARA', 'COSTA', 'TRAMA', 'FAUNA', 'LINDA', 'TRATO', 'NOTAR', 'MARCO', 'AXIAL', 'ZORRO', 'PULSO', 'NOBLE', 'OBRAR', 'RIGOR', 'OBESO', 'REGIR', 'VITAL', 'CALLE', 'RUIDO', 'SERIE', 'ILUSO', 'FAVOR', 'TOPAR', 'AUTOR', 'GUIAR', 'VERAZ', 'TIRAR', 'ANCHO', 'SAGAZ', 'SHOCK', 'DOSIS', 'DRAMA', 'CEDER', 'BARCO', 'CURSO', 'BUSCA', 'ROGAR', 'GUAPO', 'FUERA', 'PRADO', 'MARCA', 'CRUEL', 'RITMO', 'STAFF', 'GESTO', 'CITAR', 'VALLE', 'YACER', 'NUEVA', 'BAILE', 'VELAR', 'LLAMA', 'CHICA', 'OMISO', 'CUEVA', 'PILAR', 'HABLA', 'AMENO', 'USADO', 'VISTA', 'VUELO', 'VIGOR', 'SILLA', 'DUELO', 'AGUDO', 'TORPE', 'FURIA', 'HOBBY', 'AVISO', 'TROZO', 'FALLO', 'HIELO', 'SOCIO', 'RURAL', 'HUMOR', 'SENIL', 'CABAL', 'PARED', 'CAGAR', 'FEROZ', 'METAL', 'LUCRO', 'MITAD']
word_list = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY', 'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD', 'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT', 'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT', 'DRAMA', 'DRAWN', 'DREAM', 'DRESS', 'DRILL', 'DRINK', 'DRIVE', 'DROVE', 'DYING', 'EAGER', 'EARLY', 'EARTH', 'EIGHT', 'ELITE', 'EMPTY', 'ENEMY', 'ENJOY', 'ENTER', 'ENTRY', 'EQUAL', 'ERROR', 'EVENT', 'EVERY', 'EXACT', 'EXIST', 'EXTRA', 'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD', 'FIFTH', 'FIFTY', 'FIGHT', 'FINAL', 'FIRST', 'FIXED', 'FLASH', 'FLEET', 'FLOOR', 'FLUID', 'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME', 'FRANK', 'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FULLY', 'FUNNY', 'GIANT', 'GIVEN', 'GLASS', 'GLOBE', 'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT', 'GRASS', 'GREAT', 'GREEN', 'GROSS', 'GROUP', 'GROWN', 'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'HAPPY', 'HARRY', 'HEART', 'HEAVY', 'HENCE', 'HENRY', 'HORSE', 'HOTEL', 'HOUSE', 'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INNER', 'INPUT', 'ISSUE', 'JAPAN', 'JIMMY', 'JOINT', 'JONES', 'JUDGE', 'KNOWN', 'LABEL', 'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEASE', 'LEAST', 'LEAVE', 'LEGAL', 'LEVEL', 'LEWIS', 'LIGHT', 'LIMIT', 'LINKS', 'LIVES', 'LOCAL', 'LOGIC', 'LOOSE', 'LOWER', 'LUCKY', 'LUNCH', 'LYING', 'MAGIC', 'MAJOR', 'MAKER', 'MARCH', 'MARIA', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT', 'MEDIA', 'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MOTOR', 'MOUNT', 'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC', 'NEEDS', 'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED', 'NOVEL', 'NURSE', 'OCCUR', 'OCEAN', 'OFFER', 'OFTEN', 'ORDER', 'OTHER', 'OUGHT', 'PAINT', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PHOTO', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLAIN', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIME', 'PRINT', 'PRIOR', 'PRIZE', 'PROOF', 'PROUD', 'PROVE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH', 'READY', 'REFER', 'RIGHT', 'RIVAL', 'RIVER', 'ROBIN', 'ROGER', 'ROMAN', 'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SERVE', 'SEVEN', 'SHALL', 'SHAPE', 'SHARE', 'SHARP', 'SHEET', 'SHELF', 'SHELL', 'SHIFT', 'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED', 'SKILL', 'SLEEP', 'SLIDE', 'SMALL', 'SMART', 'SMILE', 'SMITH', 'SMOKE', 'SOLID', 'SOLVE', 'SORRY', 'SOUND', 'SOUTH', 'SPACE', 'SPARE', 'SPEAK', 'SPEED', 'SPEND', 'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAFF', 'STAGE', 'STAKE', 'STAND', 'START', 'STATE', 'STEAM', 'STEEL', 'STICK', 'STILL', 'STOCK', 'STONE', 'STOOD', 'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'SUITE', 'SUPER', 'SWEET', 'TABLE', 'TAKEN', 'TASTE', 'TAXES', 'TEACH', 'TEETH', 'TERRY', 'TEXAS', 'THANK', 'THEFT', 'THEIR', 'THEME', 'THERE', 'THESE', 'THICK', 'THING', 'THINK', 'THIRD', 'THOSE', 'THREE', 'THREW', 'THROW', 'TIGHT', 'TIMES', 'TIRED', 'TITLE', 'TODAY', 'TOPIC', 'TOTAL', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY', 'TRUST', 'TRUTH', 'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL', 'UPPER', 'UPSET', 'URBAN', 'USAGE', 'USUAL', 'VALID', 'VALUE', 'VIDEO', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHEEL', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD', 'WORRY', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG', 'WROTE', 'YIELD', 'YOUNG', 'YOUTH']
lista_intentos = []
colores = [[],[],[],[],[],[DEFAULT]]
resultado = ""
alphabet = list(string.ascii_uppercase)

while idioma != 1 or idioma != 2:
    idioma = input("\033c \nIntroduce el idioma en el que prefieres jugar.\n 1 Para Español 2 para ingles\n")
    try:
        if int(idioma) == int:
            idioma == int(idioma)
    except:
        print("Eso no es un número valido")
    if idioma == 1 or idioma == 2:
        break
if idioma == 2:
    palabra = word_list[random.randint(1, len(word_list))]
elif idioma == 1:
    palabra = lista_palabras[random.randint(1, len(lista_palabras))]



#Declaramos las funciones

#Funcion para el color de las letras
def colorin(a):
    if a == 0:
        colores[n].append(GREEN)
        colores[n].append(intento[n])
    elif a == 1:
        colores[n].append(YELLOW)
        colores[n].append(intento[n])
    elif a == 2:
        colores[n].append(DEFAULT)
        colores[n].append(intento[n])
#Funcion para resetear el programa
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Introducción
print("\033c")
print("Bienvenido a nuestra version de Wordle\n Introduce tu primera palabra para comenzar")
print(" Si introduces un caracter que no sea una letra seras penalizado perdiendo un intento")
print(" Introduce solo una R en cualquier momento del juego para volver a empezar")

#Número de intentos
vidas = 0
#Inicio del bucle principal
while vidas < 6:
    intento = input("\n").upper()
    for x in range(len(intento)):
        if intento[x] not in alphabet:
            print("Algun caracter introducido no es una letra")
            intento = input("\n").upper()
    copiastr = str(palabra)

#Botón para reiniciar
    if intento == "R":
        restart_program()
    print("\033c")
    print("Introduce solo una R en cualquier momento del juego para volver a empezar")

    for x in lista_intentos:
        print(x)
#Comprobamos que la palabra es de 5 letras
    if len(intento) == 5:
        for n in range(len(intento)):
            #Comprobamos que la letra esta dentro de la palabra
            if intento[n] in copiastr:
                #Comprobamos si la posición es igual
                if intento[n] == copiastr[n]:
                    colorin(0)

                else:
                    colorin(1)

            elif intento[n] != copiastr:
                colorin(2)
        #Juntamos las letras y sus respectivos colores de la lista "colores"
        for x in range(len(colores)):
            resultado += " ".join(colores[x])
        #Lo añadimos a los resultados para luego mostrarlos al inicio de cada repetición del bucle
        lista_intentos.append(resultado)
        #Lógica para ganar
        if intento == palabra:
            print("\nHas Ganado\n")
            exit()
        elif intento != palabra:
            vidas += 1
        print(resultado)
        #Reseteamos las variables
        colores = [[],[],[],[],[],[DEFAULT]]
        resultado = ""
    #Excepción para cuando no se cumplan las 5 letras
    else:
        print("Tu palabra tiene más o menos de 5 letras")
#Lógica para perder
if vidas == 6:
    print("\nHas perdido\n")
    print(f"La palabra era {palabra}")

