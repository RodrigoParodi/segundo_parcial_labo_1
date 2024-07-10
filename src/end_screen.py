import pygame
from settings import *
from pygame.locals import *
from fun_texts import *
from objects import *
from collision import *
from fun_end_screen import incrementar_stats


def end(pantalla:pygame.Surface,win:bool,volumen_juego:float,mensaje:str,score:int,
        tiempo:int,kills:int,municion:int,vida:int)->int:
    """Muestra la pantalla Final del nivel

    Args:
        pantalla (pygame.Surface): Superficie donde se mostrara la pantalla de FIN de nivel
        win (bool): True = Ganador , False = Perdedor
        volumen_juego (float): volumen del juego
        mensaje (str): mensaje que mostrara debajo del titulo
        score (int): cantidad de puntos obtenidos
        tiempo (int): tiempo en que se termino el nivel
        kills (int): cantidad de kills logradas
        municion (int): Cantidad de municion sobrante
        vida (int): Cantidad de vida sobrante

    Returns:
        int: Devuelve un numero entero donde 1 representa volver  a jugar el nivel y 2 representa volver al menu
    """

    fuente = pygame.font.SysFont(None,80)
    fuente_stats = pygame.font.SysFont(None,50)

    if win:
        mensaje_final = "- WINNER -"
        color = GREEN
    else:
        mensaje_final = "- GAME OVER -"
        color = RED

    menu = cargar_objetos(PATH_MENU, "menu_final")
    stats = parsear_csv(PATH_TEXT_STATS)

    incrementar_stats(stats,score,kills,vida,win)

    pygame.mixer.music.unload()
    game_over = pygame.mixer.Sound("./src/Resources/Sounds/Game over/game_over.mp3")
    game_over.set_volume(volumen_juego)

    game_over.play()
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == QUIT:   
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                for obj in menu:
                    if punto_en_retangulo(e.pos,obj["rect"]):
                        if obj["nombre"] == "jugar":
                            salir = 1
                            running = False
                        if obj["nombre"] == "volver":
                            salir = 2
                            running = False


        pantalla.fill(BLACK)

        mostrar_objetos(pantalla,menu)

        mostrar_texto(pantalla,mensaje_final,fuente,(600,100),color)
        mostrar_texto(pantalla,mensaje,fuente_stats,(600,150),color)
        mostrar_texto(pantalla,f"SCORE : {score}",fuente_stats,(600,200),WHITE)
        mostrar_texto(pantalla,f"TIME : {tiempo}",fuente_stats,(600,250),WHITE)
        mostrar_texto(pantalla,f"KILLS : {kills}",fuente_stats,(600,300),WHITE)
        mostrar_texto(pantalla,f"MUNICION : {municion}",fuente_stats,(600,350),WHITE)

        pygame.display.flip()
    
    return salir

