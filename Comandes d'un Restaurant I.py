afegir_producte=""
ticket=""               #declaracio de variables
total=0
nom_client=""


def afegir_productes():  #metode per afegir els productes al string (tickets)
    global ticket,subtotal,total,nom_producte,nom_client
    afegir_producte = "s"
    while afegir_producte!="n":
            nom_producte=input("Introdueix el nom del producte: ")
            quantitat=int(input("Introdueix la quantitat del producte: "))
            preu_unitari=float(input("Introdueix el preu unitari del producte: "))
            subtotal=quantitat*preu_unitari
            total+=subtotal
            ticket += f"{nom_producte:15}{quantitat:^12}{preu_unitari:>12.2f}€{subtotal:>12.2f}€\n"
            afegir_producte=input("Vols afegir un altre producte? (s/n): ").lower()


def demanar_nom_client():
    global nom_client
    nom_client=""
    while not nom_client:
        nom_client=input("Introdueix el nom del client: ")     #Metode per demanar el nom del client i comprovar que estigui correctament escrit
        if not nom_client.isalpha():
            print("El nom no pot contenir números")
            nom_client = ""
    return nom_client
          
def crear_nova_comanda():
    global nom_client, ticket
    ticket = ""                     #metode per iniciar una nova comanda i posar els productes amb els preus i tot el que comporta
    demanar_nom_client()
    print("============ NOVA COMANDA ============")
    afegir_productes()



def IVA():          #metode per aplicar impostos a la comanda i imprimir a sota del string ticket
    global total
    iva=total*0.1
    total_amb_iva=total+iva
    impostos=f"Total sense IVA: {total:>35.2f} €\nIVA (10%): {iva:>41.2f} €\nTOTAL A PAGAR: {total_amb_iva:>37.2f} €"
    print(impostos)

def generar_tiquet():       #plantilla del ticket
    print("S'esta generant el ticket...")
    print("=============== TIQUET ===============\n")
    print(f"Client: {nom_client}\n")
    print("Producte        Quantitat   Preu unit.   Subtotal")
    print("--------------------------------------------------")
    print(ticket)
    print("--------------------------------------------------")
    IVA()
    print("==================================================")

def actualitzar_ticket(): #menu d'actualitzacion
    global nom_client,ticket,subtotal,total
    opcio_actu=0
    while opcio_actu!=3:
        print("=====MENU ACTUALIZACIO=====")
        print("1. Actualitzar nom client")
        print("2. Actualitzar informació del tiquet")
        print("3. Sortir")
        try:
            opcio_actu=int(input("Escolleix una opcio (1-3): "))
        except ValueError:
            print("La opcio ha de ser un numero del 1 al 3")
        
        match opcio_actu:
            case 1:
                demanar_nom_client()
            case 2:                                #trucada als metodes
                afegir_productes()
            case 3:
                print("DADES ACTUALITZADES")
                print("Sortint del menú d'actualització...")
            case _:
                print("Opcio invalida")


if __name__ == "__main__":
    try:
        opcio=0
        while opcio!=4:
            print("===== GESTIÓ COMANDES RESTAURANT =====\n")
            print("1.Crear nova comanda")
            print("2.Actualitzar comanda anterior")     #menu principal
            print("3.Visualitzar últim tiquet")
            print("4.Sortir")
            opcio=int(input("Escolleix una opció (1-4): "))
            match opcio:
                case 1:
                    crear_nova_comanda()
                    generar_tiquet()
                case 2:
                    if len(ticket)<1:
                        print("No hi ha cap comanda creada")
                    else:                                                  #crida de metodes amb condicio per si no hi ha cap tiquet creat anteriorment
                        actualitzar_ticket()
                case 3:
                    if len(ticket)<1:
                        print("No hi ha cap comanda creada")
                    else:
                        generar_tiquet()
                case 4:
                    print("Sortint del sistema...")

    except ValueError:
        print("Error de formato")


