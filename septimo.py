def donde4(union, cadena):
    if cadena[1] == "nombre":
        if cadena[3] == "edad":
            if cadena[5] == "activo":
                if cadena[7] == "promedio" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "promedio":
                if cadena[7] == "activo" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")

        elif cadena [3] == "activo":
            if cadena[5] == "edad":
                if cadena[7] == "promedio" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "promedio":
                if cadena[7] == "edad" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        elif cadena[3] == "promedio":
            if cadena[5] == "activo":
                if cadena[7] == "edad" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "edad":
                if cadena[7] == "activo" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")

    elif cadena[1] == "edad":
        if cadena[3] == "nombre":
            if cadena[5] == "activo":
                if cadena[7] == "promedio" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "promedio":
                if cadena[7] == "activo" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        elif cadena [3] == "activo":
            if cadena[5] == "nombre":
                if cadena[7] == "promedio" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "promedio":
                if cadena[7] == "nombre" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        elif cadena[3] == "promedio":
            if cadena[5] == "activo":
                if cadena[7] == "nombre" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "nombre":
                if cadena[7] == "activo" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")

    elif cadena[1] == "activo":
        if cadena[3] == "edad":
            if cadena[5] == "nombre":
                if cadena[7] == "promedio" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "promedio":
                if cadena[7] == "nombre" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        elif cadena [3] == "nombre":
            if cadena[5] == "edad":
                if cadena[7] == "promedio" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "promedio":
                if cadena[7] == "edad" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        elif cadena[3] == "promedio":
            if cadena[5] == "edad":
                if cadena[7] == "nombre" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "nombre":
                if cadena[7] == "edad" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")

    elif cadena[1] == "promedio":
        if cadena[3] == "edad":
            if cadena[5] == "activo":
                if cadena[7] == "nombre" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "nombre":
                if cadena[7] == "activo" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        elif cadena [3] == "activo":
            if cadena[5] == "nombre":
                if cadena[7] == "edad" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "edad":
                if cadena[7] == "nombre" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        elif cadena[3] == "nombre":
            if cadena[5] == "activo":
                if cadena[7] == "edad" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            elif cadena[5] == "edad":
                if cadena[7] == "activo" and cadena[8] == "donde" and cadena[9] == "nombre":
                    buscar(union, cadena)
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")
    else:
        print("Comando Invalido")

def buscar(union, cadena):
    for archivo in union:
        if archivo.get('nombre') == cadena[12]:
            print(archivo.get('nombre'))
            print(archivo.get('edad'))
            print(archivo.get('activo'))
            print(archivo.get('promedio'))
            print("")
