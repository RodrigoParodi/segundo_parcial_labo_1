from settings import *
from sys import exit
from pygame.locals import *
from modo import *
from objects import *
from collision import *
from funciones_nivel_uno import *
from imagenes import *
from fun_texts import *
from end_screen import *
from pausa import *
import pygame

def star_level(pantalla:pygame.Surface,volumen_musica:float,volumen_juego:float,dificultad:str)->int:
    """Inicia el nivel uno mostrando todos sus recursos

    Args:
        pantalla (pygame.Surface): pantalla donde vamos a mostrar el nivel uno
        volumen_musica (float): volumen de la musica
        volumen_juego (float): volumen del juego
        dificultad (str): dificultad en la que se encuentra el juego

    Returns:
        int: retorna un numero entero que indicara si queremos volver al menu o volver a jugar el nivel
    """
    #Fondo Nivel
    image_level = pygame.image.load("./src/Resources/Images/Backgrounds/fondoNivel.png")
    background = pygame.transform.scale(image_level,SCREEN_SIZE)

    #Musica Nivel
    pygame.mixer.music.load("./src/Resources/Sounds/Music/musica_nivel.mp3") #Nueva musica de fondo
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volumen_musica)

    #Personaje
    tanque = crear_tanque(tanque_acciones,490,550,SIZE_TANKS,LIFE)

    #Enemigo
    lista_enemigos = []
    lista_enemigos.append(crear_tanque(tanque_rojo_acciones,200,200,SIZE_TANKS,LIFE_RED,enemigo=True))
    lista_enemigos.append(crear_tanque(tanque_rojo_acciones,100,70,SIZE_TANKS,LIFE_RED,enemigo=True))
    lista_enemigos.append(crear_tanque(tanque_rojo_acciones,320,380,SIZE_TANKS,LIFE_RED,enemigo=True))
    lista_enemigos.append(crear_tanque(tanque_azul_acciones,990,500,SIZE_TANKS,LIFE_BLUE,enemigo=True))
    lista_enemigos.append(crear_tanque(tanque_azul_acciones,860,550,SIZE_TANKS,LIFE_BLUE,enemigo=True))
    lista_enemigos.append(crear_tanque(tanque_amarillo_acciones,850,70,SIZE_TANKS,LIFE_YELLOW,enemigo=True))

    #Sonidos
    disparo = pygame.mixer.Sound("./src/Resources/Sounds/gunshot_sound/sonido_disparo_tanque.mp3")
    explosion = pygame.mixer.Sound("./src/Resources/Sounds/Burst/explosion.mp3")
    disparo.set_volume(volumen_juego)
    explosion.set_volume(volumen_juego)

    #Interfaz
    fondo_interfaz = pygame.image.load("./src/Resources/Images/Interface level/interfaz_nivel.png")
    fondo_tiempo = pygame.image.load("./src/Resources/Images/Interface level/fondo_tiempo.png")
    imagen_tanque = pygame.image.load(PATH_TANK_UP)
    interfaz = pygame.transform.scale(fondo_interfaz,SIZE_INTERFACE)
    tiempo_imagen = pygame.transform.scale(fondo_tiempo,SIZE_INTERFACE_TIME)
    img_tank = pygame.transform.scale(imagen_tanque,SIZE_TANK_IMG)
    fuente = pygame.font.SysFont(None,25)
    fuente_t = pygame.font.SysFont(None,50)

    #MUROS
    muros = cargar_objetos(PATH_LEVEL, "superficies")

    #COINS e ITEMS
    coins =  cargar_objetos(PATH_LEVEL, "coins")
    municiones = cargar_objetos(PATH_LEVEL, "municion")

    #BASE ENEMIGA
    flag_enemy = crear_bloque(PATH_FLAG_ENEMY,630,470,50,100)

    #evento personalizado
    DIRECCION = USEREVENT + 1
    GENERAR_MUNICION = USEREVENT + 2
    TIEMPO = USEREVENT + 3

    #Cargar Dificultad
    if dificultad == "Facil":
        tiempo_nivel = 180
        botiquines = cargar_objetos(PATH_LEVEL, "botiquin")
        daño_proyectil = DAMAGE
    elif dificultad == "Media":
        tiempo_nivel = 120
        botiquines = cargar_objetos(PATH_LEVEL, "botiquin")
        daño_proyectil = DAMAGE
    elif dificultad == "Dificil":
        tiempo_nivel = 70
        botiquines = []
        daño_proyectil = DAMAGE + 10

    #Variables de control
    move_right = False
    move_left = False
    move_up = False
    move_down = False
    salir = 0
    proyectiles = []
    proyectiles_enemigos = []
    tiempo_ultimo_disparo = 0
    tiempo_ultimo_disparo_enemigo = 0
    cont_kills = 0
    municion = 10
    score = 0

    pygame.time.set_timer(TIEMPO, 1000)
    pygame.time.set_timer(DIRECCION, 5000)
    pygame.time.set_timer(GENERAR_MUNICION, 30000)

    running = True
    while running:
        #Eventos
        for e in pygame.event.get():
            if e.type == QUIT:   
                pygame.quit()
                exit()
            if e.type == KEYDOWN:
                if e.key == K_TAB:
                    cambiar_modo()
                if e.key == K_w:
                    move_up = True
                    move_right = False
                    move_left = False
                    move_down = False
                if e.key == K_a:
                    move_left = True
                    move_right = False
                    move_up = False
                    move_down = False
                if e.key == K_s:
                    move_down = True
                    move_right = False
                    move_left = False
                    move_up = False
                if e.key == K_d:
                    move_right = True
                    move_left = False
                    move_up = False
                    move_down = False
                if e.key == K_ESCAPE:
                    if screen_pause(pantalla):
                        salir = 2
                        running = False

            if e.type == KEYUP:
                if e.key == K_w:
                    move_up = False
                if e.key == K_a:
                    move_left = False
                if e.key == K_s:
                    move_down = False
                if e.key == K_d:
                    move_right = False

            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - tiempo_ultimo_disparo >= 500 and municion > 0:
                        #Lanza Disparo

                        disparo.play()
                        p = crear_disparo(tanque["rect"].center,tanque["dir_disparo"],PATH_TANK_PROJECTILE,SPEED_GUNSHOT)
                        proyectiles.append(p)
                        tiempo_ultimo_disparo = tiempo_actual
                        municion -= 1

            if e.type == TIEMPO:
                tiempo_nivel -= 1

            if e.type == DIRECCION:
                if len(lista_enemigos) > 0:
                    numero = randint(0,len(lista_enemigos) - 1)
                    cambiar_direccion(lista_enemigos[numero])

            if e.type == GENERAR_MUNICION and dificultad != "Dificil":
                bloque = municion_random(muros)
                municiones.append(bloque)

        # detecta colision del personaje con un muro
        for muro in muros:
            if detectar_colision(tanque["rect"],muro["rect"]):
                colision = True
                move_right = False
                move_left = False
                move_up = False
                move_down = False
                muro_colisionado = muro
                break
            else:
                colision = False

        #Mover tanque del personaje
        if colision == False:
            if move_left:
                tanque["img"] = pygame.transform.scale(tanque["acciones"]["izquierda"],(40,40))
                tanque["rect"].left -= SPEED
                tanque["dir_disparo"] = "izquierda"

            if move_right:
                tanque["img"] = pygame.transform.scale(tanque["acciones"]["derecha"],(40,40))
                tanque["rect"].left += SPEED
                tanque["dir_disparo"] = "derecha"

            if move_up:
                tanque["img"] = pygame.transform.scale(tanque["acciones"]["arriba"],(40,40))
                tanque["rect"].top -= SPEED
                tanque["dir_disparo"] = "arriba"

            if move_down:
                tanque["img"] = pygame.transform.scale(tanque["acciones"]["abajo"],(40,40))
                tanque["rect"].top += SPEED
                tanque["dir_disparo"] = "abajo"

        elif colision:
            if punto_en_retangulo((tanque["rect"].topleft),muro_colisionado["rect"]) or \
                punto_en_retangulo((tanque["rect"].midleft),muro_colisionado["rect"]) or \
                punto_en_retangulo((tanque["rect"].bottomleft),muro_colisionado["rect"]):
                tanque["rect"].left += SPEED

            if punto_en_retangulo((tanque["rect"].topright),muro_colisionado["rect"]) or \
                punto_en_retangulo((tanque["rect"].midright),muro_colisionado["rect"]) or \
                punto_en_retangulo((tanque["rect"].bottomright),muro_colisionado["rect"]):
                tanque["rect"].right -= SPEED

            if punto_en_retangulo((tanque["rect"].topright),muro_colisionado["rect"]) or \
                punto_en_retangulo((tanque["rect"].midtop),muro_colisionado["rect"]) or \
                punto_en_retangulo((tanque["rect"].topleft),muro_colisionado["rect"]):
                tanque["rect"].top += SPEED

            if punto_en_retangulo((tanque["rect"].bottomright),muro_colisionado["rect"]) or \
                punto_en_retangulo((tanque["rect"].midbottom),muro_colisionado["rect"]) or \
                punto_en_retangulo((tanque["rect"].bottomleft),muro_colisionado["rect"]):
                tanque["rect"].bottom -= SPEED


        #Mover proyectil
        mover_proyectiles(proyectiles)
        mover_proyectiles(proyectiles_enemigos)

        #Eliminar proyectil
        eliminar_proyectiles_colision_muro(proyectiles,muros,explosion)
        eliminar_proyectiles_colision_enemigo(proyectiles,lista_enemigos,explosion)

        eliminar_proyectiles_colision_muro(proyectiles_enemigos,muros,explosion)
        eliminar_proyectiles_colision_personaje(proyectiles_enemigos,tanque,explosion,daño_proyectil)

        #Eliminar coin
        score = eliminar_items(coins,tanque,10,score)

        #Usar botiquin
        if tanque["vida"] < 100:
            tanque["vida"] = eliminar_items(botiquines,tanque,50,tanque["vida"])
        elif tanque["vida"] > 100:
            tanque["vida"] = 100

        #Usar Caja de municion
        municion = eliminar_items(municiones,tanque,5,municion)

        #Mover Enemigos

        if len(lista_enemigos) > 0:
            for enemigo in lista_enemigos:
                movimiento_enemigo(enemigo,muros)
        
        #Eliminar Enemigo
        if len(lista_enemigos) > 0:
            for enemigo in lista_enemigos.copy():
                if enemigo["vida"] <= 0:
                    score += 20
                    cont_kills += 1
                    municion += 1
                    explosion.play()
                    lista_enemigos.remove(enemigo)

        #Rango Disparos Enemigos
        if len(lista_enemigos) > 0:
            for enemigo in lista_enemigos:
                funcion_rango_disparo(enemigo,muros)
        
        #Disparo Enemigo
        if len(lista_enemigos) > 0:
            for enemigo in lista_enemigos:
                if tanque["rect"].colliderect(enemigo["rango"]["rectangulo"]):
                    tiempo_actual_enemigo = pygame.time.get_ticks()
                    if tiempo_actual_enemigo - tiempo_ultimo_disparo_enemigo >= 500:
                        #Lanza Disparo

                        disparo.play()
                        p = crear_disparo(enemigo["rect"].center,enemigo["dir_disparo"],PATH_TANK_PROJECTILE,SPEED_GUNSHOT)
                        proyectiles_enemigos.append(p)
                        tiempo_ultimo_disparo_enemigo = tiempo_actual_enemigo

        #Habilitar Base Enemiga
        if len(lista_enemigos) == 0:
            for muro in muros.copy():
                if muro["nombre"] == "puerta":
                    muros.remove(muro)
                    break
        
        #Pantalla Final
        if detectar_colision(tanque["rect"],flag_enemy["rect"]):
            salir = end(pantalla,True,volumen_juego,"Mision Cumplida",score,tiempo_nivel,cont_kills,municion,tanque["vida"])
        elif tanque["vida"] <= 0:
            salir = end(pantalla,False,volumen_juego,"Tanque Destruido",score,tiempo_nivel,cont_kills,municion,tanque["vida"])
        elif tiempo_nivel == 0:
            salir = end(pantalla,False,volumen_juego,"Tiempo Agotado",score,tiempo_nivel,cont_kills,municion,tanque["vida"])

        if salir == 1 or salir == 2:
            running = False

        #Dibujar en pantalla
        pantalla.blit(background,ORIGIN)

        mostrar_objetos(pantalla,proyectiles)

        mostrar_objetos(pantalla,proyectiles_enemigos)

        mostrar_objetos(pantalla,lista_enemigos)

        pantalla.blit(tanque["img"],tanque["rect"])
        pantalla.blit(flag_enemy["img"],flag_enemy["rect"])
        mostrar_objetos(pantalla,muros)
        mostrar_objetos(pantalla,coins)
        mostrar_objetos(pantalla,botiquines)
        mostrar_objetos(pantalla,municiones)

        pantalla.blit(interfaz,POS_INTERFACE)
        pantalla.blit(img_tank,POS_TANK_IMG)
        pantalla.blit(tiempo_imagen,POS_INTERFACE_TIME)

        mostrar_texto(pantalla,f"VIDA : {tanque['vida']}",fuente,(100,615),BLACK)
        mostrar_texto(pantalla,f"SCORE : {score}",fuente,(100,635),BLACK)
        mostrar_texto(pantalla,f"MUNICION : {municion}",fuente,(100,655),BLACK)
        mostrar_texto(pantalla,f"KILLS : {cont_kills}",fuente,(100,675),BLACK)
        mostrar_texto(pantalla,f"{tiempo_nivel}",fuente_t,(570,650),BLACK)

        if obtener_modo():
            pygame.draw.rect(pantalla,GREEN,tanque["rect"],1)
            pygame.draw.rect(pantalla,BLACK,flag_enemy["rect"],1)
            for muro in muros:
                pygame.draw.rect(pantalla,BLUE,muro["rect"],1)
            for coin in coins:
                pygame.draw.rect(pantalla,GREEN,coin["rect"],1)
            for enemigo in lista_enemigos:
                pygame.draw.rect(pantalla,RED,enemigo["rect"],1)
                pygame.draw.rect(pantalla,RED,enemigo["rango"]["rectangulo"],5)
        
    
        pygame.display.flip()
    
    return salir