#!/usr/bin/python3

import pygame, os, math

grille = [[0] * 4 for i in
          range(4)]  # grille ou on appliquera les algo stockera seulement les valeurs qui seront dans les rectangles
# la grille est initialisée a 0 partout
mar = 30  # marge des rectangles
cot = 60  # longueur du coté

def choisir_num(x, y): #a suivre --> commande pour ecrire un chiffre
    print(x,y)


def click_inter_grille(grille):  # prend une grille en parametre (tableau n*n)
    if pygame.mouse.get_pressed()[0]:  # renvoie 1 si le le click gauche est activé
        click = pygame.mouse.get_pos()  # on stock les coordonées du click
        if (screen.get_at(click) == color):  # ne fait quelque chose que si l'on a cliqué sur du blanc
            x = math.floor((
                (click[1]/ (cot + mar))-2))  # les coordonées sont inversées quand on passe de la grille a l'interface
            y = math.floor(((click[0]/ (cot + mar))-4))
            grille[x][y] = "X"
            pygame.draw.rect(screen,colorclick, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot,
                                                        cot)) #change de couleur pendant le click


pygame.init()
WINDOW_SIZE = [1080, 720]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Futoshiki")   #titre de la fenetre
Icone = pygame.image.load("assets/icone.jpg")  #lecture de l'icone
pygame.display.set_icon(Icone)   #mettre l'icone
done = False
screen.fill((0, 105, 102))  # met le fond en vert
color = (255, 255, 255)  # couleur que l'on utilise pour les rectangles
colorclick = (255, 255, 35) # couleur quand on click sur un rectangle
imagetitre = pygame.image.load("assets/titreFutoshiki.png").convert_alpha()

while not done:
    screen.blit(imagetitre, (290, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for x in range(4):
        for y in range(4):
            pygame.draw.rect(screen, color, pygame.Rect(x * (cot + mar) + 390, y * (cot + mar) + 200, cot,
                                                        cot))  # dessine la "grille de dimension n"
            # sous formes de n*n rectangles avec une marge "mar"
    click_inter_grille(grille)

    pygame.display.flip()

for element in grille:  # test pour voir sur quels rectangles on a clické
    print(element)
