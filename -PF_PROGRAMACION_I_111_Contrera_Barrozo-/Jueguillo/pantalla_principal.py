import pygame
import sys
from colores import *
from test import *
from ahorcado import JuegoAhorcado  # Importa la clase JuegoAhorcado
from funciones_secundarias import *
from pantallas import *

pygame.init()

ancho_ventana = 1200
alto_ventana = 720
dimension_ventana = (ancho_ventana, alto_ventana)

ventana = pygame.display.set_mode(dimension_ventana)
pygame.display.set_caption("Ahorcado")

boton_play = cargar_imagen("Imagenes/play.png", 100, 100)
boton_play_rectangulo = crear_y_posicionar_boton(boton_play, True, ancho_ventana // 2, alto_ventana // 2)

boton_instrucciones = cargar_imagen("Imagenes/signo_de_pregunta.png", 65, 65)
boton_instrucciones_rectangulo = crear_y_posicionar_boton(boton_instrucciones, False, 1000, 550)

boton_flecha = cargar_imagen("Imagenes/flecha_1.png", 50, 50)
boton_flecha_rectangulo = crear_y_posicionar_boton(boton_flecha, False, 50, 50)

fuente = pygame.font.SysFont('arial', 80)
texto_ahorcado = fuente.render("AHORCADO", False, NEGRO)
texto_rect = texto_ahorcado.get_rect(center=(ancho_ventana // 2, alto_ventana // 2 - 100))

fuente_instrucciones = pygame.font.SysFont('arial', 35)
texto_titulo_instrucciones = fuente.render("Instrucciones", True, NEGRO)

ventana_principal = 0
ventana_juego = 1
ventana_instrucciones = 2

ventana_actual = ventana_principal
flag_run = True

while flag_run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if ventana_actual == ventana_principal:
                if boton_play_rectangulo.collidepoint(evento.pos):
                    ventana_actual = ventana_juego
                    juego = JuegoAhorcado(ancho_ventana, alto_ventana)
                    juego.ejecutar()  # Llama al método jugar del juego
                    ventana_actual = ventana_principal
                elif boton_instrucciones_rectangulo.collidepoint(evento.pos):
                    ventana_actual = ventana_instrucciones
            elif ventana_actual == ventana_instrucciones:
                if boton_flecha_rectangulo.collidepoint(evento.pos):
                    ventana_actual = ventana_principal
    
    ventana.fill(BLANCO)
    
    if ventana_actual == ventana_principal:
        ventana.blit(texto_ahorcado, texto_rect)
        ventana.blit(boton_play, boton_play_rectangulo)
        ventana.blit(boton_instrucciones, boton_instrucciones_rectangulo)
    elif ventana_actual == ventana_instrucciones:
        ventana.blit(texto_titulo_instrucciones, (400, 120))
        dibujar_texto(ventana, lineas, fuente_instrucciones, NEGRO, 150, 200)
        ventana.blit(boton_flecha, boton_flecha_rectangulo)
    
    pygame.display.update()

