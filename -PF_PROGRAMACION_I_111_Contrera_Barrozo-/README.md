# -PF_PROGRAMACION_I_111_Contrera_Barrozo-

## Juego del Ahorcado
Este juego esta desarrollado en Python utilizando la libreria Pygame

## Instrucciones:
- Debes utilizar el teclado para poder adivinar las letras de la palabra
- Dispones de 60 segundos para descubrir la palabra
- Tienes tres comodines que puedes utilizar:
  1. Descubrir una letra: al seleccionar este comodin el juego descubre una letra al azar. Si existen más incidencias de esa letra no las descubre. 
  2. Tiempo extra: al seleccionar este comodín, se aumentará 30 segundos a la partida actual.
  3. Multiplicar tiempo restante: este comodín se podrá elegir durante los primeros 10 segundos de la partida. El mismo duplicará el tiempo restante una vez encontrada la palabra. Si el jugador no la descubre, el        comodín queda sin efecto.

## Pantalla del juego
~~~ Python 
  while flag_run:
      for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
              flag_run = False
          elif evento.type == pygame.MOUSEBUTTONDOWN:
              if ventana_actual == ventana_principal:
                  if boton_play_rectangulo.collidepoint(evento.pos):
                      ventana_actual = ventana_juego
                      juego = JuegoAhorcado(ancho_ventana, alto_ventana)
                      juego.ejecutar()
                      ventana_actual = ventana_principal
                  elif boton_instrucciones_rectangulo.collidepoint(evento.pos):
                      ventana_actual = ventana_instrucciones
              elif ventana_actual == ventana_instrucciones:
                  if boton_flecha_rectangulo.collidepoint(evento.pos):
                      ventana_actual = ventana_principal
~~~

## Juego en acción 

