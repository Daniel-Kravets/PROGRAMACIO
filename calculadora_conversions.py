def comprovar_enter(text):
    valor=None
    while valor is None:
        try:
            valor=int(input(text))
        except ValueError:
            print("Error de formato")
        except Exception as e:
            print(e)
            print(type(e))
    return valor

def comprovar_string(text):
    return input(text)

def detectar_base():
    prefixos=["0b","0o","0x"]
    base=""
    valor=0
    while valor not in prefixos:
        print("Introdueix un prefix per pasar aquell numero a les altres bases:")
        print(prefixos)
        print("Introdueix: 'decimal' si vols pasar un nombre decimal a altres bases")
        valor=input("Introdueix prefix o 'decimal': ")
        if valor not in prefixos and valor!="decimal":
            print("Cal introduir el valor seguint les instruccions")
        if valor=="decimal":
            print("Has seleccionat un numero decimal")
            base="d"
            break
    if valor==prefixos[0]:
        print("Has seleccionat un numero binari")
        base="b"
    elif valor==prefixos[1]:
        print("Has seleccionat un numero octal")
        base="o"
    elif valor==prefixos[2]:
        print("Has seleccionat un numero hexadecimal")
        base="h"
    return valor,base

def binari_a_decimal(num_binari):
    """Converteix un número binari (string) a decimal (int) manualment, amb validació."""
    decimal = 0
    num_binari = num_binari.lstrip('0b') # Elimina el prefix si l'usuari l'ha inclòs
    
    for digit in num_binari:
        if digit not in '01':
            raise ValueError(f"El dígit '{digit}' no és vàlid per a un número binari.")
        decimal = decimal * 2 + int(digit)
    return decimal

def octal_a_decimal(num_octal):
    """Converteix un número octal (string) a decimal (int) manualment, amb validació."""
    decimal = 0
    num_octal = num_octal.lstrip('0o') # Elimina el prefix si l'usuari l'ha inclòs
    
    for digit in num_octal:
        if digit not in '01234567':
            raise ValueError(f"El dígit '{digit}' no és vàlid per a un número octal.")
        decimal = decimal * 8 + int(digit)
    return decimal

def hexadecimal_a_decimal(num_hexadecimal):
    """Converteix un número hexadecimal (string) a decimal (int) manualment, amb validació."""
    decimal = 0
    num_hexadecimal = num_hexadecimal.lstrip('0x').upper() # Elimina el prefix i posa en majúscules
    
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    for digit in num_hexadecimal:
        if digit not in hex_map:
            raise ValueError(f"El dígit '{digit}' no és vàlid per a un número hexadecimal.")
        decimal = decimal * 16 + hex_map[digit]
    return decimal

def decimal_a_binari(num_decimal):
    """Converteix un número decimal (int) a binari (string) manualment."""
    if num_decimal == 0:
        return "0b0"
    
    binari = ""
    temp_decimal = num_decimal
    while temp_decimal > 0:
        binari = str(temp_decimal % 2) + binari
        temp_decimal //= 2
    return "0b" + binari

def decimal_a_octal(num_decimal):
    """Converteix un número decimal (int) a octal (string) manualment."""
    if num_decimal == 0:
        return "0o0"
    
    octal = ""
    temp_decimal = num_decimal
    while temp_decimal > 0:
        octal = str(temp_decimal % 8) + octal
        temp_decimal //= 8
    return "0o" + octal

def decimal_a_hexadecimal(num_decimal):
    """Converteix un número decimal (int) a hexadecimal (string) manualment."""
    if num_decimal == 0:
        return "0x0"
    
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = ""
    temp_decimal = num_decimal
    while temp_decimal > 0:
        residu = temp_decimal % 16
        if residu < 10:
            hexadecimal = str(residu) + hexadecimal
        else:
            hexadecimal = hex_map[residu] + hexadecimal
        temp_decimal //= 16
    return "0x" + hexadecimal



opcio=0
while opcio!=2:
    print("--- BENVINGUT A LA CALCULADORA DE CONVERSIONS! ---\n")
    print("1. Convertir a una base")
    print("2. Sortir del programa")
    opcio=int(comprovar_enter("Introdueix una opcio (1-2): "))
    match opcio:
        case 1:
            valor,base=detectar_base()
            if base=="b" or base =="o" or base=="h":
                print(f"Conversió del numero {valor} a decimal:")
                try:
                    if base=="b":
                        num_a_convertir = comprovar_string(f"Introdueix el número binari (sense prefix {valor}): ")
                        decimal = binari_a_decimal(num_a_convertir)
                        print(f"El número binari {num_a_convertir} convertit a decimal és: {decimal}")
                        break
                    elif base=="o":
                        num_a_convertir = comprovar_string(f"Introdueix el número octal (sense prefix {valor}): ")
                        decimal = octal_a_decimal(num_a_convertir)
                        print(f"El número octal {num_a_convertir} convertit a decimal és: {decimal}")
                        break
                    elif base=="h":
                        num_a_convertir = comprovar_string(f"Introdueix el número hexadecimal (sense prefix {valor}): ")
                        decimal = hexadecimal_a_decimal(num_a_convertir)
                        print(f"El número hexadecimal {num_a_convertir} convertit a decimal és: {decimal}")
                        break
                except ValueError as e:
                    print(f"Error de validació: {e}")
                except Exception as e:
                    print(f"Error inesperat: {e}")
            elif base=="d":
                # Conversió de Decimal a Binari/Octal/Hexadecimal
                num_decimal = comprovar_enter("Introdueix el número decimal a convertir: ")
                
                if num_decimal is not None:
                    print("\n--- Resultats de la Conversió ---")
                    
                    # Conversió a Binari
                    binari = decimal_a_binari(num_decimal)
                    print(f"Decimal {num_decimal} a Binari: {binari}")
                    
                    # Conversió a Octal
                    octal = decimal_a_octal(num_decimal)
                    print(f"Decimal {num_decimal} a Octal: {octal}")
                    
                    # Conversió a Hexadecimal
                    hexadecimal = decimal_a_hexadecimal(num_decimal)
                    print(f"Decimal {num_decimal} a Hexadecimal: {hexadecimal}")
                    print("--------------------------------\n")
        case 2:
            print("Gràcies per utilitzar la calculadora de conversions. Adéu!")
        case _:
            print("Opció no vàlida. Si us plau, introdueix 1 o 2.")