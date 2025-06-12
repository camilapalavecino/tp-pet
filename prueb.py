from datetime import datetime

class Reporte:
    def __init__(self, tipo_reporte, ubicacion, fecha=None):
        self.tipo_reporte = tipo_reporte    # 'Perdido' o 'Encontrado'
        self.ubicacion = ubicacion          # Ej: 'Buenos Aires'
        # Si no se pasa fecha, se pone la actual automáticamente
        self.fecha = fecha if fecha else datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        return f"Reporte: {self.tipo_reporte} | Ubicación: {self.ubicacion} | Fecha: {self.fecha}"
