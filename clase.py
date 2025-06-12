# clases.py

from datetime import datetime
from abc import ABC, abstractmethod

class Mascota:
    #Mascota.{tipo,color, nombre, edad, tamaño, sexo, estado}
    def __init__(self,tipo:str, nombre: str, color: str, edad: int, tamanio: str, sexo: str): #Aclaramos los tipos para un mejor manejo de los datos
        self.tipo=tipo
        self.nombre = nombre
        self.color = color
        self.edad=edad
        self.tamanio=tamanio
        self.sexo=sexo
    def __str__(self):
        return f"{self.tipo} | {self.nombre} | {self.color} | Edad: {self.edad} | Tamaño: {self.tamanio} | {self.sexo} "


    #Perro {color, nombre, edad, tamaño, sexo, raza, estado}
	#	Gato{color, nombre, edad, tamaño, sexo, estado}
	#	Roedor{color, nombre, edad, tamaño, sexo, tipo [ej, conejo, hámster, cobayo], estado}

class Perro(Mascota):
    def __init__(self,tipo:str, nombre: str, color: str, edad: int, tamanio: str, sexo:str, raza:str):
        super().__init__(tipo,nombre, color, edad, tamanio, sexo)
        self.raza=raza
    def __str__(self):
        return f"{self.tipo} | {self.nombre} | {self.color} | Edad: {self.edad} | Tamaño: {self.tamanio} | {self.sexo} | {self.raza} "

class Gato(Mascota):
    def __init__(self, tipo:str,nombre:str, color:str, edad:str, tamanio:str, sexo:str):
        super().__init__(tipo, nombre, color, edad, tamanio, sexo)
    def __str__(self):
        return f"{self.tipo} | {self.nombre} | {self.color} | Edad: {self.edad} | Tamaño: {self.tamanio} | {self.sexo} "

class Roedor(Mascota):
    def __init__(self, tipo:str, nombre:str, color:str, edad:int, especie:str, sexo:str):
        super().__init__(tipo, nombre, color, edad, especie, sexo)
        self.especie=especie
    def __str__(self):
        return f"{self.tipo} | {self.nombre} | {self.color} | Edad: {self.edad} | Tamaño: {self.especie} | {self.sexo} "

#Clase Padre: 	Persona {nombre, contacto[telefono o mail], mascota}
#Clases hijas: 	Dueño_Mascota {nombre, contacto, mascota}
#		Encuentra_Mascota{nombre, contacto, mascota}    
class Persona:
    def __init__(self, nombre: str, email:str):
        self.nombre=nombre
        self.email=email
def __str__(self):
        return f"{self.nombre} | {self.email}"

class Duenio_mascota(Persona):
    def __init__(self, nombre:str, email:str):
        super().__init__(nombre, email)
    def __str__(self):
        return f"{self.nombre} | {self.email}"
    

class Encuentra_mascota(Persona):
    def __init__(self, nombre:str, email:str):
        super().__init__(nombre, email)
    def __str__(self):
        return f"{self.nombre} | {self.email}"
        
#Clase Padre: 	Registro{fecha, lugar, mascota, persona, estado}
#Clases hijas:	Registro_perdida{fecha, lugar, mascota, persona, estado}
#egistro_encuentro{fecha, lugar, mascota, persona, estado}
#Registro_coincidencia{registro1, registro2,persona, estado}

class Reporte(ABC):
    def __init__(self, fecha:datetime, lugar:str, mascota:Mascota, persona:Persona, estado:str):
        self.fecha=fecha
        self.lugar=lugar
        self.mascota=mascota
        self.persona=persona
        self.estado=estado

        @abstractmethod
        def mostrar_datos():
            pass

class Reporte_perdida(Reporte):
    def __init__(self, fecha:datetime, lugar:str, mascota:Mascota, duenio_mascota:Persona, estado:str):
        super().__init__(fecha, lugar, mascota, duenio_mascota, estado)
    def __str__(self):
        return f"{self.fecha} | {self.lugar} | {self.mascota} | {self.duenio_mascota} | Estado: {self.estado}"
    
    def mostrar_datos(self):
         print(f"""
    🐾 Reporte de pérdida:
    Fecha: {self.fecha.strftime('%d/%m/%Y')}
    Lugar: {self.lugar}
    Estado: {self.estado}
    
    📌 Mascota:
    {self.mascota}
    
    👤 Dueño:
    {self.persona}
    """)

class Reporte_encuentro(Reporte):
    def __init__(self, fecha:datetime, lugar:str, mascota:Mascota, persona:Persona, estado:str):
        super().__init__(fecha, lugar, mascota, persona, estado)
    def __str__(self):
        return f"{self.fecha} | {self.lugar} | {self.mascota} | {self.duenio_mascota} | Estado: {self.estado}"

    def mostrar_datos(self):
         print(f"""
    🐾 Reporte de encuentro:
    Fecha: {self.fecha.strftime('%d/%m/%Y')}
    Lugar: {self.lugar}
    Estado: {self.estado}
    
    📌 Mascota:
    {self.mascota}
    
    👤 Reportante:
    {self.persona}
    """)

class Reporte__coincidencia(Reporte):
    def __init__(self,reporte1:Reporte, reporte2: Reporte, persona: Persona, estado:str):
        super().__init__(persona, estado)
        self.reporte1=reporte1
        self.reporte2=reporte2
    def __str__(self):
        return f"{self.fecha} | {self.lugar} | {self.mascota} | {self.duenio_mascota} | Estado: {self.estado}"

    def mostrar_datos(self):
         print(f"""
    🐾 Reporte de pérdida:
    Fecha: {self.fecha.strftime('%d/%m/%Y')}
    Lugar: {self.lugar}
    Estado: {self.estado}
    
    📌 Mascota:
    {self.mascota}
    
    👤 Persona:
    {self.persona}
    """)