import pygame,sys,random
from Funciones import *

pygame.init()

def Victoria():
    resolucion=[960,800]
    ventana=pygame.display.set_mode(resolucion)
    Continuar=pygame.Rect(resolucion[0]-100,resolucion[1]-100,150,50)
    fotograma = 0
    f_muro = 0
    continuar=pygame.Rect(resolucion[0]-200,resolucion[1]-125,170,70)

    araña_feliz = [pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Feliz_L.png").convert_alpha()
                ,pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Feliz_R.png").convert_alpha()]
    araña_feliz[0] = pygame.transform.scale(araña_feliz[0],(570,380))
    araña_feliz[1] = pygame.transform.scale(araña_feliz[1],(570,380))
    araña_feliz[0] = pygame.transform.rotate(araña_feliz[0],-5)
    araña_feliz[1] = pygame.transform.rotate(araña_feliz[1],-5)
    run=True
    while run:
        ventana.fill((86, 18, 132))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        f_muro+=1
        if(f_muro==60):
            fotograma+=1
            f_muro=0
        if(fotograma==2):
            fotograma=0
        
        ventana.blit(araña_feliz[fotograma],(10,resolucion[1]-475))    
        crear_boton(ventana,continuar,"Continuar",40)
        pygame.display.flip()
Victoria()