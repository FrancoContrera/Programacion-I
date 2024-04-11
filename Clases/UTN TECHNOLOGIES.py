#UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.
#
# Las posibles aplicaciones son las siguientes:
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA),
# Internet de las cosas (IOT)

# Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

# A) Los datos a ingresar por cada empleado encuestado son:
# nombre del empleado
# edad (no menor a 18)
# género (Masculino - Femenino - Otro)
#tecnologia (IA, RV/RA, IOT)  
# B) Cargar por terminal 10 encuestas.
# C) Determinar:
# Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
# Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
# Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.

#Alumno: Franco Contrera

contador_masculino = 0
contador_no_IA = 0
mayor_edad_masculino = 0
nombre_mayor_edad_masculino = ""
tecnologia_mayor_edad_masculino = ""

tecnologia_valida = ["IA", "RV/RA", "IOT"]
resultado_encuesta = []

for i in range(10):

    nombre = input("Ingrese el nombre del empleado: ")

    while True:
        edad = int(input("Ingrese la edad del empleado: "))
        if edad >= 18:
            break
        print("La edad debe ser al menos 18. Inténtalo de nuevo.")
    
    while True:
        genero = input("Ingrese el género del empleado: ")
        if genero in ["Masculino", "Femenino", "Otro"]:
            break
        print("El género debe ser Masculino, Femenino u Otro")

    while True:
        tecnologia = input("Ingrese la tecnología por la que vota el empleado (IA, RV/RA, IOT): ")
        if tecnologia in tecnologia_valida:
            break
        print(f"La tecnología debe ser una de las siguientes: IA, RV/RA o IOT")

    resultado_encuesta = (nombre, edad, genero, tecnologia) + resultado_encuesta

    contador_masculino += (genero == "Masculino" and tecnologia in ["IOT", "IA"] and 25 <= edad <= 50)

    contador_no_IA += (tecnologia != "IA" and (genero != "Femenino" or 33 <= edad <= 40))
    
    if genero == "Masculino" and edad > mayor_edad_masculino:
        mayor_edad_masculino = edad
        nombre_mayor_edad_masculino = nombre
        tecnologia_mayor_edad_masculino = tecnologia

porcentaje_no_IA = (contador_no_IA / 10) * 100

print(f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive: {contador_masculino}")

print(f"Porcentaje de empleados que no votaron por IA, cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40: {porcentaje_no_IA:}%")

print(f"Nombre y tecnología de género masculino con mayor edad:{nombre_mayor_edad_masculino} + {tecnologia_mayor_edad_masculino}")

