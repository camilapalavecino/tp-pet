from funciones import reportar_mascota_perdida, reportar_mascota_encontrada

def mostrar_menu():
    print("MENÚ DE MASCOTAS")
    print("1. Reportar mascota encontrada")
    print("2. Reportar mascota perdida")
    print("3. Ver listado de mascotas")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            #registrar_mascota()
            reportar_mascota_encontrada()
        elif opcion == "2":
            reportar_mascota_perdida()
        elif opcion == "3":
            reportar_mascota_perdida()
            #mostrar_mascotas()
        elif opcion == "4":
            print(" ¡Gracias por usar el sistema de mascotas!")
            break
        else:
            print("Opción no válida. Intentalo de nuevo.")

if __name__ == "__main__":
    main()