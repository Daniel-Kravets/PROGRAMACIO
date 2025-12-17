import random

#FUNCIONS


def tirada(posicio):
    global dado1, dado2
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    if posicio >= 60:
        resultat_tirada = dado1
        print(f"{lista_jugadors[i]} ha llençat i ha tret {dado1} resultat: {resultat_tirada}")
    else:
        resultat_tirada = dado1 + dado2
        print(f"{lista_jugadors[i]} ha llençat i ha tret {dado1} i {dado2}, resultat: {resultat_tirada}")

    return resultat_tirada


def llançar():
    global contador_tiradas, dado1, dado2, exceso

    print(f"És el torn del jugador {i+1}, {lista_jugadors[i]}")
    tirar = ""

    while tirar != "tiro":
        tirar = input("Introdueix 'tiro' per llençar els daus: ")
        if tirar != "tiro":
            print("Has d'introduir 'tiro'")

    resultat_daus = tirada(posicions[i])
    print(f"Avançes {resultat_daus} caselles")

    posicions[i] += resultat_daus
    print(f"Estas a la casella {posicions[i]}")

    if posicions[i] > 63:
        exceso = posicions[i] - 63
        posicions[i] = 63 - exceso

    return posicions

def daus_especials():
    if dado1 == 3 and dado2 == 6:
            posicions[i] = 26
            print("Avances fins la casella 26")
            print("De dado a dado y tiro porque me ha tocado.")
    elif dado1 == 4 and dado2 == 5:
        posicions[i] = 53
        print("Avances fins la casella 53")
        print("De dado a dado y tiro porque me ha tocado.")

def casella_oca():
    index_oca = oca.index(posicions[i])
    if index_oca < len(oca) - 1:
        posicions[i] = oca[index_oca + 1]
        print("De oca en oca i tiro perquè em toca")
        print(f"Avances fins la casella {posicions[i]}")
        print(f"El jugador {i+1} torna a tirar")

def casella_pont():
    print("Has caigut a la casella de pont")
    if posicions[i] == 6:
        posicions[i] = 12
    else:
        posicions[i] = 6
    print(f"Viatjes fins la casella {posicions[i]}")
    print(f"El jugador {i+1} torna a tirar")

def fonda():
    print("Has caigut a la Fonda, no et pots moure la seguent jugada")
    penalizaciones[i] += 1


def casella_pou():
    jugador_pou = None
    print("Has caigut al pou, no et pots moure en dos torns o si un jugador també cau al pou")
    if jugador_pou is not None:
        penalizaciones[jugador_pou] = 0
    jugador_pou = i
    penalizaciones[i] += 2

def laberint():
    print("Has caigut al laberint, tornes a la casella 39")
    posicions[i] = 39

def preso():
    print("Has caigut a la presó, no et pots moure en tres torns")
    penalizaciones[i] += 3

def mort():
    print("Has caigut a la mort, tornes al principi")
    posicions[i] = 0

def comprovar_jugadors(texto):
    nombre_jugadors=None
    while nombre_jugadors is None:
        try:
            nombre_jugadors=int(input(f"{texto}: "))
            if nombre_jugadors<2 or nombre_jugadors>4:
                print("Cal introduir un numero entre 2 i 4")
                nombre_jugadors=None
            else:
                print(f"Valor correctament introduit, jugaran {nombre_jugadors} persones")
        except ValueError:
            print("Error de format, introdueix un numero")
        except Exception as e:
            print(e)
            print(type(e))
    return nombre_jugadors

def noms_jugadors():
    for i in range(nombre_jugadors):
        try:
            nom = input(f"Introdueix el nom del jugador {i+1}: ")
            lista_jugadors.append(nom)
        except ValueError:
            print("Error de format")
        except Exception as e:
            print(e)
            print(type(e))
    return lista_jugadors


#Assignació variables

oca = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
dado1 = 0
dado2 = 0
lista_jugadors = []



if __name__=="__main__":

    print("--- BENVINGUT AL JOC DE LA OCA! ---")

    nombre_jugadors=comprovar_jugadors("Introdueix el nombre de jugadors(2-4): ")
    lista_jugadors=noms_jugadors()

    print(f"Els jugadors que participaran son: {lista_jugadors}, bona sort!")

    posicions = [0] * nombre_jugadors
    penalizaciones = [0] * nombre_jugadors
    

    i = 0  # jugador a qui li toca

    while 63 not in posicions:

        if penalizaciones[i] > 0:
            penalizaciones[i] -= 1
            i += 1
            if i >= len(lista_jugadors):
                i = 0
            continue

        llançar()

        # Daus 3-6 i 4-6
        if posicions[i] == 0:
            daus_especials()
            continue

        # oca
        if posicions[i] in oca:
            casella_oca()
            continue

        # pont
        if posicions[i] == 6 or posicions[i] == 12:
            casella_pont()
            continue

        # fonda
        if posicions[i] == 19:
            fonda()

        # pou
        if posicions[i] == 31:
            casella_pou()

        # laberint
        if posicions[i] == 42:
            laberint()

        # preso
        if posicions[i] == 52:
            preso()

        # mort
        if posicions[i] == 58:
            mort()

        # jardi oca
        if posicions[i] == 63:
            print(f"Felicitats!! El jugador {i+1}, {lista_jugadors[i]} ha guanyat.")
            break

        i += 1
        if i >= len(lista_jugadors):
            i = 0
