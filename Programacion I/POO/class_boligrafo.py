class Bolígrafo:
    def __init__(self, color, grosor_punta):
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = grosor_punta
        self.color = color
        self.cantidad_tinta = 80

    def escribir(self, texto):
        gasto_tinta = len(texto)
        if self.grosor_punta == "Grueso":
            gasto_tinta *= 2

        if self.cantidad_tinta >= gasto_tinta:
            self.cantidad_tinta -= gasto_tinta
            return texto
        else:
            return "No alcanza la tinta"

    def recargar(self, cantidad):
        nueva_cantidad = self.cantidad_tinta + cantidad
        if nueva_cantidad > self.capacidad_tinta_maxima:
            exceso = nueva_cantidad - self.capacidad_tinta_maxima
            self.cantidad_tinta = self.capacidad_tinta_maxima
            return f"Se recargó la lapicera y sobró {exceso} cantidad de tinta."
        else:
            self.cantidad_tinta = nueva_cantidad
            return "Lapicera recargada"