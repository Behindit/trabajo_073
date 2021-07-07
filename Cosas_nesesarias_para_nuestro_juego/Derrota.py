import pygame,sys,random
from Funciones import *
from Funciones_enemigos import *

pygame.init()

def crear_boton(pantalla,boton,texto,tamaño):
    fuente1=pygame.font.SysFont("Times New Roman",tamaño)
    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(pantalla,[225, 38, 180],boton,0)
    else:
        pygame.draw.rect(pantalla,[174, 15, 135],boton,0)
    ren=fuente1.render(texto,True,(255,255,255))
    pantalla.blit(ren,(boton.x+(boton.width-ren.get_width())/2,boton.y+(boton.height-ren.get_height())/2))

def Derrota(ventana):
    fotograma = 0
    f_muro = 0
    continuar=pygame.Rect(960-200,800-100,170,70)
    
    pygame.mixer.music.load(os.path.dirname(os.path.abspath(__file__))+"\\Musica/DERROTA.wav")
    pygame.mixer.music.play(1,0.0)
    pygame.mixer.music.set_volume(0.08)

    pokemon = [pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/SQ_L.png").convert_alpha()
                ,pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/SQ_R.png").convert_alpha()]
    pokemon[0] = pygame.transform.scale(pokemon[0],(252,249))
    pokemon[1] = pygame.transform.scale(pokemon[1],(252,249))
    pokemon[0] = pygame.transform.rotate(pokemon[0],-5)
    pokemon[1] = pygame.transform.rotate(pokemon[1],-5)

    ranita = [pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Frog_L.png").convert_alpha()
                ,pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Frog_R.png").convert_alpha()]
    ranita[0] = pygame.transform.scale(ranita[0],(252,249))
    ranita[1] = pygame.transform.scale(ranita[1],(252,249))
    ranita[0] = pygame.transform.rotate(ranita[0],-5)
    ranita[1] = pygame.transform.rotate(ranita[1],-5)
    run=True
    while run:
        ventana.fill((64, 56, 58))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and continuar.collidepoint(pygame.mouse.get_pos()):
                run=False
        f_muro+=1
        if(f_muro==60):
            fotograma+=1
            f_muro=0
        if(fotograma==2):
            fotograma=0
        
        ventana.blit(pokemon[fotograma],(10,800-300))    
        ventana.blit(ranita[fotograma],(310,800-300))  
        crear_boton(ventana,continuar,"Continuar",40)
        pygame.display.flip()