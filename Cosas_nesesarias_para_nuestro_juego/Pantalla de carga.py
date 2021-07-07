import pygame,sys,random,os
from pygame import mixer

pygame.init()

def Pantalla_carga(ventana):
    ventana=pygame.display.set_mode([960,800])
    fotograma = 0
    f_muro = 0
    background=pygame.image.load((os.path.dirname(os.path.abspath(__file__))+"\\Background\P_CARGA.png"))
    background = pygame.transform.scale(background,(960,600))
    run=True
    while run:
        ventana.fill((0,0,0))
        ventana.blit(background,[0,100])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        f_muro+=1
        if(f_muro==60):
            fotograma+=1
            f_muro=0
        if(fotograma==2):
            fotograma=0
        pygame.display.flip()