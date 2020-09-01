def donde3(union, cadena):
    print("")
    if cadena[1] == "nombre":
        if cadena[3] == "edad":
            if cadena[5] == "activo":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "promedio" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")

            elif cadena[5] == "promedio":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[5] == "edad":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "promedio" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "edad" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "promedio":
            if cadena[5] == "edad":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "edad" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")

    elif cadena[1] == "edad":
        if cadena[3] == "nombre":
            if cadena[5] == "activo":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "promedio" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[5] == "nombre":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "promedio" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "nombre" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "promedio":
            if cadena[5] == "nombre":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "nombre" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")
    elif cadena[1] == "activo":
        if cadena[3] == "edad":
            if cadena[5] == "nombre":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "promedio" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "nombre" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "nombre":
            if cadena[5] == "edad":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "activo" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "edad" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "promedio":
            if cadena[5] == "edad":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "nombre" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "edad" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")

    elif cadena[1] == "promedio":
        if cadena[3] == "edad":
            if cadena[5] == "nombre":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "nombre" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "activo":
            if cadena[5] == "nombre":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "edad" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "edad":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "nombre" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "nombre":
            if cadena[5] == "edad":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo":
                if cadena[6] == "donde" and cadena[7] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[10]:
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "edad" and cadena[8] == "donde":
                    buscar(union, cadena)
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")
    else:
        print("Comando Invalido")

def buscar(union, cadena):
    if cadena[9] == "edad":
        for archivo in union:
            if archivo.get('edad') == int(cadena[11]):
                print(archivo.get('nombre'))
                print(archivo.get('edad'))
                print(archivo.get('activo'))
                print(archivo.get('promedio'))
                print("")
    elif cadena[9] == "activo":
        for archivo in union:
            if archivo.get('activo') == bool(cadena[11]):
                print(archivo.get('nombre'))
                print(archivo.get('edad'))
                print(archivo.get('activo'))
                print(archivo.get('promedio'))
                print("")
    elif str(cadena[9]) == "promedio":
        for archivo in union:
            if archivo.get('promedio') == float(cadena[11]):
                print(archivo.get('nombre'))
                print(archivo.get('edad'))
                print(archivo.get('activo'))
                print(archivo.get('promedio'))
                print("")
    else:
        print("Comando Invalido")