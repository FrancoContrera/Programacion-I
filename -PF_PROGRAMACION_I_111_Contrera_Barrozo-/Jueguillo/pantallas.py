import pygame
from colores import *
from ahorcado import *

def mostrar_pantalla_perdio(self):
    self.ventana.fill(BLANCO)
    texto_perdio = self.fuente_grande.render("PERDISTE", True, ROJO)
    self.ventana.blit(texto_perdio, (480, 220))
    self.ventana.blit(self.boton_casa_img, self.boton_casa_rect)
    self.ventana.blit(self.boton_play_img, self.boton_play_rect)
        
def mostrar_pantalla_pausa(self):
    self.ventana.fill(BLANCO)
    texto_pausa = self.fuente_grande.render("PAUSA", True, NEGRO)
    texto_pausa_rect = texto_pausa.get_rect(center=(self.ancho_ventana // 2, self.alto_ventana // 2 - 50))
    self.ventana.blit(texto_pausa, texto_pausa_rect)
    self.ventana.blit(self.boton_casa_img, self.boton_casa_rect)
    self.ventana.blit(self.boton_play_img, self.boton_play_rect)

