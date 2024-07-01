def aplicar_descuentos_mayoristas(precio, unidades, descuento):
    """Aplica descuentos a los productos

    Args:
        precio (float): Recibe el precio del producto.
        unidades (int): Recibe la cantidad de unidades.
        descuento (float): Recibe el descuento en porcentaje.

    Returns:
        float: Devuelve el precio con el descuento si las unidades son mayores o iguales a 10.
    """
    if unidades >= 10:
        descuento_aplicado = precio * descuento / 100
        precio_con_descuento = precio - descuento_aplicado
        resutado = precio_con_descuento
    else:
        resultado = precio
    return resultado

print(f"El precio con descuento es: {aplicar_descuentos_mayoristas(100, 15, 20)}")