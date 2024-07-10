
def punto_en_retangulo(punto,rect):
    x,y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def detectar_colision(rect_1, rect_2):
    #Revisa si algun punto de la rect_1 esta en la rect_2
    if (punto_en_retangulo(rect_1.topleft,rect_2) or 
        punto_en_retangulo(rect_1.topright,rect_2) or 
        punto_en_retangulo(rect_1.bottomright,rect_2) or 
        punto_en_retangulo(rect_1.bottomleft,rect_2)):
        return True

    #Revisa si algun punto de la rect_2 esta en la rect_1
    if (punto_en_retangulo(rect_2.topleft,rect_1) or 
        punto_en_retangulo(rect_2.topright,rect_1) or 
        punto_en_retangulo(rect_2.bottomright,rect_1) or 
        punto_en_retangulo(rect_2.bottomleft,rect_1)):
        return True
    
    #Si no hay colision retorna False
    return False