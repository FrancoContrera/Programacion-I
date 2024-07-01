import sys
import pygame
import random
import time
from colores import *
from funciones_archivos import *

class JuegoAhorcado:
    def __init__(self, ancho_ventana, alto_ventana, tiempo_limite=60):
        pygame.init()
        self.ancho_ventana = ancho_ventana
        self.alto_ventana = alto_ventana
        self.ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
        pygame.display.set_caption("Juego de Ahorcado")

        self.tiempo_limite = tiempo_limite
        self.fuente_grande = pygame.font.SysFont('arial', 48)
        self.fuente_pequena = pygame.font.SysFont('arial', 24)

        self.cargar_datos()
        self.inicializar_comodines()

        self.inicializar_matriz = lambda palabra: [["_"] for _ in palabra]
        
        self.reiniciar_juego()

        self.ejecutando = True
        self.pausado = False
        self.perdio = False

    def cargar_datos(self):
        # Cargar categorías y palabras desde el archivo JSON
        self.categorias_palabras = cargar_categorias_palabras('categorias_palabras.json')
        self.puntuacion = cargar_puntuacion("puntuacion.csv")
        self.cargar_imagenes()
        
    def cargar_imagenes(self):
        self.boton_pausa_img = self.cargar_imagen("Imagenes/pausa.png", (40, 40))
        self.boton_pausa_rect = self.boton_pausa_img.get_rect(topright=(1190, 10))

        self.signo_instrucciones_img = self.cargar_imagen("Imagenes/signo_de_pregunta.png", (40, 40))
        self.signo_instrucciones_rect = self.signo_instrucciones_img.get_rect(center=(self.ancho_ventana // 2 + 90, self.alto_ventana // 1.8))

        self.boton_casa_img = self.cargar_imagen("Imagenes/casa.png", (100, 100))
        self.boton_play_img = self.cargar_imagen("Imagenes/play.png", (100, 100))
        self.boton_casa_rect = self.boton_casa_img.get_rect(center=(self.ancho_ventana // 2 - 100, self.alto_ventana // 2))
        self.boton_play_rect = self.boton_play_img.get_rect(center=(self.ancho_ventana // 2 + 100, self.alto_ventana // 2))

        self.icono_tiempo_extra_img = self.cargar_imagen("Imagenes/comodin_tiempo.png", (40, 40))
        self.icono_descubrir_letra_img = self.cargar_imagen("Imagenes/comodin_letra.png", (40, 40))
        self.icono_multiplicar_tiempo_img = self.cargar_imagen("Imagenes/comodin_multiplicar.png", (40, 40))

        self.icono_tiempo_extra_rect = self.icono_tiempo_extra_img.get_rect(bottomright=(self.ancho_ventana - 10, self.alto_ventana - 10))
        self.icono_descubrir_letra_rect = self.icono_descubrir_letra_img.get_rect(bottomright=(self.ancho_ventana - 60, self.alto_ventana - 10))
        self.icono_multiplicar_tiempo_rect = self.icono_multiplicar_tiempo_img.get_rect(bottomright=(self.ancho_ventana - 110, self.alto_ventana - 10))

    def cargar_imagen(self, path, size):
        imagen = pygame.image.load(path)
        return pygame.transform.scale(imagen, size)

    def inicializar_comodines(self):
        self.comodines_usados = {
            "tiempo_extra": False,
            "descubrir_letra": False,
            "multiplicar_tiempo": False,
            "multiplicador_tiempo_activo": False
        }

    def seleccionar_categoria(self):
        categorias = list(self.categorias_palabras.keys())
        return random.choice(categorias)

    def seleccionar_palabra(self, categoria):
        palabras = self.categorias_palabras[categoria]
        return random.choice(palabras)

    def actualizar_matriz(self):
        palabra = self.estado_juego["palabra_seleccionada"].lower()
        letras_adivinadas = self.estado_juego["letras_adivinadas"]
        matriz = self.estado_juego["matriz_palabra"]
        palabra = palabra.lower()
        for i in range(len(palabra)):
            letra = palabra[i]
            if letra in letras_adivinadas:
                matriz[i][0] = letra

    def reiniciar_juego(self, tiempo_extra_ronda_anterior=0):
        categoria = self.seleccionar_categoria()
        palabra_seleccionada = self.seleccionar_palabra(categoria)
        matriz_palabra = self.inicializar_matriz(palabra_seleccionada)
        self.estado_juego = {
            "categoria": categoria,
            "palabra_seleccionada": palabra_seleccionada,
            "matriz_palabra": matriz_palabra,
            "letras_adivinadas": [],
            "intentos": 6,
            "tiempo_inicio": time.time(),
            "tiempo_restante": self.tiempo_limite + tiempo_extra_ronda_anterior,
            "mensajes": [],
            "mensajes_temporales": [],
            "comodin_tiempo_extra_usado": self.comodines_usados.get("tiempo_extra", False),
            "comodin_descubrir_letra_usado": self.comodines_usados.get("descubrir_letra", False),
            "comodin_multiplicar_tiempo_usado": self.comodines_usados.get("multiplicar_tiempo", False),
            "multiplicador_tiempo_activo": self.comodines_usados.get("multiplicador_tiempo_activo", False),
        }

    def descubrir_letra(self):
        palabra = self.estado_juego["palabra_seleccionada"]
        letras_adivinadas = self.estado_juego["letras_adivinadas"]
        letras_no_adivinadas = [letra for letra in palabra if letra not in letras_adivinadas]
        
        if letras_no_adivinadas:
            letra_a_descubrir = random.choice(letras_no_adivinadas)
            
            # Verificar cuántas veces se ha descubierto esta letra
            veces_descubierta = letras_adivinadas.count(letra_a_descubrir)
            
            # Añadir la letra a las letras adivinadas
            self.estado_juego["letras_adivinadas"].append(letra_a_descubrir)
            
            # Añadir mensaje temporal solo si la letra no había sido descubierta antes
            if veces_descubierta == 0:
                self.estado_juego["mensajes_temporales"].append((f"Descubierta la letra {letra_a_descubrir}", time.time(), VERDE, 2))
               
    def tiempo_extra(self, tiempo_extra=30):
        self.estado_juego["tiempo_restante"] += tiempo_extra
        self.estado_juego["mensajes_temporales"].append((f"Tiempo EXTRA: {tiempo_extra} segundos", time.time(), VERDE, 2))

    def multiplicar_tiempo(self):
        tiempo_transcurrido = time.time() - self.estado_juego["tiempo_inicio"]
        if tiempo_transcurrido <= 10:
            self.estado_juego["comodin_multiplicar_tiempo_usado"] = True
            self.estado_juego["multiplicador_tiempo_activo"] = True
            self.estado_juego["mensajes_temporales"].append(("Multiplicar tiempo activado", time.time(), VERDE, 2))

    def mostrar_texto(self, texto, posicion, color, fuente):
        texto_renderizado = fuente.render(texto, True, color)
        self.ventana.blit(texto_renderizado, posicion)

    def mostrar_mensajes(self, mensajes, fuente):
        y_offset = 80
        for mensaje in mensajes:
            self.mostrar_texto(mensaje, (10, y_offset), ROJO, fuente)
            y_offset += 30

    def mostrar_mensajes_temporales(self, mensajes_temporales, fuente):
        y_offset = self.alto_ventana - 30
        for mensaje, tiempo, color, duracion in mensajes_temporales:
            if time.time() - tiempo < duracion:
                self.mostrar_texto(mensaje, (10, y_offset), color, fuente)
                y_offset -= 30

    def mostrar_pantalla_perdio(self):
        self.ventana.fill(BLANCO)
        texto_perdio = self.fuente_grande.render("PERDISTE", True, ROJO)
        self.ventana.blit(texto_perdio, (480, 220))
        self.ventana.blit(self.boton_play_img, self.boton_play_rect)
        self.ventana.blit(self.boton_casa_img, self.boton_casa_rect)
        
    def mostrar_pantalla_pausa(self):
        self.ventana.fill(BLANCO)
        texto_pausa = self.fuente_grande.render("PAUSA", True, NEGRO)
        texto_pausa_rect = texto_pausa.get_rect(center=(self.ancho_ventana // 2, self.alto_ventana // 2 - 50))
        self.ventana.blit(texto_pausa, texto_pausa_rect)
        self.ventana.blit(self.boton_casa_img, self.boton_casa_rect)
        self.ventana.blit(self.boton_play_img, self.boton_play_rect)
    

    def dibujar_matriz(self):
        palabra = self.estado_juego["matriz_palabra"]
        x_offset = (self.ancho_ventana - 50 * len(palabra)) // 2
        for i in range(len(palabra)):
            letra = palabra[i][0]
            x_pos = x_offset + i * 50 + 25
            y_pos = self.alto_ventana - 100
            
            if letra == "_":
                guion_bajo_renderizado = self.fuente_grande.render("_", True, NEGRO)
                guion_bajo_rect = guion_bajo_renderizado.get_rect(center=(x_pos, y_pos))
                self.ventana.blit(guion_bajo_renderizado, guion_bajo_rect)
            else:
                letra_renderizada = self.fuente_grande.render(letra, True, NEGRO)
                letra_rect = letra_renderizada.get_rect(center=(x_pos, y_pos))
                self.ventana.blit(letra_renderizada, letra_rect)

    def dibujar_ahorcado(self):
        intentos = self.estado_juego["intentos"]
        x_centro = self.ancho_ventana // 2 - 150
        y_centro = 350

        # Dibujar la horca (está siempre presente)
        pygame.draw.line(self.ventana, NEGRO, (x_centro - 100, y_centro + 150), (x_centro + 100, y_centro + 150), 5)
        pygame.draw.line(self.ventana, NEGRO, (x_centro, y_centro - 150), (x_centro, y_centro + 150), 5)
        pygame.draw.line(self.ventana, NEGRO, (x_centro, y_centro - 150), (x_centro + 100, y_centro - 150), 5)
        pygame.draw.line(self.ventana, NEGRO, (x_centro + 100, y_centro - 150), (x_centro + 100, y_centro - 100), 5)

        # Dibujar las partes del cuerpo
        if intentos < 6:
            pygame.draw.circle(self.ventana, NEGRO, (x_centro + 100, y_centro - 75), 25, 5)  # cabeza
        if intentos < 5:
            pygame.draw.line(self.ventana, NEGRO, (x_centro + 100, y_centro - 50), (x_centro + 100, y_centro + 50), 5)  # cuerpo
        if intentos < 4:
            pygame.draw.line(self.ventana, NEGRO, (x_centro + 100, y_centro - 25), (x_centro + 75, y_centro), 5)  # brazo 1
        if intentos < 3:
            pygame.draw.line(self.ventana, NEGRO, (x_centro + 100, y_centro - 25), (x_centro + 125, y_centro), 5)  # brazo 2
        if intentos < 2:
            pygame.draw.line(self.ventana, NEGRO, (x_centro + 100, y_centro + 50), (x_centro + 75, y_centro + 100), 5)  # pierna 1
        if intentos < 1:
            pygame.draw.line(self.ventana, NEGRO, (x_centro + 100, y_centro + 50), (x_centro + 125, y_centro + 100), 5)  # pierna 2

    def renderizar_pantalla(self):
        self.ventana.fill(BLANCO)
        self.dibujar_ahorcado()
        self.dibujar_matriz()

        self.mostrar_texto(f"Categoría: {self.estado_juego['categoria']}", (10, 10), NEGRO, self.fuente_pequena)
        self.mostrar_texto(f"Tiempo: {int(self.estado_juego['tiempo_restante'])}", (10, 40), NEGRO, self.fuente_pequena)
        self.mostrar_texto(f"Intentos restantes: {self.estado_juego['intentos']}", (10, 70), NEGRO, self.fuente_pequena)
        self.mostrar_texto(f"Puntuación: {self.puntuacion}", (10, 100), NEGRO, self.fuente_pequena)  # Mostrar la puntuación directamente

        self.mostrar_mensajes(self.estado_juego["mensajes"], self.fuente_pequena)
        self.mostrar_mensajes_temporales(self.estado_juego["mensajes_temporales"], self.fuente_pequena)

        self.ventana.blit(self.boton_pausa_img, self.boton_pausa_rect)
        self.ventana.blit(self.icono_tiempo_extra_img, self.icono_tiempo_extra_rect)
        self.ventana.blit(self.icono_descubrir_letra_img, self.icono_descubrir_letra_rect)
        self.ventana.blit(self.icono_multiplicar_tiempo_img, self.icono_multiplicar_tiempo_rect)

        if self.pausado:
            self.mostrar_pantalla_pausa()

        if self.perdio:
            self.mostrar_pantalla_perdio()

        pygame.display.flip()

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if self.boton_pausa_rect.collidepoint(evento.pos):
                    self.pausado = not self.pausado
                if self.pausado:
                    if self.boton_casa_rect.collidepoint(evento.pos):
                        self.volver_al_menu_principal()
                    elif self.boton_play_rect.collidepoint(evento.pos):
                        self.pausado = False
                elif self.perdio:
                    if self.boton_casa_rect.collidepoint(evento.pos):
                        self.volver_al_menu_principal()
                    elif self.boton_play_rect.collidepoint(evento.pos):
                        self.reiniciar_juego()
                        self.perdio = False
                else:
                    if self.icono_tiempo_extra_rect.collidepoint(evento.pos) and not self.estado_juego["comodin_tiempo_extra_usado"]:
                        self.tiempo_extra()
                        self.estado_juego["comodin_tiempo_extra_usado"] = True
                    elif self.icono_descubrir_letra_rect.collidepoint(evento.pos) and not self.estado_juego["comodin_descubrir_letra_usado"]:
                        self.descubrir_letra()
                        self.estado_juego["comodin_descubrir_letra_usado"] = True
                    elif self.icono_multiplicar_tiempo_rect.collidepoint(evento.pos) and not self.estado_juego["comodin_multiplicar_tiempo_usado"]:
                        self.multiplicar_tiempo()
                        self.estado_juego["comodin_multiplicar_tiempo_usado"] = True
            elif evento.type == pygame.KEYDOWN:
                if not self.pausado and not self.perdio:
                    letra = evento.unicode.lower()
                    if letra.isalpha() and letra not in self.estado_juego["letras_adivinadas"]:
                        self.estado_juego["letras_adivinadas"].append(letra)
                        if letra not in self.estado_juego["palabra_seleccionada"].lower():
                            self.estado_juego["intentos"] -= 1
                            self.puntuacion = max(0, self.puntuacion - 10)  # Restar 10 puntos por error, pero no bajar de 0
                            self.estado_juego["mensajes_temporales"].append((f"Letra '{letra}' incorrecta, -10 puntos.", time.time(), ROJO, 2))
                        else:
                            self.puntuacion += 10  # Sumar 10 puntos por acierto
                            self.estado_juego["mensajes_temporales"].append((f"Letra '{letra}' correcta, +10 puntos.", time.time(), VERDE, 2))
                        guardar_puntuacion("puntuacion.csv", self.puntuacion)
            
    def actualizar_estado_juego(self):
        self.actualizar_matriz()
        self.estado_juego["tiempo_restante"] = self.tiempo_limite - (time.time() - self.estado_juego["tiempo_inicio"])

        if self.estado_juego["intentos"] <= 0 or self.estado_juego["tiempo_restante"] <= 0:
            self.perdio = True
            self.estado_juego["mensajes"].append(f"Perdiste! La palabra era: {self.estado_juego['palabra_seleccionada']}")

        if all([letra[0] != "_" for letra in self.estado_juego["matriz_palabra"]]):
            tiempo_restante = self.estado_juego["tiempo_restante"]
            if self.estado_juego["multiplicador_tiempo_activo"]:
                tiempo_restante *= 2
            self.puntuacion += int(tiempo_restante)  # Convertir el tiempo restante en un número entero antes de sumar
            guardar_puntuacion("puntuacion.csv", self.puntuacion)  # Guardar la puntuación actualizada en el archivo CSV
            self.estado_juego["mensajes"].append(f"Palabra completada! Puntuación: {self.puntuacion}")
            self.reiniciar_juego(int(tiempo_restante))  # Pasar el tiempo restante como un número entero
    
    def volver_al_menu_principal(self):
        self.ejecutando = False

    def ejecutar(self):
        while self.ejecutando:
            self.manejar_eventos()
            if not self.pausado and not self.perdio:
                self.actualizar_estado_juego()
            self.renderizar_pantalla()