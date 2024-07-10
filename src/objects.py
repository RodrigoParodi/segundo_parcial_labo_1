from fun_files import *
from settings import *
import pygame

def crear_bloque(imagen,left=0, top=0, ancho=40, alto=40, nombre="N/A")->dict:
    """Fabrica un objeto con una imagen 

    Args:
        imagen (_type_): imagens que le vamos a colocar
        left (int, optional): posicion y
        top (int, optional): posicion x
        ancho (int, optional): cantidad de ancho
        alto (int, optional): cantidad de altura
        nombre (str, optional): nombre del objeto , por default tendra de nombre "N/A"

    Returns:
        dict: diccionario que contiene los datos del objeto creado
    """
    rec = pygame.Rect(left, top, ancho, alto)
    imagen = pygame.transform.scale(pygame.image.load(imagen),(ancho,alto))

    return {"rect": rec, "nombre": nombre,"img":imagen}


def crear_tanque(imagenes,left=0, top=0, tamaño = (40,40), vida = 100, direccion ="derecha",enemigo = False)->dict:
    """Crea un tanque para los niveles

    Args:
        imagenes (_type_): imagenes de un tanque
        left (int, optional): posicion y
        top (int, optional): posicion x
        tamaño(tuple): tamaño que tendra el tanque
        vida (int, optional): Cantidad de vida. Defaults to 100.
        direccion (str, optional): direcion inicial . Defaults to "derecha".
        enemigo (bool, optional): si el tanque es enemigo True, si no lo es False

    Returns:
        dict: datos del tanque creado
    """

    datos = {}
    datos["rect"] = pygame.Rect(left, top, tamaño[0],tamaño[1])
    datos["dir"] = direccion
    datos["img"] = pygame.transform.scale(imagenes["derecha"],tamaño)
    datos["acciones"] = imagenes
    datos["dir_disparo"] = direccion
    datos["vida"] = vida

    if enemigo:
        x = datos["rect"].right
        y = datos["rect"].centery
        datos["rango"] = crear_rango_disparo((1200,5),x,y)

    return datos

def cargar_objetos(path:str,clave:str)->list:
    """crea todos los objetos que necesitamos almacenados en un archivo .json y los carga en una lista

    Args:
        path (str): path donde se encuentran los objetos
        clave (str): clave de la lista de objetos que queremos cargar

    Returns:
        list: Lista que contendra los objetos creados y cargados
    """
    objeto = parsear_json(path,clave)
    lista_objetos = []
    for obj in objeto:
        bloque = crear_bloque(obj["path_imagen"],obj["x"],obj["y"],obj["ancho"],obj["largo"],obj["nombre"])
        lista_objetos.append(bloque)

    return lista_objetos


def mostrar_objetos(pantalla:pygame.Surface,lista_objetos:list):
    """Muestra una lista de objetos en la pantalla

    Args:
        pantalla (pygame.Surface): pantalla donde vamos a mostrar los objetos
        lista_objetos (list): lista de objetos que vamos a mostrar
    """

    for obj in lista_objetos:
        pantalla.blit(obj["img"],obj["rect"])

def crear_disparo(posicion:tuple[int,int],direccion = "derecha",imagen = None, speed = 20):
    """Crea un proyectil

    Args:
        posicion (tuple[int,int]): posicion por donde saldra el disparo
        direccion (str, optional): direccion inicial del disparo . Defaults to "derecha".
        imagen (_type_, optional): imagen del proyectil . Defaults to None.
        speed (int, optional): velocidad del disparo . Defaults to 20.

    Returns:
        _type_: datos del proyectil creado
    """
    r = pygame.Rect(0,0,GUNSHOT_WIDTH,GUNSHOT_HEIGHT)
    r.midbottom = posicion
    imagen = pygame.transform.scale(pygame.image.load(imagen),(GUNSHOT_WIDTH,GUNSHOT_HEIGHT))

    return {"rect": r, "img": imagen,"dir":direccion, "speed":speed}

def crear_rango_disparo(tamaño , x,y):
    """crea diccionario con un rectangulo que representa el rango de disparo de un tanque enemigo

    Args:
        tama (_type_): tamaño del rango
        x (_type_): pos x del rectangulo
        y (_type_): pos y del rectangulo

    Returns:
        _type_: retorna el rango creado
    """

    rango = {}

    rango["superficie"] = pygame.Surface(tamaño)

    rango["rectangulo"] = rango["superficie"].get_rect()
    rango["rectangulo"].x = x
    rango["rectangulo"].y = y

    return rango