import re
import cargar
from cargar import cargar
from suma import sumas
from maximo import maximo
from minimo import minimo


def entrada():
    cadena = input("Introducir Comando: ")
    cadena1 = re.split('[ ,]', cadena)
    comando = cadena1[0].lower()

    if comando == "cargar":
        carga = cargar(cadena1)
        print("-------------------------------------------")
        print("")
        menu(carga)

    elif comando == "seleccionar":
        print("No hay archivos cargados")
        entrada()

    elif comando == "maximo":
        print("No hay archivos cargados")
        entrada()

    elif comando == "minimo":
        print("No hay archivos cargados")
        entrada()

    elif comando == "suma":
        print("No hay archivos cargados")
        entrada()

    elif comando == "cuenta":
        print("No hay archivos cargados")
        entrada()

    elif comando == "reportar":
        print("No hay archivos cargados")
        entrada()

    else:
        print("Comando invalido")
        entrada()


def menu(union):
    if len(union) != 0:
        cadena = input("Introducir Comando: ")
        cadena1 = re.split('[ ,]', cadena.lower())
        comando = cadena1[0]

        if comando == "cargar":
            print("-------------------------------------------")
            carga = cargar(cadena1)
            print("-------------------------------------------")
            menu(carga)

        elif comando == "seleccionar":
            print("-------------------------------------------")
            print("Comando seleccionar")
            print("-------------------------------------------")
            menu(union)

        elif comando == "maximo":
            print("-------------------------------------------")
            mayor = maximo(union, cadena1)
            print(mayor)
            print("-------------------------------------------")
            menu(union)

        elif comando == "minimo":
            print("-------------------------------------------")
            mayor = minimo(union, cadena1)
            print(mayor)
            print("-------------------------------------------")
            menu(union)

        elif comando == "suma":
            print("-------------------------------------------")
            total = sumas(union, cadena1)
            print(total)
            print("-------------------------------------------")
            menu(union)

        elif comando == "cuenta":
            print("-------------------------------------------")
            print(union)
            print(len(union))
            print("-------------------------------------------")
            menu(union)

        elif comando == "reportar":
            print("-------------------------------------------")
            print("Comando reportar")
            print("-------------------------------------------")
            menu(union)

        else:
            print("Comando invalido")
            menu(union)
    else:
        print("No hay archivos cargados")
        entrada()


entrada()
