import time
import random

def door_control_auto(door_open):
    detect = random.randint(0, 1)

    if detect == 1:
        door_open = True
        print("Face ID: Persona detectada: Puerta ABIERTA.")
    else:
        door_open = False
        print("Face ID: Nadie detectado: Puerta CERRADA.")

    return door_open

def fire_alarm_control_auto(fire_alarm_on, co2_limit, current_co2):
    if current_co2 >= co2_limit:
        fire_alarm_on = True
        print("ALARMA ACTIVADA: CO2 alto.")
    else:
        fire_alarm_on = False
        print("Alarma apagada: CO2 normal.")
    return fire_alarm_on

def sprinkler_control_auto(sprinkler_on, asp_hora, asp_minut, hora, minut):
    if hora == asp_hora and minut == asp_minut:
        sprinkler_on = True
        print("Aspersor ACTIVADO a la hora programada.")
    else:
        sprinkler_on = False
    return sprinkler_on

def extinguisher_control_auto(fire_alarm_on, extinguisher_on):
    if fire_alarm_on:
        extinguisher_on = True
        print("Extintor ACTIVADO automáticamente por fuego.")
    else:
        extinguisher_on = False
    return extinguisher_on

def reloj(hora, minut):
    minut += 1
    if minut >= 60:
        minut = 0
        hora += 1
    if hora >= 24:
        hora = 0

    if hora < 10:
        hora_s = "0" + str(hora)
    else:
        hora_s = str(hora)

    if minut < 10:
        minut_s = "0" + str(minut)
    else:
        minut_s = str(minut)

    return hora, minut, hora_s + ":" + minut_s

def config_menu():
    print("\nCONFIGURACIÓN DEL SISTEMA")

    co2_limit = int(input("Límite de CO2 para activar la alarma (ppm): "))

    print("\nPROGRAMAR ASPERSOR (Formato 24h)")
    asp_hora = int(input("Hora (0-23): "))
    asp_minut = int(input("Minuto (0-59): "))

    print("\nConfiguración guardada.\n")

    return co2_limit, asp_hora, asp_minut

def simulation(co2_limit, asp_hora, asp_minut):
    hora = 0
    minut = 0

    door_open = False
    fire_alarm_on = False
    sprinkler_on = False
    extinguisher_on = False

    print("\n--- SIMULACIÓN AUTOMÁTICA INICIADA ---")
    print("Pulsa CTRL+C para detener.\n")

    try:
        while True:
            hora, minut, hora_str = reloj(hora, minut)
            print("\nHora:", hora_str)

            current_co2 = random.randint(300, 2000)
            print("CO2 detectado:", current_co2, "ppm")

            door_open = door_control_auto(door_open)
            fire_alarm_on = fire_alarm_control_auto(fire_alarm_on, co2_limit, current_co2)
            sprinkler_on = sprinkler_control_auto(sprinkler_on, asp_hora, asp_minut, hora, minut)
            extinguisher_on = extinguisher_control_auto(fire_alarm_on, extinguisher_on)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nSimulación detenida.")

def main_menu():
    co2_limit = 900
    asp_hora = 0
    asp_minut = 0

    while True:
        print("\nMENU PRINCIPAL")
        print("1. Configurar sistema")
        print("2. Iniciar simulación")
        print("3. Salir")

        try:
            option = int(input("Elige una opción: "))

            if option == 1:
                co2_limit, asp_hora, asp_minut = config_menu()

            elif option == 2:
                simulation(co2_limit, asp_hora, asp_minut)

            elif option == 3:
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Debes introducir un número.")

if __name__ == "__main__":
    main_menu()
