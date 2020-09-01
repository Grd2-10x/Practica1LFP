def tercero(union, cadena):
    if cadena[1] == "*" and cadena[2] == "donde":
        if cadena[3] == "edad":
            for archivo in union:
                if archivo.get('edad') == int(cadena[5]):
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
        elif cadena[3] == "activo":
            for archivo in union:
                if archivo.get('activo') == bool(cadena[5]):
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
        elif str(cadena[3]) == "promedio":
            for archivo in union:
                if archivo.get('promedio') == float(cadena[5]):
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
    elif cadena[1] == "nombre":
        if cadena[3] == "edad":
            if cadena[5] == "promedio":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "activo":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[3] == "promedio":
            if cadena[5] == "edad":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "activo":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[5] == "promedio":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "edad":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[2] == "donde":
            if cadena[3] == "edad":
                for archivo in union:
                    if archivo.get('edad') == int(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
            elif cadena[3] == "activo":
                for archivo in union:
                    if archivo.get('activo') == bool(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
            elif str(cadena[3]) == "promedio":
                for archivo in union:
                    if archivo.get('promedio') == float(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
        else:
            print("Comando Invalido")

    elif cadena[1] == "edad":
        if cadena[3] == "nombre":
            if cadena[5] == "promedio":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "activo":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[3] == "promedio":
            if cadena[5] == "nombre":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "activo":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[5] == "promedio":
                for archivo in union:
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "nombre":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[2] == "donde":
            if cadena[3] == "edad":
                for archivo in union:
                    if archivo.get('edad') == int(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
            elif cadena[3] == "activo":
                for archivo in union:
                    if archivo.get('activo') == bool(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
            elif str(cadena[3]) == "promedio":
                for archivo in union:
                    if archivo.get('promedio') == float(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
        else:
            print("Comando Invalido")

    elif cadena[1] == "promedio":
        if cadena[3] == "edad":
            if cadena[5] == "nombre":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "activo":
                for archivo in union:
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[3] == "nombre":
            if cadena[5] == "edad":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "activo":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[3] == "activo":
            if cadena[5] == "nombre":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "edad":
                for archivo in union:
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[2] == "donde":
            if cadena[3] == "edad":
                for archivo in union:
                    if archivo.get('edad') == int(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
            elif cadena[3] == "activo":
                for archivo in union:
                    if archivo.get('activo') == bool(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
            elif str(cadena[3]) == "promedio":
                for archivo in union:
                    if archivo.get('promedio') == float(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
        else:
            print("Comando Invalido")

    elif cadena[1] == "activo":
        if cadena[3] == "edad":
            if cadena[5] == "promedio":
                for archivo in union:
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "nombre":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[3] == "promedio":
            if cadena[5] == "nombre":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "edad":
                for archivo in union:
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[3] == "nombre":
            if cadena[5] == "promedio":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('activo'))
                    print(archivo.get('promedio'))
                    print("")
            elif cadena[5] == "edad":
                for archivo in union:
                    print(archivo.get('nombre'))
                    print(archivo.get('edad'))
                    print(archivo.get('activo'))
                    print("")
            else:
                print("Comando Invalido")

        elif cadena[2] == "donde":
            if cadena[3] == "edad":
                for archivo in union:
                    if archivo.get('edad') == int(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
            elif cadena[3] == "activo":
                for archivo in union:
                    if archivo.get('activo') == bool(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
            elif str(cadena[3]) == "promedio":
                for archivo in union:
                    if archivo.get('promedio') == float(cadena[5]):
                        print(archivo.get('nombre'))
                        print("")
        else:
            print("Comando Invalido")
    else:
        print("Comando Invalido")
