#!/usr/bin/python3

#############################################################################
#############################################################################
###########################       FUTOSHIKI       ###########################
########      FAIT PAR : Allan, Rayan, Nico, Alexandre et Mattéo      #######
############################     Version 1.0     ############################
#############################################################################
#############################################################################


#############################    IMPORTATIONS    ############################

import pygame, os, math
from pygame.locals import *

#############################    FONCTIONS    ############################

def installe_grille():
    grille_base = [0, 0, 4, 0],[1, 0, 0, 0],[0, 20, 3, 4],[0, 0, 10, 0] #Les unités sont les flèches et les dizaines
    #sont les chiffres de base non modifianble
    fleche_gauche = pygame.image.load("assets/fleche_gauche.png").convert_alpha()  # Lecture des flèches, gauche = 1
    fleche_haut = pygame.image.load("assets/fleche_haut.png").convert_alpha()  # haut = 2
    fleche_droit = pygame.image.load("assets/fleche_droit.png").convert_alpha()  # droite = 3
    fleche_bas = pygame.image.load("assets/fleche_bas.png").convert_alpha()  #bas = 4

    for a in range(difficulte):  #Lecture de la grille de base
        for b in range(difficulte):
            grille[a][b] = 0  #Met les chiffres de base dans la grille
            if (grille_base[a][b] != 0):
                if ((grille_base[a][b] % 10) == 1):  #Placement des flèches
                    screen.blit(fleche_gauche, (b * (cot + mar) + 450, a * (cot + mar) + 200))

                elif ((grille_base[a][b] % 10) == 2):
                    screen.blit(fleche_haut, (b * (cot + mar) + 390, a * (cot + mar) + 260))

                elif ((grille_base[a][b] % 10) == 3):
                    screen.blit(fleche_droit, (b * (cot + mar) + 450, a * (cot + mar) + 200))

                elif ((grille_base[a][b] % 10) == 4):
                    screen.blit(fleche_bas, (b * (cot + mar) + 390, a * (cot + mar) + 260))

                if (grille_base[a][b] > 39): #Placement des chiffres de base
                    pygame.draw.rect(screen, colorbase,
                                     pygame.Rect(b * (cot + mar) + 390, a * (cot + mar) + 200, cot, cot))
                    screen.blit(P4, (b * (cot + mar) + 390, a * (cot + mar) + 200, cot, cot))
                    grille[a][b] = 4

                elif (grille_base[a][b] > 29):
                    pygame.draw.rect(screen, colorbase,
                                     pygame.Rect(b * (cot + mar) + 390, a * (cot + mar) + 200, cot, cot))
                    screen.blit(P3, (b * (cot + mar) + 390, a * (cot + mar) + 200, cot, cot))
                    grille[a][b] = 3

                elif (grille_base[a][b] > 19):
                    pygame.draw.rect(screen, colorbase,
                                     pygame.Rect(b * (cot + mar) + 390, a * (cot + mar) + 200, cot, cot))
                    screen.blit(P2, (b * (cot + mar) + 390, a * (cot + mar) + 200, cot, cot))
                    grille[a][b] = 2

                elif (grille_base[a][b] > 9):
                    pygame.draw.rect(screen, colorbase,
                                     pygame.Rect(b * (cot + mar) + 390, a * (cot + mar) + 200, cot, cot))
                    screen.blit(P1, (b * (cot + mar) + 390, a * (cot + mar) + 200, cot, cot))
                    grille[a][b] = 1

    return grille #Renvoie la grille avec les chiffres de base





def changer_num(): #commande pour ecrire un chiffre cliquée

    if clickable_area_G1.collidepoint(event.pos):
        if (grille[x][y] == 1): #Si le chiffre clique est deja sur la case alors efface la case
            pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            grille[x][y] = 0  # remet la case à 0 dans la matrice
        else:
            pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            screen.blit(P1, (y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            grille[x][y] = 1
            verifie_grille_finie()
            print("1 clické")
    if clickable_area_G2.collidepoint(event.pos):
        if (grille[x][y] == 2): #Si le chiffre clique est deja sur la case alors efface la case
            pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            grille[x][y] = 0  # remet la case à 0 dans la matrice
        else:
            pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            screen.blit(P2, (y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            grille[x][y] = 2
            verifie_grille_finie()
            print("2 clické")
    if clickable_area_G3.collidepoint(event.pos):
        if (grille[x][y] == 3): #Si le chiffre clique est deja sur la case alors efface la case
            pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            grille[x][y] = 0 #remet la case à 0 dans la matrice
        else:
            pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            screen.blit(P3, (y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            grille[x][y] = 3
            verifie_grille_finie()
            print("3 clické")
    if clickable_area_G4.collidepoint(event.pos):
        if (grille[x][y] == 4): #Si le chiffre clique est deja sur la case alors efface la case
            pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            grille[x][y] = 0  # remet la case à 0 dans la matrice
        else:
            pygame.draw.rect(screen, color, pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            screen.blit(P4, (y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            grille[x][y] = 4
            verifie_grille_finie()
            print("4 clické")

def retourne_grille_finie():
    grille_finie = [[2, 1, 3, 4],[3, 4, 2, 1],[1, 2, 4, 3],[4, 3, 1, 2]]
    return grille_finie

def verifie_grille_finie():
    grille_finie = retourne_grille_finie()
    if (grille == grille_finie):
        gagner()

def gagner():
    image_gagner = pygame.image.load("assets/gagner.png").convert_alpha()
    screen.blit(image_gagner, (290, 210))


def click_sur_grille(grille):  #Sert a avoir les coordonnees du click sur la grille
    if pygame.mouse.get_pressed()[0]:  # renvoie 1 si le le click gauche est activé
        click = pygame.mouse.get_pos()  # on stock les coordonées du click
        if (screen.get_at(click) == (color)):  # ne fait quelque chose que si l'on a cliqué sur du blanc
            global x
            global y
            x = math.floor((
                (click[1]/ (cot + mar))-2))  # les coordonées sont inversées quand on passe de la grille a l'interface
            y = math.floor(((click[0]/ (cot + mar))-4))
            change_couleur_case_selec()

def change_couleur_case_selec():
    if event.type == MOUSEBUTTONDOWN:  # a toi de voir si tu veux ne gérer que des clics particuliers
        for a in range(difficulte):  # Remet toutes les cases vide en blanc
            for b in range(difficulte):
                if grille[a][b] == 0:
                    pygame.draw.rect(screen, color, pygame.Rect(b * (cot + mar) + 390, a * (cot + mar) +
                                                                200, cot, cot))
        if grille[x][y] == 0:
            pygame.draw.rect(screen, colorclick,
                             pygame.Rect(y * (cot + mar) + 390, x * (cot + mar) + 200, cot, cot))
            # change de couleur après click


#############################    VARIABLES    ############################

pygame.init()
WINDOW_SIZE = [1080, 720]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Futoshiki")   #titre de la fenetre

grille = [[0] * 4 for i in range(4)]  # grille ou on appliquera les algo stockera seulement les valeurs qui seront dans
# les rectangles
# la grille est initialisée a 0 partout
mar = 30  # marge des rectangles
cot = 60  # longueur du coté


Icone = pygame.image.load("assets/icone.jpg")  #lecture de l'icone
pygame.display.set_icon(Icone)   #mettre l'icone
running = True #Vérifie si la fenetre doit rester ouverte
screen.fill((0, 105, 102))  # met le fond en vert
color = (255, 255, 255)  # couleur que l'on utilise pour les rectangles
colorclick = (255, 255, 35) # couleur quand on click sur un rectangle
colorbase = (170, 170, 170) # couleur des chiffres de base non modifiable
imagetitre = pygame.image.load("assets/titreFutoshiki.png").convert_alpha() #Lecture du titre Futoshiki
difficulte = 4 #taille de grille



G1 = pygame.image.load("assets/G1.png").convert_alpha()  #Lecture des grands numéros cliquable
G2 = pygame.image.load("assets/G2.png").convert_alpha()
G3 = pygame.image.load("assets/G3.png").convert_alpha()
G4 = pygame.image.load("assets/G4.png").convert_alpha()

clickable_area_G1 = pygame.Rect((320, 575), (100, 100))  #Zone cliquable des numéros (comme un bouton)
rect_surf_G1 = pygame.Surface(clickable_area_G1.size)
clickable_area_G2 = pygame.Rect((445, 575), (100, 100))
rect_surf_G2 = pygame.Surface(clickable_area_G2.size)
clickable_area_G3 = pygame.Rect((570, 575), (100, 100))
rect_surf_G3 = pygame.Surface(clickable_area_G3.size)
clickable_area_G4 = pygame.Rect((695, 575), (100, 100))
rect_surf_G4 = pygame.Surface(clickable_area_G4.size)

P1 = pygame.image.load("assets/P1.png").convert_alpha()  #Lecture des petits numéros qui vont sur la grille
P2 = pygame.image.load("assets/P2.png").convert_alpha()
P3 = pygame.image.load("assets/P3.png").convert_alpha()
P4 = pygame.image.load("assets/P4.png").convert_alpha()

for x in range(difficulte):
    for y in range(difficulte):
        pygame.draw.rect(screen, color, pygame.Rect(x * (cot + mar) + 390, y * (cot + mar) + 200, cot,
                                                    cot))  # dessine la "grille de dimension n"
        # sous formes de n*n rectangles avec une marge "mar"

x = -1 #coordonneé de la grille x de la dernière case cliquée
y= -1  #coordonneé de la grille y de la dernière case cliquée
initial=True #pour initialiser qu'une fois la grille
#############################    FENETRE    ############################

while running: #Tant que la fentetre est en cours

    if initial:
        screen.blit(imagetitre, (290, 20))  # Affichage du titre Futoshiki

        screen.blit(G1, (320, 575))  # Affichage des grands numéros cliquable
        screen.blit(G2, (445, 575))
        screen.blit(G3, (570, 575))
        screen.blit(G4, (695, 575))
        grille = installe_grille()
        initial=False


    for event in pygame.event.get(): #Pour chaque evenement
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOUSEBUTTONUP:  # quand je relache le bouton
            if event.button == 1 and x != -1 and y != -1 :  # 1= clique gauche et vérifie qu'une case est été précedement
                changer_num() #Appelle fonction ppour changer les numéros



    click_sur_grille(grille)


    pygame.display.flip()

for element in grille:  #Affichage console de la grille
    print(element)
