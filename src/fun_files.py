from validate import *

def parsear_json(path:str, clave:str):
    '''
    Brief : Esta funcion lee los datos almacenados en un archivo json y los
    almacena dentro de una lista de diccionarios.

    Parameters:
        path : Ruta donde se encuentra el archivo
        clave : Clave de la lista de diccionario que quieremos obtener almacenado en el archivo
    
        return retorno : Retorna la lista 
    '''
    import json
    with open(path, "r")as archivo:
        data = json.load(archivo)
    retorno = data[clave] 


    return retorno

def parsear_csv(path:str)->list:
    '''
    Brief : Esta funcion trae todos los datos guardados en un archivo.csv y los
    almacena en una lista .
    
    Parameters:
        path : Ruta donde se encuentra el archivo.
    
        Return lista : Retorna una lista con los datos cargados
    '''
    lista = []
    with open(path, "r", encoding="utf8") as archivo:
        for linea in archivo:
            registro = linea.strip("\n").split(",")
            valor = {} 
            valor["texto"] =validar_str(registro[0])
            valor["x"] = validar_int(registro[1]) 
            valor["y"] = validar_int(registro[2])
            valor["valor"] = validar_int(registro[3])

            lista.append(valor)

    return lista

def crear_csv(path:str,lista:list):
    """Modifica un archivo csv

    Args:
        path (str): direccion donde se guardara el archivo
        lista (list): lista de datos que vamos a guardar en el csv
    """
    with open(path,"w",encoding="utf-8") as archivo:
        for dato in lista:
            mensaje = f"{dato['texto']},{dato['x']},{dato['y']},{dato['valor']:0.0f}\n"
            archivo.write(mensaje)