import pygame,sys,random
from Funciones import *

pygame.init()

#ventana
resolucion=[960,800]
ventana=pygame.display.set_mode(resolucion)
fondo=pygame.image.load("space.jpg").convert()
fondo=pygame.transform.scale(fondo,resolucion)

#colores
blanco=[255,255,255]
negro=[0,0,0]
rojo=[255,0,0]
verde=[0,255,0]
azul=[0,0,255]

jugar=pygame.Rect(resolucion[0]/2-75,resolucion[1]/4-25,150,50)
opciones=pygame.Rect(resolucion[0]/2-75,resolucion[1]/4+50,150,50)
extras=pygame.Rect(resolucion[0]/2-75,resolucion[1]/4+125,150,50)
salir=pygame.Rect(resolucion[0]/2-75,resolucion[1]/4+200,150,50)

run=True
while run:
    
    ventana.fill(negro)
    ventana.blit(fondo,[0,0])
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and jugar.collidepoint(pygame.mouse.get_pos()):
            ejecucion_juego(ventana)
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and opciones.collidepoint(pygame.mouse.get_pos()):
            print("click2")
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and extras.collidepoint(pygame.mouse.get_pos()):
            print("click3")
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and salir.collidepoint(pygame.mouse.get_pos()):
            run=False
            
    #dibujar pantalla
    crear_boton(ventana,jugar,"Jugar")
    crear_boton(ventana,opciones,"Opciones")
    crear_boton(ventana,extras,"Extras")
    crear_boton(ventana,salir,"Salir")
    

    
    pygame.display.flip()