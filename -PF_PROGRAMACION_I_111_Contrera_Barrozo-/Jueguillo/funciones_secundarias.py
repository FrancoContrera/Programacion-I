import pygame
pygame.init()

def cargar_imagen(path: str, ancho: int, alto: int):
    """Carga y escala una imagen al tamaño especificado.

    Args:
        path (str): ruta de la imagen.
        ancho (int): ancho deseado para la imagen.
        alto (int): alto deseado para la imagen.

    Returns:
        pygame.Surface: imagen escalada
    """
    imagen = pygame.image.load(path)
    imagen = pygame.transform.scale(imagen, (ancho, alto))

    return imagen

def crear_y_posicionar_boton(imagen: pygame.Surface, centro: bool , x: int, y: int):
    """Obtiene y posiciona el rectángulo de la imagen.

    Args:
        imagen (pygame.Surface): La imagen para la cual se obtendrá el rectángulo.
        x (int): posicion x del rectángulo.
        y (int): posicion y del rectángulo.
        centro (bool): True, el centro del rectángulo se establece en (x, y). 
                    False, la esquina superior izquierda del rectángulo se establece en (x, y).
    Returns:
        pygame.Rect: el rectangulo posicionado de la imagen.
    """
    centro = False
    boton_rectangulo = imagen.get_rect()
    if centro == True:
        boton_rectangulo.center = (x, y)
    else:
        boton_rectangulo.topleft = (x, y)
    
    return boton_rectangulo

lineas = """Debes de adivinar la palabra oculta
Tienes 60 segundos para adivinarla y 6 intentos
Tienes 3 comodines para utilizar durante la partida
    - Descubrir una letra 
    - Tiempo extra
    - Multiplicar tiempo restante: este comodín se 
      puede elegir solo al comienzo de la partida
      (durante los primeros 10 segundos).
"""

def dibujar_texto(ventana, lineas, fuente, color, x, y):
    lineas = lineas.split("\n")
    posicion_y = 0  #contador para calcular la posicion y en cada linea
    for linea in lineas:
        texto = fuente.render(linea, True, color)
        ventana.blit(texto, (x, y + posicion_y))
        posicion_y +=  fuente.get_height() #esto asegura que cada linea se dibuje abajo de la anterior
        