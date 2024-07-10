import pygame
from pygame.locals import *
from fun_texts import *
from objects import *
from settings import *
from collision import *

def screen_pause(pantalla:pygame.Surface)->bool:
    """Muestra el menu de pausa durante el nivel y pone el juego en estado de pausa

    Args:
        pantalla (pygame.Surface): superficie donde mostraremos el menu pausa

    Returns:
        bool: retorna True si queremos volver al menu y False si queremos continuar jugando
    """
    
    pygame.mixer.music.pause()
    fuente = pygame.font.SysFont(None,100)


    menu = cargar_objetos(PATH_MENU,"menu_pausa")

    salir = False
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == QUIT:   
                pygame.quit()
                exit()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.mixer.music.unpause()
                    running = False
            if e.type == MOUSEBUTTONDOWN:
                for obj in menu:
                    if punto_en_retangulo(e.pos,obj["rect"]):
                        if obj["nombre"] == "jugar":
                            pygame.mixer.music.unpause()
                            salir = False
                            running = False
                        if obj["nombre"] == "volver":
                            salir = True
                            running = False
        
        mostrar_objetos(pantalla,menu)
        mostrar_texto(pantalla,"PAUSA",fuente,(610,100),BLACK)

        pygame.display.flip()
    
    return salir