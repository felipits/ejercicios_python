import json
departamentos = []

while True:
    print("\nSistema de Gestion de Ventar de Departamentos")
    print("1. Agregar Departamento")
    print("2. Lista de Departamentos")
    print("3. Buscar Departamento")
    print("4. Modificar Departamento")
    print("5. Eliminar Departamento")
    print("6. Guardar Datos")
    print("7. Cargar y ver Datos")
    print("8. Salir")
    menu = input("Seleccione una opción: ")
    print()

    if menu == "1":
        id = int(input("Ingrese ID del departamento: "))
        direccion = input("Ingrese la direccion: ")
        precio = int(input("Ingrese el precio: "))
        superficie = int(input("Ingrese la superficie: "))
        num_habitaciones = int(input("Ingrese numero de habitaciones: "))
        
        departamento = {
            "id": id,
            "direccion": direccion,
            "precio": precio,
            "superficie": superficie,
            "num_habitaciones": num_habitaciones
            
        }
        departamentos.append(departamento)
        print("Departamento agregado exitosamente.")
        
    elif menu == "2":
        if departamentos:
            for departamento in departamentos:
                print(departamento)
        else:
            print("No hay departamentos listados.")
    
    elif menu == "3":
        id = input("Ingrese el ID del departamento a buscar: ")
        for departamento in departamentos:
            if departamento["id"] == id:
                print(departamento)
                break
        else:
                print("Departamento no encontrado.")
    
    elif menu == "4":
        id = input("Ingrese el ID del departamento a modificar: ")
        encontrado = False
        for departamento in departamentos:
            if departamento["id"] == id:
                encontrado = True
                print("Ingrese los nuevos datos del departamento:")
                departamento["direccion"] = input("Ingrese la direccion: ")
                departamento["precio"] = int(input("Ingrese el precio: "))
                departamento["superficie"] = int(input("Ingrese la superficie: "))
                departamento["num_habitaciones"] = int(input("Ingrese numero de habitaciones: "))

                print("Departamento modificado exitosamente.")
                break
        if not encontrado:
                print("Departamento no encontrado.")
                                
    elif menu == "5":
        id = input("Ingrese el ID del departamento a eliminar: ")
        for departamento in departamentos:
            if departamento["id"] == id:
                departamentos.remove(departamento)
                print("Departamento eliminado exitosamente.")
                break
            else:
                print("Departamento no encontrado.")
    
    elif menu == "6":
        with open ("data_dptos.json","w") as archivo:
            json.dump(departamentos, archivo)
        print("Archivo creado con exito.")

    elif menu == "7":
        with open ("data_dptos.json","r") as archivo:
            dptos_leidos = json.load(archivo)
            print(dptos_leidos)
            departamentos = dptos_leidos

    else:
        print("Seleccione un opcion valida.")
        break
        print("Saliendo del programa...")