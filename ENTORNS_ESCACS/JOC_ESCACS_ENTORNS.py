def comprovar_enter(text):
    valor=False
    try:
        while valor==False:
            valor=int(input(text))
            if valor==False:
                print("Cal introduir un enter")
    except ValueError:
        print("Introdueix un valor vàlid")
    except Exception as e:
        print(type(e))
        print(e)
    return valor

def assignar_jugadors():
    global jugadors,colors_jugadors
    colores=["blanc","negre"]
    colors_jugadors=[]
    jugadors=[]
    color1=False
    color2=""
    jugador1=input("Introdueix el nom del jugador1: ")
    jugadors.append(jugador1)
    while color1==False:
        color1=input("Introdueix amb quin color voldras jugar (blanc/negre): ")
        if color1 not in colores:
            color1=False
            print("EL color ha de ser blanc o negre")
    colors_jugadors.append(color1)
    jugador2=input("Introdueix el nom del jugador2: ")
    jugadors.append(jugador2)
    if color1=="blanc":
        color2="negre"
    else:
        color2="blanc"
    colors_jugadors.append(color2)
    print(f"Jugaran el/la {jugador1} ({color1}) contra el/la {jugador2} ({color2}), BONA SORT!")
    return jugadors,colors_jugadors
    

    

def crear_tauler():
    global tauler
    tauler = [
    [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    ['1', 't', 'c', 'a', 'q', 'k', 'a', 'c', 't'],
    ['2', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['3', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['4', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['5', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['6', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['7', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['8', 'T', 'C', 'A', 'Q', 'K', 'A', 'C', 'T']]

    return tauler

def validar_coordenadas(coords):
    coordenades_lletres=["a","b","c","d","e","f","g","h"]
    coordenades_numeros=["1","2","3","4","5","6","7","8"]
    if coords[0] not in coordenades_lletres:
        print("Lletra de la coordenada incorrecte")
        return False
    if coords[1] not in coordenades_numeros:
        print("Numero de la coordenada incorrecte")
        return False
        

    if len(coords)!=2:
        print("longitud de la coordenada erronea")
        return False
    
    return True


def validar_errors_generals(color,fila_inicial,columna_inicial, fila_final,columna_final):
    peça = tauler[fila_inicial][columna_inicial]
    posicio_desti = tauler[fila_final][columna_final]

    if color == "blanc" and peça.islower():
        print("Peça incorrecte")
        return False
        
    elif color =="negre" and peça.isupper():
        print("Peça incorrecte")
        return False
    
    elif peça==".":
        print("Has de seleccionar una peça")
        return False

    if color == "blanc" and posicio_desti.isupper():
        print("No pots sobreposar les teves propies peçes")
        return False
        
    elif color == "negre" and posicio_desti.islower():
        print("No pots sobreposar les teves propies peçes")
        return False
    return True


def peon(color,fila_final,fila_ini,columna_final,columna_ini):
    if tauler[fila_final][columna_final]==".":

        #----PEON BLANC-----
        if color=="blanc":
            if columna_final==columna_ini:
                if fila_ini==7 and fila_ini-fila_final>1:
                    if tauler[fila_final][columna_final]=="." and tauler[fila_ini-1][columna_final]!=".":
                        print("No pots saltar per sobre de peças")
                        return False
                if fila_ini==7 and fila_ini-fila_final<=2:
                    tauler[fila_final][columna_final]="P"
                    tauler[fila_ini][columna_ini]="."
                    return True
                elif fila_ini!=7 and fila_ini-fila_final==1:
                    tauler[fila_final][columna_final]="P"
                    tauler[fila_ini][columna_ini]="."
                    return True
                elif fila_ini!=7 and fila_ini-fila_final>1:
                    print("No pots avançar dos caselles amb el peo perque no esta a la posicio inicial")
                    return False
                elif fila_ini==7 and fila_ini-fila_final>2:
                    print("No pots avançar mes de dos caselles amb el peo desde la posicio inicial")
                    return False
                elif tauler[fila_ini][columna_ini]!="P":
                    print("Has de seleccionar una peça blanca")
                    return False
                
                #CAPTURA BLANQUES
            else:
                if tauler[fila_final][columna_final]!=".":
                    if fila_ini-fila_final>2 or columna_final==columna_ini:
                        print("No pots capturar")
                        return False
                    elif tauler[fila_final][columna_final]!="P" and fila_ini==fila_final+1:
                        print("Peça capturada")
                        tauler[fila_final][columna_final]="P"
                        tauler[fila_ini][columna_ini]="."
                        return True
            
        #-----PEON NEGRE-----
        if color=="negre":
            if columna_final==columna_ini:
                if fila_ini==2 and fila_final-fila_ini>1:
                    if tauler[fila_final][columna_final]=="." and tauler[fila_ini+1][columna_final]!=".":
                        print("No pots saltar per sobre de peces")
                        return False
                if fila_final-fila_ini<=2:
                    tauler[fila_final][columna_final]="p"
                    tauler[fila_ini][columna_ini]="."
                    return True
                elif fila_ini!=2 and fila_final-fila_ini==1:
                    tauler[fila_final][columna_final]="p"
                    tauler[fila_ini][columna_ini]="."
                    return True
                elif fila_ini!=2 and fila_final-fila_ini>1:
                    print("No pots avançar dos caselles amb el peo perque no esta a la posicio inicial")
                    return False
                
                elif fila_ini==2 and fila_final-fila_ini>1:
                    if tauler[fila_final][columna_final]=="." and tauler[fila_ini+1][columna_final]!=".":
                        print("No pots saltar per sobre de peças")
                        return False
                elif  fila_ini==2 and fila_final-fila_ini>2:
                    print("No pots avançar mes de dos caselles amb el peo desde la posicio inicial")
                    return False
                elif tauler[fila_ini][columna_ini]!="p":
                    print("Has de seleccionar una peça negre")
                    return False
                
            #CAPTURA NEGRES
            else:
                if tauler[fila_final][columna_final]!="." and color=="negre":
                    if fila_final-fila_ini>2 or columna_final==columna_ini:
                        print("No pots capturar")
                        return False
                    elif tauler[fila_final][columna_final].isupper() and fila_ini==fila_final-1:
                        print("Peça capturada")
                        tauler[fila_final][columna_final]="p"
                        tauler[fila_ini][columna_ini]="."
                        return True
    print("Acció no valida")
    return False


def cavall(color,fila_final,fila_ini,columna_final,columna_ini):

    if (abs(fila_final-fila_ini)==2 and abs(columna_final-columna_ini)==1) or \
    (abs(fila_final-fila_ini)==1 and abs(columna_final-columna_ini)==2):

        peça_dest = tauler[fila_final][columna_final]

        if color=="blanc":
            if peça_dest=="." or peça_dest.islower():
                tauler[fila_final][columna_final]="C"
                tauler[fila_ini][columna_ini]="."
                return True

        if color=="negre":
            if peça_dest=="." or peça_dest.isupper():
                tauler[fila_final][columna_final]="c"
                tauler[fila_ini][columna_ini]="."
                return True

    print("Accio no valida pel cavall")
    return False

def torre(color,fila_final,fila_ini,columna_final,columna_ini):

    if fila_ini!=fila_final and columna_ini!=columna_final:
        print("La torre es mou en linia recta")
        return False

    # Movimiento vertical
    if columna_ini==columna_final:
        pas = 1 if fila_final>fila_ini else -1
        for f in range(fila_ini+pas, fila_final, pas):
            if tauler[f][columna_ini]!=".":
                print("No pots saltar peces")
                return False

    # Movimiento horizontal
    if fila_ini==fila_final:
        pas = 1 if columna_final>columna_ini else -1
        for c in range(columna_ini+pas, columna_final, pas):
            if tauler[fila_ini][c]!=".":
                print("No pots saltar peces")
                return False

    peça_dest = tauler[fila_final][columna_final]

    if color=="blanc":
        if peça_dest=="." or peça_dest.islower():
            tauler[fila_final][columna_final]="T"
            tauler[fila_ini][columna_ini]="."
            return True

    if color=="negre":
        if peça_dest=="." or peça_dest.isupper():
            tauler[fila_final][columna_final]="t"
            tauler[fila_ini][columna_ini]="."
            return True

    print("Moviment invalid per la torre")
    return False

def alfil(color,fila_final,fila_ini,columna_final,columna_ini):

    if abs(fila_final-fila_ini) != abs(columna_final-columna_ini):
        print("L'alfil es mou en diagonal")
        return False

    pas_f = 1 if fila_final>fila_ini else -1
    pas_c = 1 if columna_final>columna_ini else -1

    f = fila_ini + pas_f
    c = columna_ini + pas_c

    while f != fila_final and c != columna_final:
        if tauler[f][c]!=".":
            print("No pots saltar peces")
            return False
        f += pas_f
        c += pas_c

    peça_dest = tauler[fila_final][columna_final]

    if color=="blanc":
        if peça_dest=="." or peça_dest.islower():
            tauler[fila_final][columna_final]="A"
            tauler[fila_ini][columna_ini]="."
            return True

    if color=="negre":
        if peça_dest=="." or peça_dest.isupper():
            tauler[fila_final][columna_final]="a"
            tauler[fila_ini][columna_ini]="."
            return True

    print("Moviment invalid per l'alfil")
    return False

def reina(color,fila_final,fila_ini,columna_final,columna_ini):

    # Movimiento tipo torre
    if fila_ini==fila_final or columna_ini==columna_final:

        # Vertical
        if columna_ini==columna_final:
            pas = 1 if fila_final>fila_ini else -1
            for f in range(fila_ini+pas, fila_final, pas):
                if tauler[f][columna_ini]!=".":
                    print("No pots saltar peces")
                    return False

        # Horizontal
        if fila_ini==fila_final:
            pas = 1 if columna_final>columna_ini else -1
            for c in range(columna_ini+pas, columna_final, pas):
                if tauler[fila_ini][c]!=".":
                    print("No pots saltar peces")
                    return False

    # Movimiento tipo alfil
    elif abs(fila_final-fila_ini)==abs(columna_final-columna_ini):

        pas_f = 1 if fila_final>fila_ini else -1
        pas_c = 1 if columna_final>columna_ini else -1

        f = fila_ini + pas_f
        c = columna_ini + pas_c

        while f != fila_final and c != columna_final:
            if tauler[f][c]!=".":
                print("No pots saltar peces")
                return False
            f += pas_f
            c += pas_c

    else:
        print("Moviment invalid per la reina")
        return False

    peça_dest = tauler[fila_final][columna_final]

    if color=="blanc":
        if peça_dest=="." or peça_dest.islower():
            tauler[fila_final][columna_final]="Q"
            tauler[fila_ini][columna_ini]="."
            return True

    if color=="negre":
        if peça_dest=="." or peça_dest.isupper():
            tauler[fila_final][columna_final]="q"
            tauler[fila_ini][columna_ini]="."
            return True

    print("Moviment invalid per la reina")
    return False


def rei(color,fila_final,fila_ini,columna_final,columna_ini):

    if abs(fila_final-fila_ini)<=1 and abs(columna_final-columna_ini)<=1:

        peça_dest = tauler[fila_final][columna_final]

        if color=="blanc":
            if peça_dest=="." or peça_dest.islower():
                tauler[fila_final][columna_final]="K"
                tauler[fila_ini][columna_ini]="."
                return True

        if color=="negre":
            if peça_dest=="." or peça_dest.isupper():
                tauler[fila_final][columna_final]="k"
                tauler[fila_ini][columna_ini]="."
                return True

    print("Moviment invalid pel rei")
    return False


def convertir_coordenada(coord):
    lletra = coord[0]
    numero = coord[1]
    columna = tauler[0].index(lletra)
    fila=int(numero)
    return fila , columna

def partida():
    global torn
    assignar_jugadors()
    tauler=crear_tauler()
    torn=0
    i=0 #numero de jugador a qui li toca
    abandonar=""
    jugada_valida=False
    while abandonar!="abandonar":
        print("--- TAULER ---")
        for fila in tauler:
                for elemento in fila:
                    print(elemento,end=" ")
                print()
        if torn==0:
            print("Comencen blanques")
        print(f"\nTorn de {jugadors[i]},{colors_jugadors[i]}")
        abandonar=input(f"Vols abandonar la partida o seguir jugant? (per abandonar introdueix un espai, si no qualsevol altre tecla: ")
        if abandonar==" ":
            print(f"Ha guanyat {jugadors[(i+1)%2]}")
            break
        jugada_valida = False
        while not jugada_valida:
            coords_inicials=input("Introdueix les coordenades incials (format:lletranumero): ")
            coords_finals=input("Introdueix les coordenades finals (format:lletranumero): ")
            if validar_coordenadas(coords_inicials) and validar_coordenadas(coords_finals):
                jugada_valida=True
            if jugada_valida:
                fila_ini,col_ini=convertir_coordenada(coords_inicials)
                fila_final,columna_final=convertir_coordenada(coords_finals)
                jugada_valida=validar_errors_generals(colors_jugadors[i],fila_ini,col_ini,fila_final,columna_final)
                if jugada_valida:
                    if tauler[fila_ini][col_ini]=="P" or tauler[fila_ini][col_ini]=="p":
                        jugada_valida = peon(colors_jugadors[i],fila_final,fila_ini,columna_final,col_ini)
                        if jugada_valida:
                            torn+=1
                            i+=1
                            if i>=2:
                                i=0
                    elif tauler[fila_ini][col_ini]=="C" or tauler[fila_ini][col_ini]=="c":
                        jugada_valida=cavall(colors_jugadors[i],fila_final,fila_ini,columna_final,col_ini)
                        if jugada_valida:
                            torn+=1
                            i+=1
                            if i>=2:
                                i=0
                    elif tauler[fila_ini][col_ini]=="T" or tauler[fila_ini][col_ini]=="t":
                        jugada_valida = torre(colors_jugadors[i],fila_final,fila_ini,columna_final,col_ini)
                        if jugada_valida:
                            torn+=1
                            i+=1
                            if i>=2:
                                i=0

                    elif tauler[fila_ini][col_ini]=="A" or tauler[fila_ini][col_ini]=="a":
                        jugada_valida = alfil(colors_jugadors[i],fila_final,fila_ini,columna_final,col_ini)
                        if jugada_valida:
                            torn+=1
                            i+=1
                            if i>=2:
                                i=0
                    elif tauler[fila_ini][col_ini]=="Q" or tauler[fila_ini][col_ini]=="q":
                        jugada_valida = reina(colors_jugadors[i],fila_final,fila_ini,columna_final,col_ini)
                        if jugada_valida:
                            torn+=1
                            i+=1
                            if i>=2:
                                i=0

                    elif tauler[fila_ini][col_ini]=="K" or tauler[fila_ini][col_ini]=="k":
                        jugada_valida = rei(colors_jugadors[i],fila_final,fila_ini,columna_final,col_ini)
                        if jugada_valida:
                            torn+=1
                            i+=1
                            if i>=2:
                                i=0


                    
if __name__=="__main__":
    partida()

