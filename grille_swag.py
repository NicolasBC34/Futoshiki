#!/usr/bin/python3

import pygame,os,math

grille=[[0]*4 for i in range(4)]    #grille ou on appliquera les algo stockera seulement les valeurs qui seront dans les rectangles 
                                    #la grille est initialisée a 0 partout
mar=30      #marge et longueur du coté des rectangles
cot=60  

def click_inter_grille(grille):                     #prend une grille en parametre (tableau n*n)
    if pygame.mouse.get_pressed()[0]:               #renvoie 1 si le le click gauche est activé
        click=pygame.mouse.get_pos()                #on stock les coordonées du click
        if (screen.get_at(click)==color):           #ne fait quelque chose que si l'on a cliqué sur du blanc
            x=math.floor((click[1]/(cot+mar)))      #les coordonées sont inversées quand on passe de la grille a l'interface
            y=math.floor((click[0]/(cot+mar)))
            grille[x][y]="X"

pygame.init()
WINDOW_SIZE=[500,500]
screen=pygame.display.set_mode(WINDOW_SIZE)
done=False
screen.fill((0,0,0)) #met le fond en noir
color=(255,255,255) #couleur que l'on utilise pour les rectangles
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    for x in range(4):
        for y in range(4):
            pygame.draw.rect(screen,color,pygame.Rect(x*(cot+mar),y*(cot+mar),cot,cot)) #dessine la "grille de dimension n" 
                                                                                        #sous formes de n*n rectangles avec une marge "mar"
    click_inter_grille(grille)
            
    pygame.display.flip()

for element in grille:      #test pour voir sur quels rectangles on a clické
    print(element)