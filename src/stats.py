from objects import *
from pygame.locals import *
from collision import *
from fun_texts import *
from settings import *
import pygame

def screen_stats(pantalla:pygame.Surface):
    """Muestra la pantalla de estadisticas obtenidas en el nivel

    Args:
        pantalla (pygame.Surface): pantalla donde vamos a mostrar el menu de estadisticas
    """
    
    image_menu = pygame.image.load("./src/Resources/Images/Backgrounds/FondoMenu.jpg")
    background = pygame.transform.scale(image_menu,SCREEN_SIZE)
    fuente = pygame.font.SysFont(None,50)
    menu = cargar_objetos(PATH_MENU,"menu_stats")
    stats = parsear_csv(PATH_TEXT_STATS)

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
                            running = False
        
        pantalla.blit(background,ORIGIN)
        mostrar_objetos(pantalla,menu)
        for text in stats:
            mostrar_texto(pantalla,f"{text['texto']} : {text['valor']} ",fuente,(text["x"],text["y"]),BLACK)

        pygame.display.flip()
    