def validar_str(dato:str)->str:
    """Valida que una cadena sea de tipo string y le aplica un formato

    Args:
        dato (str): cadena a validar

    Raises:
        TypeError: Si hay error lanzara una excepcion

    Returns:
        str: dato validado
    """
    if type(dato) == str:
        if len(dato) > 0:
            dato = dato.lower().capitalize()
        else:
            dato = "No Tiene"
    else:
        raise TypeError("Esto no es un String!!!")
    return dato

def validar_int(dato:str)->int:
    """Valida que una cadena sea un numero de tipo entero y lo convierte en uno

    Args:
        dato (str): dato a validar

    Raises:
        TypeError: si hay un error lanzara uan excepcion

    Returns:
        int: dato validado
    """
    if type(dato) != int:
        if dato.isdigit():
            dato = int(dato)
        else:
            raise TypeError("Esto no es un numero entero!!!")
    return dato

def validar_float(dato:str)->float:
    """Valida que una cadena sea un numero de tipo flotante y lo convierte en uno

    Args:
        dato (str): dato a validar

    Raises:
        TypeError: si hay un error lanzara uan excepcion

    Returns:
        int: dato validado
    """
    if type(dato) != float:
        if dato.replace('.', '').isdigit() == True:
            dato = float(dato)
        else:
            raise TypeError("Esto no es un numero flotante!!!")
    return dato