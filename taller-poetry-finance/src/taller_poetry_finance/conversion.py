def convertir_usd_a_cop(lista_precios_usd: list, tasa_cambio: float = 4100) -> list:
    """
    Convierte una lista de precios de dólares a pesos colombianos.

    Args:
        lista_precios_usd (list): Lista de precios en USD.
        tasa_cambio (float): Tasa de cambio fija (default 4100).

    Returns:
        list: Lista de precios convertidos a COP.

    Raises:
        ValueError: Si algún precio es negativo o la tasa de cambio es inválida.

    Example:
        >>> convertir_usd_a_cop([100, 50], tasa_cambio=4100)
        [410000.0, 205000.0]
    """
    if tasa_cambio <= 0:
        raise ValueError(f"La tasa de cambio debe ser positiva. Recibido: {tasa_cambio}")

    precios_cop = []
    for precio in lista_precios_usd:
        if precio < 0:
            raise ValueError(f"Los precios no pueden ser negativos. Recibido: {precio}")
        nuevo_precio = round(precio * tasa_cambio, 2)
        precios_cop.append(nuevo_precio)

    return precios_cop
