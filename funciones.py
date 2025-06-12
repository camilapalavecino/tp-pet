from datetime import datetime
from clase import Perro, Gato, Roedor, Duenio_mascota, Encuentra_mascota, Reporte, Reporte_perdida, Reporte_encuentro, Reporte__coincidencia

def crear_mascota(estado):
    if estado=="Encontrada":
        tipo=input("Ingrese el tipo de mascota (perro, gato, roedor): ")
        color=input("Ingrese el color: ")
        sexo=input("Ingrese el sexo:")
    
        if tipo=="perro":
            tipo="Perro"
            raza=input("Ingrese la raza: ")
            tamanio=input("Ingrese el tamaño: ")
            edad="Indefinida"
            chapa=input("Tiene chapa con nombre? S/N")
            if chapa=="S":
                nombre_mascota=input("Ingrese el nombre: ")
            else:
                nombre_mascota="Desconocido"
            return Perro(tipo,nombre_mascota, color, edad, tamanio, sexo, raza)
    
        elif tipo=="gato":
            tipo="Gato"
            tamanio=input("Ingrese el tamaño: ")
            edad="Indefinida"
            chapa=input("Tiene chapa con nombre? S/N")
            if chapa=="S":
                nombre_mascota=input("Ingrese el nombre: ")
            else:
                nombre_mascota="Desconocido"
            return Gato(tipo, nombre_mascota, color, edad, tamanio, sexo)
    
        elif tipo=="roedor":
            tipo="Roedor"
            edad="Indefinida"
            nombre_mascota="Desconocido"
            especie=input("Ingrese la especie de roedor (conejo, hámster, cobayo): ")
            return Roedor(tipo, nombre_mascota, color, edad, especie, sexo)
        else:
            print("Tipo de mascota no reconocido.")
            return None
        
    elif estado=="Perdida":
        nombre_mascota=input("Ingrese el nombre: ")
        edad=input("Ingrese la edad: ")

        if tipo=="perro":
            tipo="Perro"
            raza=input("Ingrese la raza: ")
            tamanio=input("Ingrese el tamaño: ")
            return Perro(tipo, nombre_mascota, color, edad, tamanio, sexo, raza)
    
        elif tipo=="gato":
            tipo="Gato"
            tamanio=input("Ingrese el tamaño: ")
            return Gato(tipo,nombre_mascota, color, edad, tamanio, sexo)
    
        elif tipo=="roedor":
            tipo="Roedor"
            especie=input("Ingrese la especie de roedor (conejo, hámster, cobayo): ")
            return Roedor(tipo,nombre_mascota, color, edad, especie, sexo)
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
    estado="Perdida"
    mascota=crear_mascota(estado)

    #Evento
    lugar=input("Ingrese las coordenadas de dónde fue visto por última vez: ")
    fecha=input("Ingrese la fecha en que se perdió (formato DD/MM/AAAA): ")
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    #Crear reporte
    reporte=Reporte_perdida(fecha, lugar, mascota, duenio_mascota,estado)
    print("\n✅ Registro completado:")
    reporte.mostrar_datos()

    return reporte

def crear_persona_encuentra():
    nombre=input("Ingrese su nombre: ")
    email=input("Ingrese una dirección de email válida: ")
    
    return Encuentra_mascota(nombre, email)

def reportar_mascota_encontrada():
    print("\n--- REPORTE DE MASCOTA ENCONTRADA ---")
    #Datos persona
    encuentra_mascota=crear_persona_encuentra()

    #Datos mascota
    estado="Encontrada"
    mascota=crear_mascota(estado)

    #Evento
    lugar=input("Ingrese las coordenadas de dónde fue encontrada: ")
    fecha=input("Ingrese la fecha en la que se encontró (formato DD/MM/AAAA): ")
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    #Crear reporte
    reporte=Reporte_encuentro(fecha, lugar, mascota, encuentra_mascota,estado)
    print("\n✅ Registro completado:")
    reporte.mostrar_datos()

    return reporte



