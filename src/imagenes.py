from settings import *
import pygame

tanque_acciones = {}
tanque_acciones["arriba"] = pygame.image.load(PATH_TANK_UP)
tanque_acciones["abajo"] = pygame.image.load(PATH_TANK_DOWN)
tanque_acciones["izquierda"] = pygame.image.load(PATH_TANK_LEFT)
tanque_acciones["derecha"] = pygame.image.load(PATH_TANK_RIGHT)

tanque_rojo_acciones = {}
tanque_rojo_acciones["arriba"] = pygame.image.load(PATH_RED_TANK_UP)
tanque_rojo_acciones["abajo"] = pygame.image.load(PATH_RED_TANK_DOWN)
tanque_rojo_acciones["izquierda"] = pygame.image.load(PATH_RED_TANK_LEFT)
tanque_rojo_acciones["derecha"] = pygame.image.load(PATH_RED_TANK_RIGHT)

tanque_azul_acciones = {}
tanque_azul_acciones["arriba"] = pygame.image.load(PATH_BLUE_TANK_UP)
tanque_azul_acciones["abajo"] = pygame.image.load(PATH_BLUE_TANK_DOWN)
tanque_azul_acciones["izquierda"] = pygame.image.load(PATH_BLUE_TANK_LEFT)
tanque_azul_acciones["derecha"] = pygame.image.load(PATH_BLUE_TANK_RIGHT)

tanque_amarillo_acciones = {}
tanque_amarillo_acciones["arriba"] = pygame.image.load(PATH_YELLOW_TANK_UP)
tanque_amarillo_acciones["abajo"] = pygame.image.load(PATH_YELLOW_TANK_DOWN)
tanque_amarillo_acciones["izquierda"] = pygame.image.load(PATH_YELLOW_TANK_LEFT)
tanque_amarillo_acciones["derecha"] = pygame.image.load(PATH_YELLOW_TANK_RIGHT)