from clase import Perro, Gato, Roedor, Duenio_mascota, Encuentra_mascota, Reporte_perdida, Reporte_encuentro, Reporte__coincidencia

def crear_mascota():
    tipo=input("Ingrese el tipo de mascota (perro, gato, roedor): ")
    nombre_mascota=input("Ingrese el nombre: ")
    color=input("Ingrese el color: ")
    sexo=input("Ingrese el sexo:")
    edad=input("Ingrese la edad: ")

    if tipo=="perro":
        raza=input("Ingrese la raza: ")
        tamanio=input("Ingrese el tamaño: ")
        return Perro(nombre_mascota, color, edad, tamanio, sexo, raza)
    
    elif tipo=="gato":
        return Gato(nombre_mascota, color, edad, tamanio, sexo)
    
    elif tipo=="roedor":
        especie=input("Ingrese la especie de roedor (conejo, hámster, cobayo): ")
        return Roedor(nombre_mascota, color, edad, especie, sexo)
    else:
        print("Tipo de mascota no reconocido.")
        return None
        
def crear_duenio_mascota_perdida():
    nombre=input("Ingrese su nombre: ")
    email=input("Ingrese una dirección de email válida: ")
    
    return Duenio_mascota(nombre, email)


def reportar_mascota_perdida():
    print("\n--- REPORTE DE MASCOTA PERDIDA ---")
    #Datos dueño
    duenio_mascota=crear_duenio_mascota_perdida()

    #Datos mascota
    mascota=crear_mascota()

    #Evento
    lugar=input("Ingrese las coordenadas de dónde fue visto por última vez: ")
    fecha=input("Ingrese la fecha en que se perdió: ")
    estado="Perdida"
    #Crear reporte
    reporte=Reporte_perdida(fecha, lugar, mascota, duenio_mascota,estado)
    print("\n✅ Registro completado:")
    reporte.mostrar_datos()

    return reporte



