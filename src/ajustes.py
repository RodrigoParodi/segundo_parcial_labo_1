from objects import *
from pygame.locals import *
from collision import *
from fun_texts import *
from settings import *
import pygame

def screen_config(pantalla:pygame.Surface,volumen_musica:float,volumen_sonido:float,dificultad:str)->str:
    """Muesta la pantalla de ajustes del juego

    Args:
        pantalla (pygame.Surface): Superficie donde se va a mostrar el menu
        volumen_musica (float): Volumen de la musica
        volumen_sonido (float): Volumen del sonido
        dificultad (str): Cadena que contiene la dificultad del juego

    Returns:
        int: retorna la dificultado del juego
    """

    image_menu = pygame.image.load("./src/Resources/Images/Backgrounds/FondoMenu.jpg")
    background = pygame.transform.scale(image_menu,SCREEN_SIZE)
    fuente = pygame.font.SysFont(None,50)
    menu = cargar_objetos(PATH_MENU,"menu_ajustes")
    ajustes = parsear_csv(PATH_TEXT)

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == QUIT:   
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                for obj in menu:

                    if punto_en_retangulo(e.pos,obj["rect"]):
                        if obj["nombre"] == "volver":

                            for valor in ajustes:
                                if valor["texto"] == "Musica":
                                    valor["valor"] = 10*volumen_musica
                                elif valor["texto"] == "Sonido":
                                    valor["valor"] = 10*volumen_sonido

                            crear_csv(PATH_TEXT, ajustes)
                            running = False

                        if obj["nombre"] == "izquierda_musica":
                            if volumen_musica*10 > 1 :
                                nuevo_volumen = volumen_musica - 0.1
                                pygame.mixer.music.set_volume(nuevo_volumen)
                                volumen_musica = nuevo_volumen

                        if obj["nombre"] == "derecha_musica":
                            if volumen_musica*10 <= 9 :
                                nuevo_volumen = volumen_musica + 0.1
                                pygame.mixer.music.set_volume(nuevo_volumen)
                                volumen_musica = nuevo_volumen

                        if obj["nombre"] == "izquierda_sonido":
                            if volumen_sonido*10 > 1 :
                                nuevo_volumen = volumen_sonido - 0.1
                                volumen_sonido = nuevo_volumen

                        if obj["nombre"] == "derecha_sonido":
                            if volumen_sonido*10 <= 9 :
                                nuevo_volumen = volumen_sonido + 0.1
                                volumen_sonido = nuevo_volumen

                        if obj["nombre"] == "facil":
                            for opcion in ajustes:
                                if opcion["texto"] == "Facil":
                                    opcion["valor"] = 1
                                    dificultad = opcion["texto"]
                                else:
                                    opcion["valor"] = 0

                        if obj["nombre"] == "media":
                            for opcion in ajustes:
                                if opcion["texto"] == "Media":
                                    opcion["valor"] = 1
                                    dificultad = opcion["texto"]
                                else:
                                    opcion["valor"] = 0

                        if obj["nombre"] == "dificil":
                            for opcion in ajustes:
                                if opcion["texto"] == "Dificil":
                                    opcion["valor"] = 1
                                    dificultad = opcion["texto"]
                                else:
                                    opcion["valor"] = 0
        
        pantalla.blit(background,ORIGIN)
        mostrar_objetos(pantalla,menu)

        mostrar_texto(pantalla,f"VOLUMEN",fuente,(600,200),BLACK)
        mostrar_texto(pantalla,f"{10*volumen_musica:0.0f}",fuente,(675,250),BLACK)
        mostrar_texto(pantalla,f"{10*volumen_sonido:0.0f}",fuente,(675,325),BLACK)
        mostrar_texto(pantalla,f"DIFICULTAD",fuente,(600,400),BLACK)
        for text in ajustes:
            if (text["texto"] == "Facil" or text["texto"] == "Media" or text["texto"] == "Dificil") and text["valor"] == 1:
                mostrar_texto(pantalla,f"{text['texto']}",fuente,(text["x"],text["y"]),YELLOW)
            else:
                mostrar_texto(pantalla,f"{text['texto']}",fuente,(text["x"],text["y"]),BLACK)


        pygame.display.flip()
    return dificultad