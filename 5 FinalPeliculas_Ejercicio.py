import json

usuarios = []
peliculas = []

def menu():
    print("\nMenú:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("\nSeleccione una opcion: ")

    if opcion =="1":
        registrar_usuario()
        return menu()
    elif opcion == "2":
        iniciar_sesion()
        return
    elif opcion == "3":
        print("Saliendo del programa.")
        return
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return menu()

def registrar_usuario():
    nombre = input("Nombre de usuario: ").lower()
    clave = input("Ingrese su contraseña: ").lower()

    usuario = {
            "nombre": nombre,
            "clave": clave
    }

    usuarios.append(usuario)

    with open ("usuarios.json","w") as archivo:
            json.dump(usuarios, archivo)
            print("Usuario registrado con exito.")

def iniciar_sesion():
    user = input("\nIngrese Usuario: ").lower()
    pas = input("Ingrese Contraseña: ").lower()

    for usuario in usuarios:
        if usuario["nombre"] == user and usuario["clave"] == pas:
            print("\nSesión iniciada.")
            return menu2()
        
        else:
            print("Contraseña incorrecta. Intentelo nuevamente.")
            return menu()
        
    print("Usuario no encontrado. Por favor, verifique los datos.")
    return menu()

def menu2():
    print("\nCatálogo de Películas")
    print("1. Ingresar película")
    print("2. Buscar pelicula")
    print("3. Eliminar pelicula")
    print("4. Cerrar sesion")
    opcion2 = input("\n Seleccione una opción: ")

    if opcion2 =="1":
        ingresar_pelicula()
        return menu2()
    elif opcion2 == "2":
        buscar_pelicula()
        return menu2()
    elif opcion2 == "3":
        eliminar_pelicula()
        return menu2()
    elif opcion2 == "4":
        print("Cerrando sesion, volviendo al menu.")
        return menu()
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return menu2()

def ingresar_pelicula():
    print("Complete los datos: ")
    titulo = input("Titulo: ").lower()
    genero = input("Genero: ").lower()
    año = input("Año: ")
    duracion = input("Duracion (min): ")
    sinopsis = input("Sinopsis: ").lower()

    pelicula = {
            "titulo": titulo,
            "genero": genero,
            "año": año,
            "duracion": duracion,
            "sinopsis": sinopsis
    }

    peliculas.append(pelicula)
    
    with open ("peliculas.json","w") as archivo:
            json.dump(peliculas, archivo)
            print("Pelicula registrada con exito.")

def buscar_pelicula():
    tit = input("\nTitulo buscado: ")
    gen = input("Genero buscado: ")
    añ = input("Año buscado: ")

    for pelicula in peliculas:
        if pelicula["titulo"] == tit or pelicula["genero"] == gen or pelicula["año"] == añ:
            print("\n¡Pelicula encontrada!")
            print(f"{pelicula}")
            break
    else:
        print("Pelicula no encontrada.")

def eliminar_pelicula():
    tit = input("\n Titulo de la pelicula que desea eliminar: ")

    for pelicula in peliculas:
        if pelicula["titulo"] == tit:
            peliculas.remove(pelicula)
            print("\t -> Pelicula eliminada con exito.")
            break
        else:
            print("\t -> No se encontro dicha pelicula.")

menu()