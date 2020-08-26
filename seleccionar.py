from tercero import tercero
from cuarto import cuarto


def seleccionar(union, cadena2):
    cadena = [0] * len(cadena2)
    contador = 0
    tam = len(cadena2)

    for palabra in cadena2:
        cadena[contador] = palabra.lower()
        contador += 1

    if tam == 2:
        primero(union, cadena)
    elif tam == 3:
        segundo(union, cadena)
    elif tam == 4:
        tercero(union, cadena)
    elif tam == 5:
        cuarto(union, cadena)
    else:
        print("Comando Invalido")


def primero(union, cadena):
    if cadena[1] == "*":
        for archivo in union:
            print(archivo.get('nombre'))
            print(archivo.get('edad'))
            print(archivo.get('activo'))
            print(archivo.get('promedio'))
            print("")
    elif cadena[1] == "nombre":
        for archivo in union:
            print(archivo.get('nombre'))
            print("")
    elif cadena[1] == "edad":
        for archivo in union:
            print(archivo.get('edad'))
            print("")
    elif cadena[1] == "activo":
        for archivo in union:
            print(archivo.get('activo'))
            print("")
    elif cadena[1] == "promedio":
        for archivo in union:
            print(archivo.get('promedio'))
            print("")
    else:
        print("Comando Invalido")


def segundo(union, cadena):
    if cadena[1] == "nombre":
        if cadena[2] == "edad":
            for archivo in union:
                print(archivo.get('nombre'))
                print(archivo.get('edad'))
                print("")
        elif cadena[2] == "promedio":
            for archivo in union:
                print(archivo.get('nombre'))
                print(archivo.get('promedio'))
                print("")
        elif cadena[2] == "activo":
            for archivo in union:
                print(archivo.get('nombre'))
                print(archivo.get('activo'))
                print("")
        else:
            print("Comando Invalido")

    elif cadena[1] == "edad":
        if cadena[2] == "nombre":
            for archivo in union:
                print(archivo.get('nombre'))
                print(archivo.get('edad'))
                print("")
        elif cadena[2] == "promedio":
            for archivo in union:
                print(archivo.get('edad'))
                print(archivo.get('promedio'))
                print("")
        elif cadena[2] == "activo":
            for archivo in union:
                print(archivo.get('edad'))
                print(archivo.get('activo'))
                print("")
        else:
            print("Comando Invalido")

    elif cadena[1] == "promedio":
        if cadena[2] == "edad":
            for archivo in union:
                print(archivo.get('edad'))
                print(archivo.get('promedio'))
                print("")
        elif cadena[2] == "nombre":
            for archivo in union:
                print(archivo.get('nombre'))
                print(archivo.get('promedio'))
                print("")
        elif cadena[2] == "activo":
            for archivo in union:
                print(archivo.get('activo'))
                print(archivo.get('promedio'))
                print("")
        else:
            print("Comando Invalido")

    elif cadena[1] == "activo":
        print(cadena[1])
        if cadena[2] == "edad":
            for archivo in union:
                print(archivo.get('edad'))
                print(archivo.get('activo'))
                print("")
        elif cadena[2] == "promedio":
            for archivo in union:
                print(archivo.get('activo'))
                print(archivo.get('promedio'))
                print("")
        elif cadena[2] == "nombre":
            for archivo in union:
                print(archivo.get('nombre'))
                print(archivo.get('activo'))
                print("")
        else:
            print("Comando Invalido")
    else:
        print("Comando Invalido")
