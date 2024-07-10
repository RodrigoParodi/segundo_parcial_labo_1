import pygame
from pygame.locals import *
from settings import *
from objects import *
from fun_texts import *
from collision import *
from stats import screen_stats
from level import star_level
from ajustes import screen_config

#Inicializar pygame
pygame.init()

#Pantalla
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Projecto Halo")
icono = pygame.image.load("./src/Resources/Images/Icono/icono.png")
pygame.display.set_icon(icono)

#Fondo
image_menu = pygame.image.load("./src/Resources/Images/Backgrounds/FondoMenu.jpg")
background = pygame.transform.scale(image_menu,SCREEN_SIZE)

#Musica
pygame.mixer.music.load("./src/Resources/Sounds/Music/musica_menu.wav")
pygame.mixer.music.play(-1)

#CONFIGURACION
ajustes = parsear_csv(PATH_TEXT)

for valor in ajustes:
    if valor["texto"] == "Musica":
        volumen_musica = valor["valor"] / 10
    elif valor["texto"] == "Sonido":
        volumen_sonido = valor["valor"] / 10
    elif (valor["texto"] == "Facil" or valor["texto"] == "Media" or valor["texto"] == "Dificil") and valor["valor"] == 1:
        dificultad = valor["texto"]

pygame.mixer.music.set_volume(volumen_musica)

#Menu
menu = cargar_objetos(PATH_MENU, "menu_inicio")

#Texto
fuente = pygame.font.SysFont(None,50)

running = True
while running:
    #Eventos
    for e in pygame.event.get():
        if e.type == QUIT:   
            running = False
        if e.type == MOUSEBUTTONDOWN:
            for obj in menu:
                if punto_en_retangulo(e.pos,obj["rect"]):
                    if obj["nombre"] == "iniciar":
                        continuar = 1
                        while continuar == 1:
                            continuar = star_level(SCREEN,volumen_musica,volumen_sonido,dificultad)

                        pygame.mixer.music.load("./src/Resources/Sounds/Music/musica_menu.wav")
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(volumen_musica)

                    if obj["nombre"] == "ajustes":
                        dificultad = screen_config(SCREEN,volumen_musica,volumen_sonido,dificultad)
                        ajustes = parsear_csv(PATH_TEXT)

                        for valor in ajustes:
                            if valor["texto"] == "Musica":
                                volumen_musica = valor["valor"] / 10
                            elif valor["texto"] == "Sonido":
                                volumen_sonido = valor["valor"] / 10
                            elif (valor["texto"] == "Facil" or valor["texto"] == "Media" or valor["texto"] == "Dificil") and valor["valor"] == 1:
                                dificultad = valor["texto"]

                    if obj["nombre"] == "stats":
                        screen_stats(SCREEN)

                    elif obj["nombre"] == "salir":
                        running = False

    #DIBUJAR EN PANTALLA
    SCREEN.blit(background,ORIGIN)

    mostrar_objetos(SCREEN,menu)

    pygame.display.flip()

pygame.quit()