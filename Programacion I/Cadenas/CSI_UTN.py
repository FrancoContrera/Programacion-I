def es_asesino(secuencia_crimen, secuencia_sospechoso):
    return secuencia_crimen in secuencia_sospechoso

def encontrar_asesino(secuencia_crimen, sospechosos):
    for nombre, adn in sospechosos.items():
        if es_asesino(secuencia_crimen, adn):
            return nombre
    return "SON TODOS INOCENTES"

secuencia_crimen = "CGTTTAATG"
sospechosos = {
    "Juan Pérez": "CGGGGCTAAAATTTTTTACGATCG",
    "María Rodríguez": "AACGTTTAATGTTCTAAGCTGCG",
    "Carlos Sánchez": "CGGGGCTAAAATTTTTTACGATCG"
}

resultado = encontrar_asesino(secuencia_crimen, sospechosos)
print(f"EL asesino es: {resultado}")