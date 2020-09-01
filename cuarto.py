def cuarto(union, cadena):
    if cadena[1] == "*":
        if cadena[2] == "donde":
            if cadena[3] == "nombre":
                for archivo in union:
                    if archivo.get('nombre') == cadena[6]:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
            else:
                print("Comando Invalido")
        else:
            print("Comando Invalido")
    elif cadena[1] == "nombre":
        if cadena[2] == "donde":
            if cadena[3] == "nombre":
                for archivo in union:
                    if archivo.get('nombre') == cadena[6]:
                        print(archivo.get('nombre'))
                        print("")
            else:
                print("Comando Invalido")

        elif cadena[3] == "edad":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[7] == "activo":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "activo":
                if cadena[7] == "promedio":
                    for archivo in union:
                        print(archivo.get('nombre'))
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

        elif cadena[3] == "promedio":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "edad":
                if cadena[7] == "activo":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "activo":
                if cadena[7] == "edad":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")
        elif cadena[3] == "activo":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[7] == "edad":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "edad":
                if cadena[7] == "promedio":
                    for archivo in union:
                        print(archivo.get('nombre'))
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

    elif cadena[1] == "edad":
        if cadena[2] == "donde":
            if cadena[3] == "nombre":
                for archivo in union:
                    if archivo.get('nombre') == cadena[6]:
                        print(archivo.get('edad'))
                        print("")
            else:
                print("Comando Invalido")
        elif cadena[3] == "nombre":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('edad'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[7] == "activo":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "activo":
                if cadena[7] == "promedio":
                    for archivo in union:
                        print(archivo.get('nombre'))
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
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre":
                if cadena[7] == "activo":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "activo":
                if cadena[7] == "nombre":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[7] == "nombre":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "nombre":
                if cadena[7] == "promedio":
                    for archivo in union:
                        print(archivo.get('nombre'))
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

    elif cadena[1] == "promedio":
        if cadena[2] == "donde":
            if cadena[3] == "nombre":
                for archivo in union:
                    if archivo.get('nombre') == cadena[6]:
                        print(archivo.get('promedio'))
                        print("")
            else:
                print("Comando Invalido")
        elif cadena[3] == "edad":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre":
                if cadena[7] == "activo":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "activo":
                if cadena[7] == "nombre":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "nombre":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "edad":
                if cadena[7] == "activo":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "activo":
                if cadena[7] == "edad":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('promedio'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('promedio'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('promedio'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre":
                if cadena[7] == "edad":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "edad":
                if cadena[7] == "nombre":
                    for archivo in union:
                        print(archivo.get('nombre'))
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
        if cadena[2] == "donde":
            if cadena[3] == "nombre":
                for archivo in union:
                    if archivo.get('nombre') == cadena[6]:
                        print(archivo.get('activo'))
                        print("")
            else:
                print("Comando Invalido")
        elif cadena[3] == "edad":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('edad'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[7] == "nombre":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "nombre":
                if cadena[7] == "promedio":
                    for archivo in union:
                        print(archivo.get('nombre'))
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
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('activo'))
                            print(archivo.get('promedio'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "nombre":
                if cadena[7] == "edad":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "edad":
                if cadena[7] == "nombre":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")
            else:
                print("Comando Invalido")

        elif cadena[3] == "nombre":
            if cadena[4] == "donde":
                if cadena[5] == "edad":
                    for archivo in union:
                        if archivo.get('edad') == int(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print("")
                elif cadena[5] == "activo":
                    for archivo in union:
                        if archivo.get('activo') == bool(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print("")
                elif str(cadena[5]) == "promedio":
                    for archivo in union:
                        if archivo.get('promedio') == float(cadena[7]):
                            print(archivo.get('nombre'))
                            print(archivo.get('activo'))
                            print("")
                else:
                    print("Comando Invalido")
            elif cadena[5] == "promedio":
                if cadena[7] == "edad":
                    for archivo in union:
                        print(archivo.get('nombre'))
                        print(archivo.get('edad'))
                        print(archivo.get('activo'))
                        print(archivo.get('promedio'))
                        print("")
                else:
                    print("Comando Invalido")

            elif cadena[5] == "edad":
                if cadena[7] == "promedio":
                    for archivo in union:
                        print(archivo.get('nombre'))
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
