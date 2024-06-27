import json
import datetime

precios_pizzas = {
    "peperoni": {"pequeña": 5000, "mediana": 8000, "familiar": 10000},
    "mediterranea": {"pequeña": 6000, "mediana": 9000, "familiar": 12000},
    "vegetariana": {"pequeña": 5500, "mediana": 8500, "familiar": 11000},
}

descuentos = {
    "diurno": 0.85,
    "vespertino": 0.80,
    "administrativo": 0.90,
}

ventas = []

def menu():
        print("\nMenú de Ventas de Pizzas:")
        print("1. Registrar una venta")
        print("2. Mostrar todas las ventas")
        print("3. Buscar ventas por cliente")
        print("4. Guardar las ventas en un archivo")
        print("5. Cargar las ventas desde un archivo")
        print("6. Generar Boleta")
        print("7. Salir")
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
            generar_boleta()
            return menu()
        elif opcion == "7":
            print("Saliendo del programa.")
            return
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            return menu()


def registrar_venta():
    cliente = input("\nNombre del cliente: ").lower()
    tipo_usuario = input("Tipo de usuario (diurno / vespertino / administrativo): ").lower()
    tipo_pizza = input("Tipo de pizza (peperoni / mediterranea / vegetariana): ").lower()
    tamaño_pizza = input("Tamaño de pizza (pequeña / mediana / familiar): ").lower()
    cantidad = int(input("Cantidad de pizzas: "))
    
    if tipo_usuario not in descuentos:
        print("Tipo de usuario no válido.")
        return
    
    if tipo_pizza not in precios_pizzas or tamaño_pizza not in precios_pizzas[tipo_pizza]:
        print ("Tipo o tamaño de pizza no valido.")
        return
    
    precio_unitario = precios_pizzas(tipo_pizza)(tamaño_pizza)
    descuento = descuentos(tipo_usuario)
    precio_total = precio_unitario * cantidad
    precio_final = precio_unitario * cantidad * descuento
           
    venta = {
            "cliente": cliente,
            "tipo_usuario": tipo_usuario,
            "tipo_pizza": tipo_pizza,
            "tamaño_pizza": tamaño_pizza,
            "cantidad": cantidad,
            "precio_total": precio_total,
            "precio_final": precio_final
        }
    ventas.append(venta)
    print("Venta registrada con éxito.")

def mostrar_ventas ():
        if ventas:
            for venta in ventas:
                print("\n")
                print(venta)
        else:
            print("No se han registrado ventas.")
    
def buscar_venta():
        cliente = input("\nIngrese el nombre del cliente: ")
        for venta in ventas:
            if venta["cliente"] == cliente:
                print(venta)
                break
        else:
                print("Cliente no encontrado.")
    
def guardar_ventas():
        with open ("data_pizzas.json","w") as archivo:
            json.dump(ventas, archivo)
            print("Archivo creado con exito.")
                                
def cargar_ventas():
        with open ("data_pizzas.json","r") as archivo:
            data_pizzas = json.load(archivo)
            print(data_pizzas)
            ventas = data_pizzas

def generar_boleta():
        cliente = input("\nIngrese nombre del cliente: ")
        encontrado = False
        for venta in ventas:
             if venta["cliente"] == cliente:
                encontrado = True
   
                print("\n\t     Pizzas Duoc")
                print("Ubicación: \t\tAv. España")
                print(f"Hora: \t\t\t{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print("----------------------------------------")
                print(f"Nombre del cliente: \t\t{venta['cliente']}")
                print(f"Tipo de usuario: \t\t{venta['tipo_usuario']}")
                print(f"\n{venta['cantidad']} Pizzas {venta['tipo_pizza']} {venta['tamaño_pizza']} \t")
                print(f"Precio total: \t\t\t${venta['precio_total']}")
                print(f"Precio final con dcto: \t\t${venta['precio_final']}")
                print("----------------------------------------")
                break

        if not encontrado:
            print("Cliente no encontrado.")

menu()