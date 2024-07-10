from fun_files import *
import pygame

def mostrar_texto(superficie : pygame.Surface,texto:str,fuente:pygame.font.Font ,posicion:tuple[int,int],
                color:tuple[int,int,int],color_fondo:tuple[int,int,int] = None):
    """Muestra Texto sobre la superficie que nosotros le pasemos

    Args:
        superficie (pygame.Surface): Superficie donde se va a escribir el texto
        texto (str): Texto que queremos escribir
        fuente (pygame.font.Font): Fuente del texto que vamos a escribir
        posicion (tuple[int,int]): Posicion donde vamos a colocar el texto
        color (tuple[int,int,int]): Color del texto
        color_fondo (tuple[int,int,int], optional): Color del fondo del texto .  Defaults to None.
    """
    sup_texto = fuente.render(texto,True,color,color_fondo)
    rect_texto = sup_texto.get_rect(center = posicion)
    superficie.blit(sup_texto,rect_texto)