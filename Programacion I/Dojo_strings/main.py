from class_video import *
from datetime import datetime
from data import *

"""
Consigna:
1. IMPLEMENTAR LOS METODOS VACIOS DE LA CLASE VIDEO

2. CREAR UN MENU DE USUARIO CON LAS SIGUIENTES OPCIONES:

A. NORMALIZAR OBJETOS: para cada video de la lista, se deberá llamar a los métodos de instancia: dividir_titulo, 
obtener_codigo_url y formatear_fecha, dado que la lista de objetos que nos pasan no cumple con las normas de estandarización 
de videos que nos solicitan.
B. MOSTRAR TEMAS: se deberá mostrar la lista de todos los temas
C. ORDENAR TEMAS: los temas se ordenarán por número de sesión de menor a mayor.
D. PROMEDIO DE VISTAS: mostrar el promedio de vistas expresado en k.
E. MAXIMA REPRODUCCION: mostrar el o los videos con mayor cantidad de vistas.
F. BUSQUEDA POR CODIGO: mostrar los videos cuyo código comiencen con la palabra "nick"
G. LISTAR POR COLABORADOR: el usuario ingresa el nombre de un colaborador y el programa deberá listar todos los videos de 
ese colaborador.
H. LISTAR POR MES: el usuario ingresa un mes, y se deberán listar todos los temas lanzados en ese mes (sin importar el año)
I. SALIR 

NOTA: 
1. Las opciones BCDEFG no serán accesibles si no se normalizan previamente los datos.
2. Todas las opciones tienen que estar resueltas en metodos de la clase Video que reciban una lista de videos sumado a los
parametros necesarios para lograr el objetivo y mantener independencia de código.
"""

lista_videos = [
    Video("Trueno | Sesión #1", 25000000, 210, "https://www.youtube.com/watch?v=trueno1", "2020-06-05"),
    Video("Nathy Peluso | Sesión #36", 85000000, 180, "https://www.youtube.com/watch?v=nathypeluso36", "2020-11-27"),
    Video("Khea | Sesión #34", 65000000, 220, "https://www.youtube.com/watch?v=khea34", "2020-08-12"),
    Video("Nicki Nicole | Sesión #13", 130000000, 200, "https://www.youtube.com/watch?v=nicki13", "2019-04-23"),
    Video("YSY A | Sesión #37", 70000000, 210, "https://www.youtube.com/watch?v=ysya37", "2021-01-15"),
    Video("L-Gante | Sesión #38", 80000000, 190, "https://www.youtube.com/watch?v=lgante38", "2021-03-09"),
    Video("Duki | Sesión #50", 120000000, 210, "https://www.youtube.com/watch?v=duki50", "2022-05-14"),
    Video("Tiago PZK | Sesión #48", 95000000, 230, "https://www.youtube.com/watch?v=tiago48", "2022-02-20"),
    Video("Rauw Alejandro | Sesión #39", 110000000, 220, "https://www.youtube.com/watch?v=rauw39", "2021-05-15"),
    Video("Cazzu | Sesión #32", 72000000, 215, "https://www.youtube.com/watch?v=cazzu32", "2020-07-10"),
    Video("Nicky Jam | Sesión #40", 100000000, 195, "https://www.youtube.com/watch?v=nicky40", "2021-07-01"),
    Video("Anuel AA | Sesión #45", 115000000, 210, "https://www.youtube.com/watch?v=anuel45", "2021-11-05"),
    Video("Bad Bunny | Sesión #52", 150000000, 220, "https://www.youtube.com/watch?v=bunny52", "2022-06-10"),
    Video("Residente | Sesión #49", 90000000, 240, "https://www.youtube.com/watch?v=residente49", "2022-04-03"),
    Video("Ozuna | Sesión #44", 130000000, 215, "https://www.youtube.com/watch?v=ozuna44", "2021-10-25"),
    Video("Myke Towers | Sesión #43", 95000000, 200, "https://www.youtube.com/watch?v=myke43", "2021-09-30"),
    Video("Lunay | Sesión #47", 80000000, 205, "https://www.youtube.com/watch?v=lunay47", "2021-12-20"),
    Video("Jhay Cortez | Sesión #46", 100000000, 220, "https://www.youtube.com/watch?v=jhay46", "2021-11-30"),
    Video("Sech | Sesión #41", 95000000, 210, "https://www.youtube.com/watch?v=sech41", "2021-08-15"),
    Video("Arcángel | Sesión #42", 110000000, 225, "https://www.youtube.com/watch?v=arcangel42", "2021-09-01")
]

opciones_menu = {
    "A": "Normalizar objetos",
    "B": "Mostrar los temas",
    "C": "Ordenar los temas de menor a mayor",
    "D": "Promedio de vistas expresado en K",
    "E": "Mostrar video/videos con maximas vistas",
    "F": "Busqueda de codigo con la palabra Nick",
    "G": "Listar videos por colaborador",
    "H": "Listar videos por mes",
    "I": "Salir del program"
}
datos_normalizados = False
bandera_seguir = True

while True:
    opcion = str(input("Que desea hacer: \n"
                       "A. Normalizar objetos \n"
                       "B. Mostrar los temas \n"
                       "C. Ordenar los temas de menor a mayor \n"
                       "D. Promedio de reproducciones expresado en K \n"
                       "E. Mostrar video/videos con máximas reproducciones \n"
                       "F. Búsqueda de código con la palabra Nick \n"
                       "G. Listar videos por colaborador \n"
                       "H. Listar videos por mes \n"
                       "I. Salir del programa \n"))

    if opcion == "A":
        Video.normalizar_videos(lista_videos) #convertir en objeto datetime
        print("Los Objetos")

    elif opcion == "B":
        Video.mostrar_temas(lista_videos)

    elif opcion == "C":
        Video.ordenar_temas(lista_videos)
        print("Temas ordenados correctamente.")

    elif opcion == "D":
        Video.promedio_vistas(lista_videos)

    elif opcion == "E":
        Video.maximo_reproducciones(lista_videos)
        print(f"{Video.maximo_reproducciones}")

    elif opcion == "F":
        codigo = input("Introduzca el código: ")
        Video.buscar_por_codigo_url(lista_videos, codigo)

    elif opcion == "G":
        colaborador = input("Introduzca el colaborador: ")
        Video.listar_videos_por_colaborador(colaborador, lista_videos)

    elif opcion == "H":
        mes = input("Introduzca el mes (en formato MM): ")
        Video.listar_por_mes(lista_videos, mes)

    elif opcion == "I":
        print("Hasta la proximaaa")
        break

    else:
        print("Opcion invalida")




