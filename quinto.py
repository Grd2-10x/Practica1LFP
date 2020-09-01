def donde2(union, cadena):
    if cadena[1] == "nombre":
        if cadena[3] == "edad":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "edad" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "promedio":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('nombre'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "edad" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("comando Invalido")
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")

    elif cadena[1] == "edad":
        if cadena[3] == "nombre":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "promedio":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")
    elif cadena[1] == "activo":
        if cadena[3] == "nombre":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "edad" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "edad":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "promedio":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comandi Invalido")
            elif cadena[5] == "edad" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")

    elif cadena[1] == "promedio":
        if cadena[3] == "nombre":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('nombre'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "edad" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "edad" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "edad":
            if cadena[4] == "donde":
                if cadena[5] == "nombre":
                    for archivo in union:
                        if archivo.get('nombre') == cadena[8]:
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "activo" and cadena[6] == "donde":
                if cadena[7] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[7] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[9]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")
    else:
        print("Comando Invalido")
