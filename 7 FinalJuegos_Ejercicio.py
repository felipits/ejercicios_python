import json
import datetime

ventas = []

juegos_info = {
    "princess peach: showtime!": {"precio": 27990, "consola": "nintendo", "tipo": "aventura"},
    "mario vs. donkey kong": {"precio": 31990, "consola": "nintendo", "tipo": "aventura"},
    "hogwarts legacy": {"precio": 28990, "consola": "nintendo", "tipo": "aventura"},
    "metal slug attack reloaded": {"precio": 9990, "consola": "ps5", "tipo": "accion"},
    "crown wars": {"precio": 36990, "consola": "ps5", "tipo": "accion"},
    "ea sports fc 24 fifa 24": {"precio": 26990, "consola": "ps5", "tipo": "deporte"},
    "topspin 2k25": {"precio": 22990, "consola": "ps5", "tipo": "deporte"},
    "rugby 22": {"precio": 32990, "consola": "ps5", "tipo": "deporte"},
    "call of duty black black ops 6": {"precio": 42990, "consola": "ps4", "tipo": "disparos"},
    "red dead redemption + undead nightmare": {"precio": 32990, "consola": "ps4", "tipo": "disparos"}
}

descuentos = {
    "estudiante": 0.85,
    "trabajador": 0.90,
    "socio": 0.80,
}

def menu():
    print("\nMENÚ VIDEOJUEGOS DUOCUC: ")
    print("1. Registrar venta")
    print("2. Mostrar todas las ventas")
    print("3. Buscar venta por cliente")
    print("4. Guardar ventas en archivo")
    print("5. Cargar ventas desde un archivo")
    print("6. Generar factura")
    print("7. Salir del programa")
    opcion = input("\nSeleccione una opción: ")
    
    if opcion == "1":
        registrar_venta()
        return menu()
    elif opcion == "2":
        mostrar_ventas()
        return menu()
    elif opcion == "3":
        buscar_venta()
        return menu()
    elif opcion == "4":
        guardar_ventas()
        return menu()
    elif opcion == "5":
        cargar_ventas()
        return menu()
    elif opcion == "6":
        generar_factura()
        return menu()
    elif opcion == "7":
       print("Adios!")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return menu()
    
def registrar_venta():
    cliente = input("Ingrese nombre del cliente: ").lower()
    tipo_cliente = input("Ingrese tipo de cliente (estudiante / trabajador / socio): ").lower()
    nombre_juego = input("Ingrese nombre del juego: ").lower()
    cantidad = int(input("Unidades deseadas: "))
    
    if tipo_cliente not in descuentos:
        print("Tipo de cliente no valido.")
        return
    
    if nombre_juego not in juegos_info:
        print("Juego no encontrado en la base de datos.")
        return

    juego_info = juegos_info[nombre_juego]
    precio_unitario = juego_info["precio"]
    descuento = descuentos[tipo_cliente]
    precio_total = precio_unitario * cantidad
    precio_final = precio_total * descuento
    
    venta = {
        "cliente": cliente,
        "tipo_cliente": tipo_cliente,
        "nombre_juego": nombre_juego,
        "consola": juego_info["consola"],
        "tipo": juego_info["tipo"],
        "cantidad": cantidad,
        "precio_total": precio_total,
        "precio_final": precio_final
    }
    
    ventas.append(venta)
    print("\nVenta registrada con exito!")
    
def mostrar_ventas():
    if ventas:
        for venta in ventas:
            print(venta)
    else:
        print("\nNo se han registrado ventas.")

def buscar_venta():
    cliente = input("\nIngrese el nombre del cliente: ")
    encontrado = False
    for venta in ventas:
        if venta["cliente"] == cliente:
            print(venta)
            encontrado = True
    if not encontrado:
            print("\nCliente no encontrado.")

def guardar_ventas():
    with open('data_ventas.json', 'w') as archivo:
        json.dump(ventas, archivo)
    print("\nArchivo creado con exito.")

def cargar_ventas():
    global ventas
    with open('data_ventas.json', 'r') as archivo:
        ventas = json.load(archivo)
    print("\nVentas cargadas con exito.")

def generar_factura():
    cliente = input("\nIngrese nombre del cliente: ")
    encontrado = False
    for venta in ventas:
        if venta["cliente"] == cliente:
            encontrado = True
   
            print("\n\t\tVIDEOJUEGOS DUOCUC")
            print("--------------------------------------------------")
            print("Ubicación: \t\t\tAv. España")
            print(f"Hora: \t\t\t\t{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("--------------------------------------------------")
            print(f"Nombre del cliente: \t\t{venta['cliente']}")
            print(f"Tipo de usuario: \t\t{venta['tipo_cliente']}")
            print(f"\n{venta['nombre_juego']} \t\t${venta['precio_total']}")
            print(f"Precio total por {venta['cantidad']} unidade(s): \t\t${venta['precio_total']}")
            print(f"Precio final con dcto: \t\t\t${venta['precio_final']}")
            print("--------------------------------------------------")
            break

        if not encontrado:
            print("\nCliente no encontrado.")

menu()