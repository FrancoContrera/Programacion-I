from datetime import datetime

class Video:
    def __init__(self, titulo: str, vistas: int, tiempo: int, url_youtube: str, fecha_lanzamiento: str):
        self.titulo = titulo
        self.vistas = vistas
        self.tiempo = tiempo
        self.url_youtube = url_youtube
        self.fecha_lanzamiento = fecha_lanzamiento
        self.sesion = None
        self.colaborador = None
        self.codigo_url = None
        
    def mostrar_tema(self):
        #Agregar los datos pertinentes para que a la hora de mostrar se vean los datos completos del video
        print(f"Titulo: {self.titulo}")
        print(f"Vistas: {self.vistas}")
        print(f"Duración: {self.tiempo} segundos")
        print(f"URL de YouTube: {self.url_youtube}")
        print(f"Fecha de Lanzamiento: {self.fecha_lanzamiento.strftime("%d-%m-%Y")}")
        print("*"*30)

    def dividir_titulo(self):
    # El título tiene el formato: "<colaborador> | Sesión #<número>"
    # Necesitamos dividir el título en partes para obtener el colaborador y el número de sesión
        partes = self.titulo.split(" | ")
    
        self.colaborador = partes[0]
        sesion_partes = partes[1].split("#")
        self.sesion = sesion_partes[1].strip()
        self.sesion = int(self.sesion)
    
    def obtener_codigo_url(self):
        partes = self.url_youtube.split("v=")
        if len(partes) > 1:
            self.codigo_url = partes[1].strip()


    def formatear_fecha(self):
        self.fecha_lanzamiento = self.fecha_lanzamiento.strip()  # Elimina espacios en blanco alrededor de la fecha
        self.fecha_lanzamiento = datetime.strptime(self.fecha_lanzamiento, "%Y-%m-%d")

    def normalizar_videos(lista_videos):
        for video in lista_videos:
            video.dividir_titulo()
            video.obtener_codigo_url()
            video.formatear_fecha()
    
    def mostrar_temas(lista_videos):
        for video in lista_videos:
            video.mostrar_tema()
    
    def ordenar_temas(lista_videos):
        lista_videos.sort(key=lambda video: video.sesion) #lambda que puede tomar cualquier número de argumentos, pero tiene una sola expresión lambda.

    def promedio_vistas(lista_videos):
        suma = 0
        for video in lista_videos:
            suma += video.vistas
        promedio = suma / len(lista_videos)
        #Return promedio
        print(f"El promedio de vistas es: {promedio / 1000} k")
        #promedio = video.promedio_vistas(listas_videos)
        #print(f"El promedio de vistas es: {promedio} k")

    def maximo_reproducciones(lista_videos):
            maximo_video = lista_videos[0]
            for video in lista_videos:
                if video.vistas > maximo_video.vistas:
                    maximo_video = video
            maximo_video.mostrar_tema()

    def buscar_por_colaborador(lista_videos, nombre_colaborador):
        for video in lista_videos:
            if video.lower() == nombre_colaborador.lower():
                video.mostrar_tema()
    
    def buscar_por_mes(lista_videos, mes):
        for video in lista_videos:
            if video.fecha_lanzamiento.month == mes:
                video.mostrar_tema()
    
    def buscar_por_codigo_url(lista_videos, codigo_url):
        for video in lista_videos:
            if video.codigo_url == codigo_url:
                video.mostrar_tema()


