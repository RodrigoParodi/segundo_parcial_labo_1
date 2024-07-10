from random import *
from collision import *
from settings import *
from objects import crear_bloque
import pygame

def cambiar_direccion(tanque:dict):
    """Cambia la direccion de un tanque aleatoreamente

    Args:
        tanque (dict): tanque al que le vamos a cambiar la direccion
    """
    numero = randint(1,4)

    while True:
        if numero == 1 and tanque["dir"] != "izquierda":
            tanque["dir"] = "izquierda"
            break
        elif numero == 2 and tanque["dir"] != "derecha":
            tanque["dir"] = "derecha"
            break
        elif numero == 3 and tanque["dir"] != "arriba":
            tanque["dir"] = "arriba"
            break
        elif numero == 4 and tanque["dir"] != "abajo":
            tanque["dir"] = "abajo"
            break
        else:
            numero = randint(1,4)

def movimiento_enemigo(tanque:dict, muros:list):
    """Mueve los tanques enemigos en sus respectivas direcciones

    Args:
        tanque (dict): tanque enemigo que vamos a mover
        muros (list): Muros para detectar colisiones
    """
    for muro in muros:
        if detectar_colision(tanque["rect"],muro["rect"]):
            colision = True
            muro_colisionado = muro
            break
        else:
            colision = False
    
    if colision == False:
        if tanque["dir"] == "izquierda":
            tanque["img"] = pygame.transform.scale(tanque["acciones"]["izquierda"],SIZE_TANKS)
            tanque["rect"].left -= SPEED
            tanque["dir_disparo"] = "izquierda"

        if tanque["dir"] == "derecha":
            tanque["img"] = pygame.transform.scale(tanque["acciones"]["derecha"],SIZE_TANKS)
            tanque["rect"].left += SPEED
            tanque["dir_disparo"] = "derecha"

        if tanque["dir"] == "arriba":
            tanque["img"] = pygame.transform.scale(tanque["acciones"]["arriba"],SIZE_TANKS)
            tanque["rect"].top -= SPEED
            tanque["dir_disparo"] = "arriba"

        if tanque["dir"] == "abajo":
            tanque["img"] = pygame.transform.scale(tanque["acciones"]["abajo"],SIZE_TANKS)
            tanque["rect"].top += SPEED
            tanque["dir_disparo"] = "abajo"

    elif colision:
        if punto_en_retangulo((tanque["rect"].topleft),muro_colisionado["rect"]) or \
            punto_en_retangulo((tanque["rect"].midleft),muro_colisionado["rect"]) or \
            punto_en_retangulo((tanque["rect"].bottomleft),muro_colisionado["rect"]):
            tanque["rect"].left += SPEED
            cambiar_direccion(tanque)

        if punto_en_retangulo((tanque["rect"].topright),muro_colisionado["rect"]) or \
            punto_en_retangulo((tanque["rect"].midright),muro_colisionado["rect"]) or \
            punto_en_retangulo((tanque["rect"].bottomright),muro_colisionado["rect"]):
            tanque["rect"].right -= SPEED
            cambiar_direccion(tanque)

        if punto_en_retangulo((tanque["rect"].topright),muro_colisionado["rect"]) or \
            punto_en_retangulo((tanque["rect"].midtop),muro_colisionado["rect"]) or \
            punto_en_retangulo((tanque["rect"].topleft),muro_colisionado["rect"]):
            tanque["rect"].top += SPEED
            cambiar_direccion(tanque)

        if punto_en_retangulo((tanque["rect"].bottomright),muro_colisionado["rect"]) or \
            punto_en_retangulo((tanque["rect"].midbottom),muro_colisionado["rect"]) or \
            punto_en_retangulo((tanque["rect"].bottomleft),muro_colisionado["rect"]):
            tanque["rect"].bottom -= SPEED
            cambiar_direccion(tanque)

def funcion_rango_disparo(tanque:dict,muros:list):
    """actualiza el rango de disparo de un tanque enemigo 

    Args:
        tanque (dict): datos de un tanque
        muros (list): muros para detectar colisiones
    """
    if tanque["dir"] == "derecha":
        tanque["rango"]['rectangulo'].width = 1200
        tanque["rango"]['rectangulo'].height = 5
        tanque["rango"]["rectangulo"].midleft = tanque["rect"].midright
        for muro in muros:
            if muro["rect"].colliderect(tanque["rango"]["rectangulo"]):
                tanque["rango"]['rectangulo'].width = muro["rect"].x - tanque["rango"]['rectangulo'].x
    elif tanque["dir"] == "izquierda":
        tanque["rango"]['rectangulo'].width = 1200
        tanque["rango"]['rectangulo'].height = 5
        tanque["rango"]["rectangulo"].midright = tanque["rect"].midleft
        for muro in muros:
            if muro["rect"].colliderect(tanque["rango"]["rectangulo"]):
                tanque["rango"]["rectangulo"].left = muro["rect"].right
                tanque["rango"]['rectangulo'].width = tanque["rect"].x - muro["rect"].right
    elif tanque["dir"] == "abajo":
        tanque["rango"]['rectangulo'].width = 5
        tanque["rango"]['rectangulo'].height = 700
        tanque["rango"]["rectangulo"].midtop = tanque["rect"].midbottom
        for muro in muros:
            if muro["rect"].colliderect(tanque["rango"]["rectangulo"]):
                tanque["rango"]['rectangulo'].height = muro["rect"].y - tanque["rango"]['rectangulo'].y
    elif tanque["dir"] == "arriba":
        tanque["rango"]['rectangulo'].width = 5
        tanque["rango"]['rectangulo'].height = 700
        tanque["rango"]["rectangulo"].midbottom = tanque["rect"].midtop
        for muro in muros:
            if muro["rect"].colliderect(tanque["rango"]["rectangulo"]):
                tanque["rango"]["rectangulo"].top = muro["rect"].bottom
                tanque["rango"]['rectangulo'].height = tanque["rect"].y - muro["rect"].bottom


def municion_random(muros:list)->dict:
    """establece una caja de municiones random por el mapa

    Args:
        muros (list): muros para detectar colisiones

    Returns:
        dict: Retorna un nuevo bloque que representa uan caja de municiones nueva
    """
    x = randint(0,WIDTH)
    y = randint(0 , HEIGHT)
    bloque = crear_bloque(PATH_AMMOR,x,y,80,80)
    bandera = True
    while bandera:
        for muro in muros:
            if muro["rect"].colliderect(bloque["rect"]):
                bloque["rect"].center = (randint(0,WIDTH), randint(0 , HEIGHT))
                bandera = True
                break
            else:
                bandera = False
    return bloque

def mover_proyectiles(proyectiles:list):
    """Mueve los proyectiles

    Args:
        proyectiles (list): lista de proyectiles a mover
    """
    if len(proyectiles) > 0:
        for proyectil in proyectiles:
            if proyectil["dir"] == "izquierda":
                proyectil["rect"].move_ip( - proyectil["speed"],0)
            if proyectil["dir"] == "derecha":
                proyectil["rect"].move_ip(proyectil["speed"],0)
            if proyectil["dir"] == "arriba":
                proyectil["rect"].move_ip(0 , -proyectil["speed"])
            if proyectil["dir"] == "abajo":
                proyectil["rect"].move_ip(0,proyectil["speed"])

def eliminar_proyectiles_colision_muro(proyectiles:list,muros:list,sonido):
    """elimina los proyectiles que colisionan contra un muro

    Args:
        proyectiles (list): Proyectiles a eliminar
        muros (list): Muros para detectar colisiones
        sonido (_type_): sonido de explosion
    """
    if len(proyectiles) > 0:
        for proyectil in proyectiles.copy():
            for muro in muros:
                if detectar_colision(proyectil["rect"],muro["rect"]):
                    proyectiles.remove(proyectil)
                    sonido.play()
                    break

def eliminar_proyectiles_colision_enemigo(proyectiles:list,enemigos:list,sonido):
    """Elimina todos los proyectiles que colisiones contra un tanque enemigo

    Args:
        proyectiles (list): lista de proyectiles a eliminar
        enemigos (list): lista de enemigos
        sonido (_type_): Sonido de explosion
    """
    if len(proyectiles) > 0:
        for proyectil in proyectiles.copy():
            for enemigo in enemigos:
                if detectar_colision(proyectil["rect"],enemigo["rect"]):
                    proyectiles.remove(proyectil)
                    enemigo["vida"] -= DAMAGE
                    sonido.play()
                    break

def eliminar_proyectiles_colision_personaje(proyectiles:list,personaje:dict,sonido,daño:int):
    """Elimina todos los proyectiles que colisiones contra el personaje principal

    Args:
        proyectiles (list): lista de proyectiles a eliminar
        personaje (dict): datos del personaje principal
        sonido (_type_): sonido de explosion
        daño (int): cantidad de daño que hacen los proyectiles enemigos
    """
    if len(proyectiles) > 0:
        for proyectil in proyectiles.copy():
            if detectar_colision(proyectil["rect"],personaje["rect"]):
                proyectiles.remove(proyectil)
                personaje["vida"] -= daño
                sonido.play()
                break

def eliminar_items(lista:list,personaje:dict,puntos:int,valor:int)->int:
    """Elimina los items al ser utilizados

    Args:
        lista (list): lista de items
        personaje (dict): personaje principal
        puntos (int): puntos o mejoras que nos dan los items al ser eliminados
        valor (int): candidad actual de puntos del personaje

    Returns:
        int: retorna nueva cantidad de X valor obtenido
    """
    if len(lista) > 0:
        for item in lista.copy():
            if detectar_colision(personaje["rect"],item["rect"]):
                valor += puntos
                lista.remove(item)
                break
    return valor
