from funciones import registrar_mascota, registrar_reporte, mostrar_mascotas

def mostrar_menu():
    print("MENÚ DE MASCOTAS")
    print("1. Registrar nueva mascota")
    print("2. Reportar mascota perdida/encontrada")
    print("3. Ver listado de mascotas")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            registrar_reporte()
        elif opcion == "3":
            mostrar_mascotas()
        elif opcion == "4":
            print(" ¡Gracias por usar el sistema de mascotas!")
            break
        else:
            print("Opción no válida. Intentalo de nuevo.")


    main()
