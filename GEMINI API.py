from google import genai
def comprovar_numero(texto):
    while True:
        try:
            return int(input(f"{texto}: "))
        except ValueError:
            print("Error de format, introdueix un numero")


def peticio(quantitat, tipus, tematica):
    # Inicializa el cliente
    client = genai.Client()
    # Genera contenido
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=f"Genera exactament {quantitat} valors de tipus {tipus} amb la temàtica:{tematica} amb el format de sortida: una sola linea, valors en minuscula,separades per comes,sense espais,sense text adicional" #aqui va un prompt
    )

    respuesta = response.text
    lista = str(respuesta).split(",")
    sets.append(lista)


if __name__ == "__main__":
    opcio=0
    noms_sets=[]
    sets=[]
    llista_tipus=["text","numeric"]
    while opcio!=4:
        print("---- BENVINGUT AL GENERADOR DE SETS ----")
        print("OPCIONS:\n")
        print("1. Generar un nou set de dades")
        print("2. Visualitzar un o tots els sets de dades")
        print("3. Esborrar un o tots els sets de dades")
        print("4. Sortir")
        opcio=comprovar_numero("Introdueix opcio(1-4): ")
        match opcio:
            case 1:
                    quantitat=0
                    tematica=""
                    tipus=""
                    nom_set=input("Introdueix el nom del set: ")
                    noms_sets.append(nom_set)
                    quantitat=comprovar_numero("Introdueix nombre de dades: ")
                    while tipus not in llista_tipus:
                        tipus=input("Introdueix tipus (text o numeric): ")
                        if tipus not in llista_tipus:
                            print("Cal intoduir tot en minuscules i sense accents")
                    tematica=input("Tematica: ")
                    peticio(quantitat, tipus, tematica)

            case 2:
                opcio2=0
                while opcio2!=3:
                    print("1. Veure un set pel nom")
                    print("2. Veure tots els sets")
                    print("3. Sortir")
                    opcio2=comprovar_numero("Introdueix opcio(1-3): ")
                    match opcio2:
                        case 1:
                            nom = None
                            while nom not in noms_sets:
                                nom=input("Introdueix el nom del set que vols visualitzar: ")
                                if nom not in noms_sets:
                                    print("No existeix aquest set")
                            valor_index=noms_sets.index(nom)
                            print(f"Set de {nom_set}")
                            for v in sets[valor_index]:
                                print(f" -{v}")
                        case 2:
                            for i in range(len(noms_sets)):
                                print(f"Set de {noms_sets[i]}")
                                for v in sets[i]:
                                    print(f" -{v}")
                        case 3:
                            print("Sortint...")
                        case _:
                            print("Cal introduir un numero del 1 al 3")

            case 3:
                opcio=3
                while opcio3!=3:
                    print("1. Esborrar un set pel nom")
                    print("2. Esborrar tots els sets")
                    print("3. Sortir")
                    opcio3=comprovar_numero("Introdueix opcio(1-3): ")
                    match opcio3:
                        case 1:
                            nom = None
                            while nom not in noms_sets:
                                nom=input("Introdueix el nom del set que vols eliminar: ")
                                if nom not in noms_sets:
                                    print("No existeix aquest set")
                            valor_index=noms_sets.index(nom)
                            noms_sets.pop(valor_index)
                            sets.pop(valor_index)
                                
                        case 2:
                            noms_sets=[]
                            sets=[]
                        case 3:
                            print("Sortint...")
                        case _:
                            print("Cal introduir un numero del 1 al 3")
            
            case 4:
                print("Sortint...")
            case _:
                print("Cal introduir numero del 1 al 4")