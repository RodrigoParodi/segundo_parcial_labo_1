from fun_files import crear_csv
from settings import PATH_TEXT_STATS

def incrementar_stats(stats:list,score:int,kills:int,vida:int,win:bool):
    """Esta funcion incrementa las stats obtenidas por cada nivel

    Args:
        stats (list): Lista que contiene las stats
        score (int): score obtenido en el nivel
        kills (int): kills obtenidas en el nivel
        vida (int): vida sobrante
        win (bool): True = Ganador , False  = Perdedor
    """
    for valor in stats:
        if valor["texto"] == "Max score" and score > valor["valor"]:
            valor["valor"] = score
        elif valor["texto"] == "Score":
            valor["valor"] = score
        elif valor["texto"] == "Partidas":
            valor["valor"] += 1
        elif valor["texto"] == "Kills":
            valor["valor"] = valor["valor"] + kills
        elif valor["texto"] == "Victorias" and win == True:
            valor["valor"] += 1
        elif valor["texto"] == "Derrotas" and win == False:
            valor["valor"] += 1
        elif valor["texto"] == "Muertes" and vida <= 0:
            valor["valor"] += 1
    
    crear_csv(PATH_TEXT_STATS,stats)