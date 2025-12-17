import math
import datetime
def mostrarmenu():
    print("      MENÚ PRINCIPAL ")
    print("1. Introduir dades")
    print("2. Modificar dades")
    print("3. Visualitzar dades")
    print("4. Sortir")


nom = ""
edat = 0
pes = 0.0
alçada = 0.0
opcio = "0"

while opcio != "4":
    mostrarmenu()
    opcio=input("Escolleix opcio (1-4): ")


    match opcio:
        case "1":
            nom=input("Introdueix nom complert: ").capitalize()
            if len(nom)<1:
                print("Error: El nom no pot quedar buit.")
               
            try:
                edat=float(input("Introdueix la teva edat: "))
                edat=int(edat)
                if edat>=120 or edat<=0:
                    print("Error: L'edat ha de ser un enter positiu ≤ 120 i més gran que 0.")
                   
            except ValueError:
                 print("Error: Format numèric invàlid per a l'edat.")
                 
            try:
                pes=input("Introdueix el teu pes en kg: ")
                pes=pes.replace(",", ".")
                pes=float(pes)
                if pes>=400:
                    print("Error: El pes ha de ser un decimal positiu raonable.")
                   
            except ValueError:
                 print("Error: Format numèric invàlid per el pes.")
                 
            try:
                alçada=input("Introdueix la teva alçada en metres: ")
                alçada=alçada.replace(",", ".")
                alçada=float(alçada)
                if alçada<0.5 or alçada>2.5:
                    print("Error: L'alçada ha de ser un decimal positiu entre 0.5 i 2.5 metres.")
                   
            except ValueError:
                 print("Error: Format numèric invàlid per la alçada.")
                 
        case "2":
            print("\nQuina dada vols modificar?")
            print("1. Nom")
            print("2. Edat")
            print("3. Pes")
            print("4. Alçada")
            opcio_mod = input("Tria una opcio (1-4): ")


            match opcio_mod:
                case "1":
                    nou_nom=input("Introdueix el nou nom complet: ")
                    if len(nou_nom)<1:
                        print("Error: El nom no pot quedar buit")
               
                    else:
                        nom=nou_nom
                        print("Nom modificat correctament.")
               


                case "2":
                    try:
                        nova_edat=int(float(input("Introdueix la nova edat: ")))
                        if nova_edat<=0 or nova_edat>120:
                            print("Error: L'edat ha de ser un enter positiu ≤ 120.")
                        else:
                            edat=nova_edat
                            print("Edat modificada correctament.")
                    except ValueError:
                        print("Error: Format numèric invàlid per a l'edat.")


                case "3":
                    try:
                        nou_pes=input("Introdueix el nou pes: ").replace(",", ".")
                        nou_pes=float(nou_pes)
                        if nou_pes<=0 or nou_pes>400:
                            print("Error: El pes ha de ser un decimal positiu raonable (≤ 400).")
                        else:
                            pes=nou_pes
                            print("Pes modificat correctament.")
                    except ValueError:
                        print("Error: Format numèric invàlid per al pes.")


                case "4":
                    try:
                        nova_alçada=input("Introdueix la nova alçada (m): ").replace(",", ".")
                        nova_alçada=float(nova_alçada)
                        if nova_alçada<0.5 or nova_alçada>2.5:
                            print("Error: L'alçada ha de ser entre 0.5 i 2.5 metres.")
                        else:
                            alçada=nova_alçada
                            print("Alçada modificada correctament.")
                    except ValueError:
                        print("Error: Format numèric invàlid per l'alçada.")
        case "3":
            print("\nVisualitzar dades:\n")
            print(f"Nom:{nom}")
            print(f"Edat:{edat}")
            print(f"Pes:{pes}")
            print(f"Alçada:{alçada}")
            IMC=float(pes)/float(alçada)**2
            print(f"IMC: {IMC}")
            if IMC<18.5:
                print("\nCondició:Pes baix")
            elif IMC>=18.5 and IMC<=24.9:
                print("\nCondició:Pes normal")
            elif IMC>=25 and IMC<=29.9:
                print("\nCondició:Sobrepès")
            elif IMC<0:
                print("\nError")
            else:
                print("\nCondició:Obesitat")
            freq_max=int(220-edat)
            print(f"\nfrequenica màxima:{freq_max}")
            aigua_ml = pes * 35
            aigua_l = float(aigua_ml) / 1000
            print(f"Aigua diària recomanada: {aigua_l:.2f} litres")
            any_actual = datetime.date.today().year
            any_naixement = any_actual - edat
            print(f"Any de naixement aproximat: {any_naixement}")

        case "4":
            print("Sortir")
