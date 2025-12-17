import random
dado1=0
dado2=0

def tirada(posicio):
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    if posicio >=60:
        resultat_tirada=dado1
        print(f"{lista_jugadors[i]} ha llençat i ha tret {dado1} resultat: {resultat_tirada}")
    else:
        resultat_tirada=dado1+dado2
        print(f"{lista_jugadors[i]} ha llençat i ha tret {dado1} i {dado2}, resultat: {resultat_tirada}")
    return resultat_tirada

def llançar():
    global contador_tiradas,dado1,dado2,exceso
    print(f"És el torn del jugador {i+1}, {lista_jugadors[i]}")
    tirar=""
    while tirar!="tiro":
        tirar=input("Introdueix 'tiro' per llençar els daus: ")
        if tirar!="tiro":
            print("Has d'introduir 'tiro'")
    resultat_daus = tirada(posicions[i])
    print(f"Avançes {resultat_daus} caselles")
    posicions[i]+=resultat_daus
    print(f"Estas a la casella {posicions[i]}")
    contador_tiradas+=1
    
    if posicions[i]>63:
        exceso=posicions[i]-63
        posicions[i]=63-exceso

    return posicions

oca=[5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]

def daus_especials():
    global posicions
    if posicions[i]==0:
        if dado1==3 and dado2==6:
            posicions[i]=26
            print("Avances fins la casella 26")
            print("De dado a dado y tiro porque me ha tocado.")
            return
        elif dado1==4 and dado2==5:
            print("Avances fins la casella 53")
            posicions[i]=53

def casella_oca():
    global posicions
    if posicions[i] in oca:
        index_oca = oca.index(posicions[i])  
        if index_oca < len(oca) - 1:
            posicions[i] = oca[index_oca + 1]
            print("De oca en oca i tiro perquè em toca")
            print(f"Avances fins la casella {posicions[i]}")
            print(f"El jugador {i+1} torna a tirar")

def casella_pont():
    global posicions
    if posicions[i]==6 or posicions[i]==12:
        print("Has caigut a la casella de pont")
        if posicions[i]==6:
            posicions[i]=12
            print(f"Viatjes fins la casella {posicions[i]}")
            print(f"El jugador {i+1} torna a tirar")
        else:
            posicions[i]=6
            print(f"Viatjes fins la casella {posicions[i]}")
            print(f"El jugador {i+1} torna a tirar")

def casella_fonda():
    global penalizaciones
    if posicions[i]==19:
        print("Has caigut a la Fonda, no et pots moure la seguent jugada")
        penalizaciones[i]+=1

def casella_pou():
    global jugador_pou, penalizaciones
    if posicions[i] == 31:
        print("Has caigut al pou, no et pots moure en dos torns o si un jugador també cau al pou")
        if jugador_pou is not None:
            penalizaciones[jugador_pou]=0
        jugador_pou=i
        penalizaciones[i]+=2

def casella_laberint():
    global posicions
    if posicions[i]==42:
        print("Has caigut al laberint, tornes a la casella 39")
        posicions[i]=39

def casella_preso():
    global penalizaciones
    if posicions[i]==52:
        print("Has caigut a la presó, no et pots moure en tres torns")
        penalizaciones[i]+=3

def casella_mort():
    global posicions
    if posicions[i]==58:
        print("Has caigut a la mort, tornes al principi")
        posicions[i]=0

def casella_jardi_oca():
    if posicions[i]==63:
        print(f"Felicitats!! El jugador {i+1}, {lista_jugadors[i]} ha guanyat.")



if __name__ == '__ main __':

    print("--- BENVINGUT AL JOC DE LA OCA! ---")
    nombre_jugadors=None
    lista_jugadors=[]

    while nombre_jugadors==None:
        try:
            nombre_jugadors=int(input("Introdueix el nombre de jugadors (2-4): "))
            if nombre_jugadors<2 or nombre_jugadors>4:
                nombre_jugadors=None
                print("Has d'introduir un numero entre 2 i 4!")
        except ValueError:
            print("Error de format, introdueix un numero")
        except Exception as e:
            print(e)
            print(type(e))
    for i in range(nombre_jugadors):
        try:
            nom=input(f"Introdueix el nom del jugador {i+1}: ")
            lista_jugadors.append(nom)
        except ValueError:
            print("Error de format")
        except Exception as e:
            print(e)
            print(type(e))
    print(f"Els jugadors que participaran son: {lista_jugadors}, bona sort!")

    posicions = [0] * nombre_jugadors
    penalizaciones=[0] * nombre_jugadors
    contador_tiradas=0
    jugador_pou=None
    i=0 #jugador a qui li toca

    while 63 not in posicions:
        if penalizaciones[i] > 0:
            penalizaciones[i] -= 1
            i += 1
            if i >= len(lista_jugadors):
                i = 0
            continue

        llançar()
        
        #Daus 3-6 i 4-6
        daus_especials()

        #oca
        casella_oca()
        
        #pont
        casella_pont()
        
        #fonda
        casella_fonda()
        
        #pou
        casella_pou()
        
        #laberint
        casella_laberint()
        
        #preso
        casella_preso()
        
        #mort
        casella_mort()
        
        #jardi oca
        casella_jardi_oca()
        
        i+=1
        if i >= len(lista_jugadors):
            i=0
