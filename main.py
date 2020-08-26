import re
import cargar
from cargar import cargar
from suma import sumas
from maximo import maximo
from minimo import minimo
from seleccionar import seleccionar
from reportar import reporte


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

    elif comando == "salir":
        print("Hasta la proxima")

    else:
        print("Comando invalido")
        entrada()


def menu(union):
    if len(union) != 0:
        cadena = input("Introducir Comando: ")
        cadena1 = re.split('[ ,"]', cadena)
        comando = cadena1[0].lower()

        if comando == "cargar":
            print("-------------------------------------------")
            carga = cargar(cadena1)
            print("-------------------------------------------")
            menu(carga)

        elif comando == "seleccionar":
            print("-------------------------------------------")
            seleccionar(union, cadena1)
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
            reporte(union, cadena1)
            print("-------------------------------------------")
            menu(union)

        elif comando == "salir":
            print("Hasta la proxima")

        else:
            print("Comando invalido")
            menu(union)
    else:
        print("No hay archivos cargados")
        entrada()


print("-------------------------------------------")
print("              ---Comandos---               ")
print("1) cargar")
print("2) seleccionar")
print("3) maximo")
print("4) minimo")
print("5) suma")
print("6) cuenta")
print("7) reportar")
print("8) salir")
print("-------------------------------------------")
print("")
entrada()
