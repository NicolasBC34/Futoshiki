    #!/usr/bin/python3

    #############################################################################
    #############################################################################
    ###########################       FUTOSHIKI       ###########################
    ########      FAIT PAR : Allan, Rayan, Nico, Alexandre et Mattéo      #######
    ############################     Version 1.0     ############################
    #############################################################################
    #############################################################################


    #############################    IMPORTATIONS    ############################

import pygame, os, math, json, random
from pygame.locals import *

def def_Futoshiki(difficulte, level, la_grille_base, la_grille_finie):



    #############################    FONCTIONS    ############################

    def retourne_grille_base():
        grille_base = la_grille_base
        return grille_base


    def installe_grille():
        grille = [[0] * difficulte for i in range(difficulte)]
        grille_base = retourne_grille_base()

        # Lecture des flèches,
        # gauche = 0.5, gauche + haut = 2.5, gauche + bas = 3
        # droite = 1.5, droite + haut = 3.5, droite + bas = 4
        # haut = 1
        # bas = 2


        # sont les chiffres de base non modifianble
        fleche_gauche = pygame.image.load("Ressources/assets/fleche_gauche.png").convert_alpha()
        fleche_gauche = pygame.transform.scale(fleche_gauche, (mar, cot))
        fleche_haut = pygame.image.load("Ressources/assets/fleche_haut.png").convert_alpha()
        fleche_haut = pygame.transform.scale(fleche_haut, (cot, mar))
        fleche_droit = pygame.image.load("Ressources/assets/fleche_droit.png").convert_alpha()
        fleche_droit = pygame.transform.scale(fleche_droit, (mar, cot))
        fleche_bas = pygame.image.load("Ressources/assets/fleche_bas.png").convert_alpha()
        fleche_bas = pygame.transform.scale(fleche_bas, (cot, mar))

        for a in range(difficulte):  # Lecture de la grille de base
            for b in range(difficulte):

                grille[a][b] = 0  # Met les chiffres de base dans la grille
                if (grille_base[a][b] != 0):
                    if (((grille_base[a][b] % 10) == 0.5) or ((grille_base[a][b] % 10) == 2.5) or ((grille_base[a][b] % 10) == 3)):  # Placement des flèches
                        screen.blit(fleche_gauche, (b * (cot + mar) + marge_gauche + cot, a * (cot + mar) + marge_haut))

                    if (((grille_base[a][b] % 10) == 1) or ((grille_base[a][b] % 10) == 2.5) or ((grille_base[a][b] % 10) == 3.5)):
                        screen.blit(fleche_haut, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut + cot))

                    if (((grille_base[a][b] % 10) == 1.5) or ((grille_base[a][b] % 10) == 3.5) or ((grille_base[a][b] % 10) == 4)):
                        screen.blit(fleche_droit, (b * (cot + mar) + marge_gauche + cot, a * (cot + mar) + marge_haut))

                    if (((grille_base[a][b] % 10) == 2) or ((grille_base[a][b] % 10) == 3) or ((grille_base[a][b] % 10) == 4)):
                        screen.blit(fleche_bas, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut + cot))

                    if (grille_base[a][b] > 89):  # Placement des chiffres de base
                        pygame.draw.rect(screen, colorbase,
                                        pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        screen.blit(P9, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        grille[a][b] = 9

                    elif (grille_base[a][b] > 79):
                        pygame.draw.rect(screen, colorbase,
                                        pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        screen.blit(P8, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        grille[a][b] = 8

                    elif (grille_base[a][b] > 69):
                        pygame.draw.rect(screen, colorbase,
                                        pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        screen.blit(P7, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        grille[a][b] = 7

                    elif (grille_base[a][b] > 59):
                        pygame.draw.rect(screen, colorbase,
                                        pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        screen.blit(P6, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        grille[a][b] = 6

                    elif (grille_base[a][b] > 49):
                        pygame.draw.rect(screen, colorbase,
                                        pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        screen.blit(P5, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        grille[a][b] = 5

                    elif (grille_base[a][b] > 39):
                        pygame.draw.rect(screen, colorbase,
                                        pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        screen.blit(P4, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        grille[a][b] = 4

                    elif (grille_base[a][b] > 29):
                        pygame.draw.rect(screen, colorbase,
                                        pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        screen.blit(P3, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        grille[a][b] = 3

                    elif (grille_base[a][b] > 19):
                        pygame.draw.rect(screen, colorbase,
                                        pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        screen.blit(P2, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        grille[a][b] = 2

                    elif (grille_base[a][b] > 9):
                        pygame.draw.rect(screen, colorbase,
                                        pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        screen.blit(P1, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                        grille[a][b] = 1

        return grille  # Renvoie la grille avec les chiffres de base


    def verifie_grille_finie(grille, grille_finie):
        return grille == grille_finie


    def gagner():
        image_gagner = pygame.image.load("Ressources/assets/gagner.png").convert_alpha()
        screen.blit(image_gagner, (190, 150))
        gagner = True
        return gagner

    def verifie_2_identiques():
        grille_base = retourne_grille_base()
        for a in range(difficulte):
            for b in range(difficulte):
                for c in range(difficulte):
                    if ((b != c) and ((grille[a][b] != 0) and (grille[b][a] != 0))):
                        if (grille[a][b] == grille[a][c]):
                            if (grille_base[a][b] < 10): #Verifie que ce n'est pas un chiffre non modifiable
                                pygame.draw.rect(screen, colorerreur, pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille_base[a][c] < 10): #Verifie que ce n'est pas un chiffre non modifiable
                                pygame.draw.rect(screen, colorerreur, pygame.Rect(c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            # Réécris le chiffre par dessus la case selectionnée
                            if (grille[a][b] == 1):
                                screen.blit(P1, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P1, (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 2):
                                screen.blit(P2, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P2, (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 3):
                                screen.blit(P3, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P3, (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 4):
                                screen.blit(P4, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P4, (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 5):
                                screen.blit(P5, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P5, (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 6):
                                screen.blit(P6, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P6, (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 7):
                                screen.blit(P7, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P7, (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 8):
                                screen.blit(P8, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P8, (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 9):
                                screen.blit(P9, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P9, (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))


                        if (grille[b][a] == grille[c][a]):
                            if (grille_base[b][a] < 10): #Verifie que ce n'est pas un chiffre non modifiable
                                pygame.draw.rect(screen, colorerreur,
                                            pygame.Rect(a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                            if (grille_base[c][a] < 10): #Verifie que ce n'est pas un chiffre non modifiable
                                pygame.draw.rect(screen, colorerreur,
                                            pygame.Rect(a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            # Réécris le chiffre par dessus la case selectionnée
                            if (grille[b][a] == 1):
                                screen.blit(P1, (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P1, (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] == 2):
                                screen.blit(P2, (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P2, (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] == 3):
                                screen.blit(P3, (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P3, (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] == 4):
                                screen.blit(P4, (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P4, (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] == 5):
                                screen.blit(P5, (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P5, (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] == 6):
                                screen.blit(P6, (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P6, (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] == 7):
                                screen.blit(P7, (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P7, (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] == 8):
                                screen.blit(P8, (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P8, (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] == 9):
                                screen.blit(P9, (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P9, (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))

    def change_couleur_case_selec(x, y):
        grille_base = retourne_grille_base()
        if event.type == MOUSEBUTTONDOWN:  # a toi de voir si tu veux ne gérer que des clics particuliers
            for a in range(difficulte):  # Remet toutes les cases vide en blanc
                for b in range(difficulte):
                    if (((a != x) or (b != y)) and (grille_base[a][b] < 9)): #Vérifie que la case est ni selectionnée
                        #ni une case de base
                        pygame.draw.rect(screen, color, pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) +
                                                                    marge_haut, cot, cot)) #Remet les cases en blanc
                        if (grille[a][b] != 0): #Réécris le chiffre par dessus
                            if (grille[a][b] == 1):
                                screen.blit(P1, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 2):
                                screen.blit(P2, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 3):
                                screen.blit(P3, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 4):
                                screen.blit(P4, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 5):
                                screen.blit(P5, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 6):
                                screen.blit(P6, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 6):
                                screen.blit(P6, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 7):
                                screen.blit(P7, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 8):
                                screen.blit(P8, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] == 9):
                                screen.blit(P9, (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))

            verifie_2_identiques()
            pygame.draw.rect(screen, colorclick, pygame.Rect(y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
            if (grille[x][y] != 0):  # Réécris le chiffre par dessus la case selectionnée
                if (grille[x][y] == 1):
                    screen.blit(P1, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] == 2):
                    screen.blit(P2, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] == 3):
                    screen.blit(P3, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] == 4):
                    screen.blit(P4, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] == 5):
                    screen.blit(P5, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] == 6):
                    screen.blit(P6, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] == 6):
                    screen.blit(P6, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] == 7):
                    screen.blit(P7, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] == 8):
                    screen.blit(P8, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] == 9):
                    screen.blit(P9, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))




    def changer_num(X, Y):  # commande pour ecrire un chiffre cliquée
        if clickable_area_G1.collidepoint(event.pos):
            if (grille[X][Y] == 1):  # Si le chiffre clique est deja sur la case alors efface la case
                pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 0  # remet la case à 0 dans la matrice

            else:
                pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P1, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 1

        elif clickable_area_G2.collidepoint(event.pos):
            if (grille[X][Y] == 2):  # Si le chiffre clique est deja sur la case alors efface la case
                pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 0  # remet la case à 0 dans la matrice
            else:
                pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P2, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 2
        elif clickable_area_G3.collidepoint(event.pos):
            if (grille[X][Y] == 3):  # Si le chiffre clique est deja sur la case alors efface la case
                pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 0  # remet la case à 0 dans la matrice
            else:
                pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P3, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 3
        elif clickable_area_G4.collidepoint(event.pos):
            if (grille[X][Y] == 4):  # Si le chiffre clique est deja sur la case alors efface la case
                pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 0  # remet la case à 0 dans la matrice
            else:
                pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P4, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 4
        if (difficulte >= 5):
            if clickable_area_G5.collidepoint(event.pos):
                if (grille[X][Y] == 5):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 0  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    screen.blit(P5, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 5
        if (difficulte >= 6):
            if clickable_area_G6.collidepoint(event.pos):
                if (grille[X][Y] == 6):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 0  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    screen.blit(P6, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 6
        if (difficulte >= 7):
            if clickable_area_G7.collidepoint(event.pos):
                if (grille[X][Y] == 7):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 0  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    screen.blit(P7, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 7
        if (difficulte >= 8):
            if clickable_area_G8.collidepoint(event.pos):
                if (grille[X][Y] == 8):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 0  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    screen.blit(P8, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 8
        if (difficulte >= 9):
            if clickable_area_G9.collidepoint(event.pos):
                if (grille[X][Y] == 9):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 0  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick, pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    screen.blit(P9, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = 9



    def click_sur_grille(grille, grille_rectangles):  # Sert a avoir les coordonnees du click sur la grille
        grille_base = retourne_grille_base()
        for i in range(difficulte):  # on cherche sur quel rectangle on a cliqué
            for j in range(difficulte):
                if (grille_rectangles[i][j].collidepoint(
                        event.pos) and (grille_base[j][i] < 9)):  # rectangle trouvé, on renvoie ses coordonées dans la grille
                    x = math.floor(((event.pos[1] - 150) / (cot + mar))) #
                    # les coordonées sont inversées quand on passe de la grille a l'interface
                    y = math.floor((event.pos[0] - marge_gauche) / (cot + mar))
                    change_couleur_case_selec(x, y)
                    co = (x, y)  # renvoie les coordonées a la place de les passer en variable globale
                    return co
        return 0

    def afficher_indice():
        fait = False
        liste_case_vide = []
        nombre_case_vide = 0
        for X in range(difficulte):
            for Y in range(difficulte):
                if (grille[X][Y] == 0):
                    liste_case_vide.append(X)
                    liste_case_vide.append(Y)
                    nombre_case_vide = nombre_case_vide + 1
        if (nombre_case_vide != 0):
            case_selec = random.randint(1 , nombre_case_vide)
            X = liste_case_vide[((case_selec * 2) - 2)]
            Y = liste_case_vide[((case_selec * 2) - 1)]
            indice = grille_finie[X][Y]

            if (indice == 1):
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P1, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 1
            elif (indice == 2):
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P2, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 2
            elif (indice == 3):
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P3, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 3
            elif (indice == 4):
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P4, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 4
            elif (indice == 5):
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P5, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 5
            elif (indice == 6):
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P6, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 6
            elif (indice == 7):
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P7, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 7
            elif (indice == 8):
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P8, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 8
            elif (indice == 9):
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P9, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = 9







    #############################    VARIABLES    ############################
    pygame.init()
    WINDOW_SIZE = [1080, 720]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = (0, 105, 102)
    pygame.display.set_caption("Futoshiki")  # titre de la fenetre

    # grille ou on appliquera les algo
    # la grille est initialisée a 0 partout
    grille_rectangles = [[0] * difficulte for i in
                        range(difficulte)]  # grille interface (correspond aux rectangles qui sont des zones cliquables)

    grille_finie = la_grille_finie

    mar = int((((WINDOW_SIZE[1] * 0.8) / difficulte) / 3)) # marge des rectangles
    cot = int((((WINDOW_SIZE[1] * 0.8) / difficulte) / 3 * 2))
    marge_haut = 150
    marge_gauche = ((WINDOW_SIZE[0] - (difficulte * (cot + mar) - mar)) / 2)

    Icone = pygame.image.load("Ressources/assets/icone.jpg")  # lecture de l'icone
    pygame.display.set_icon(Icone)  # mettre l'icone
    running = True  # Vérifie si la fenetre doit rester ouverte
    screen.fill(background)  # met le fond en vert
    color = (255, 255, 255)  # couleur que l'on utilise pour les rectangles
    colorerreur = (255, 0, 0) #Couleur quand deux chiffres sont identiques sur la même ligne
    colorclick = (255, 255, 35)  # couleur quand on click sur un rectangle
    colorbase = (170, 170, 170)  # couleur des chiffres de base non modifiables

    # Chargement des polices
    titleFont = pygame.font.Font("Ressources/go3v2.ttf", 100)  
    subMenuFont = pygame.font.Font("Ressources/go3v2.ttf", 60)

    #chargement assets, zones cliquables et affichage écran
    G1 = pygame.image.load("Ressources/assets/G1.png").convert_alpha() 
    G2 = pygame.image.load("Ressources/assets/G2.png").convert_alpha()
    G3 = pygame.image.load("Ressources/assets/G3.png").convert_alpha()
    G4 = pygame.image.load("Ressources/assets/G4.png").convert_alpha()
    G5 = pygame.image.load("Ressources/assets/G5.png").convert_alpha()
    G6 = pygame.image.load("Ressources/assets/G6.png").convert_alpha()
    G7 = pygame.image.load("Ressources/assets/G7.png").convert_alpha()
    G8 = pygame.image.load("Ressources/assets/G8.png").convert_alpha()
    G9 = pygame.image.load("Ressources/assets/G9.png").convert_alpha()

    if (difficulte == 4):
        screen.blit(G1, (892, 150))  # Affichage des grands numéros cliquable
        clickable_area_G1 = pygame.Rect((892, 150), (100, 100))
        screen.blit(G2, (892, 292))
        clickable_area_G2 = pygame.Rect((892, 292), (100, 100))
        screen.blit(G3, (892, 435))
        clickable_area_G3 = pygame.Rect((892, 435), (100, 100))
        screen.blit(G4, (892, 577))
        clickable_area_G4 = pygame.Rect((892, 577), (100, 100))
    if (difficulte == 5):
        screen.blit(G1, (829, 239))  # Affichage des grands numéros cliquable
        clickable_area_G1 = pygame.Rect((829, 239), (100, 100))
        screen.blit(G2, (954, 239))
        clickable_area_G2 = pygame.Rect((954, 239), (100, 100))
        screen.blit(G3, (829, 364))
        clickable_area_G3 = pygame.Rect((829, 364), (100, 100))
        screen.blit(G4, (954, 364))
        clickable_area_G4 = pygame.Rect((954, 364), (100, 100))
        screen.blit(G5, (891, 489))
        clickable_area_G5 = pygame.Rect((891, 489), (100, 100))
    if (difficulte == 6):
        screen.blit(G1, (829, 239))  # Affichage des grands numéros cliquable
        clickable_area_G1 = pygame.Rect((829, 239), (100, 100))
        screen.blit(G2, (954, 239))
        clickable_area_G2 = pygame.Rect((954, 239), (100, 100))
        screen.blit(G3, (829, 364))
        clickable_area_G3 = pygame.Rect((829, 364), (100, 100))
        screen.blit(G4, (954, 364))
        clickable_area_G4 = pygame.Rect((954, 364), (100, 100))
        screen.blit(G5, (829, 489))
        clickable_area_G5 = pygame.Rect((829, 489), (100, 100))
        screen.blit(G6, (954, 489))
        clickable_area_G6 = pygame.Rect((954, 489), (100, 100))
    if (difficulte == 7):
        screen.blit(G1, (829, 176))  # Affichage des grands numéros cliquable
        clickable_area_G1 = pygame.Rect((829, 176), (100, 100))
        screen.blit(G2, (954, 176))
        clickable_area_G2 = pygame.Rect((954, 176), (100, 100))
        screen.blit(G3, (829, 301))
        clickable_area_G3 = pygame.Rect((829, 301), (100, 100))
        screen.blit(G4, (954, 301))
        clickable_area_G4 = pygame.Rect((954, 301), (100, 100))
        screen.blit(G5, (829, 426))
        clickable_area_G5 = pygame.Rect((829, 426), (100, 100))
        screen.blit(G6, (954, 426))
        clickable_area_G6 = pygame.Rect((954, 426), (100, 100))
        screen.blit(G7, (891, 551))
        clickable_area_G7 = pygame.Rect((891, 551), (100, 100))
    if (difficulte == 8):
        screen.blit(G1, (829, 176))  # Affichage des grands numéros cliquable
        clickable_area_G1 = pygame.Rect((829, 176), (100, 100))
        screen.blit(G2, (954, 176))
        clickable_area_G2 = pygame.Rect((954, 176), (100, 100))
        screen.blit(G3, (829, 301))
        clickable_area_G3 = pygame.Rect((829, 301), (100, 100))
        screen.blit(G4, (954, 301))
        clickable_area_G4 = pygame.Rect((954, 301), (100, 100))
        screen.blit(G5, (829, 426))
        clickable_area_G5 = pygame.Rect((829, 426), (100, 100))
        screen.blit(G6, (954, 426))
        clickable_area_G6 = pygame.Rect((954, 426), (100, 100))
        screen.blit(G7, (829, 551))
        clickable_area_G7 = pygame.Rect((829, 551), (100, 100))
        screen.blit(G8, (954, 551))
        clickable_area_G8 = pygame.Rect((954, 551), (100, 100))
    if (difficulte == 9):
        screen.blit(G1, (829, 110))  # Affichage des grands numéros cliquable
        clickable_area_G1 = pygame.Rect((829, 110), (100, 100))
        screen.blit(G2, (954, 110))
        clickable_area_G2 = pygame.Rect((954, 110), (100, 100))
        screen.blit(G3, (829, 235))
        clickable_area_G3 = pygame.Rect((829, 235), (100, 100))
        screen.blit(G4, (954, 235))
        clickable_area_G4 = pygame.Rect((954, 235), (100, 100))
        screen.blit(G5, (829, 360))
        clickable_area_G5 = pygame.Rect((829, 360), (100, 100))
        screen.blit(G6, (954, 360))
        clickable_area_G6 = pygame.Rect((954, 360), (100, 100))
        screen.blit(G7, (829, 485))
        clickable_area_G7 = pygame.Rect((829, 485), (100, 100))
        screen.blit(G8, (954, 485))
        clickable_area_G8 = pygame.Rect((954, 485), (100, 100))
        screen.blit(G9, (891, 610))
        clickable_area_G9 = pygame.Rect((891, 610), (100, 100))

    P1 = pygame.image.load("Ressources/assets/P1.png").convert_alpha() 
    P1 = pygame.transform.scale(P1, (cot, cot))
    P2 = pygame.image.load("Ressources/assets/P2.png").convert_alpha()
    P2 = pygame.transform.scale(P2, (cot, cot))
    P3 = pygame.image.load("Ressources/assets/P3.png").convert_alpha()
    P3 = pygame.transform.scale(P3, (cot, cot))
    P4 = pygame.image.load("Ressources/assets/P4.png").convert_alpha()
    P4 = pygame.transform.scale(P4, (cot, cot))
    P5 = pygame.image.load("Ressources/assets/P5.png").convert_alpha()
    P5 = pygame.transform.scale(P5, (cot, cot))
    P6 = pygame.image.load("Ressources/assets/P6.png").convert_alpha()
    P6 = pygame.transform.scale(P6, (cot, cot))
    P7 = pygame.image.load("Ressources/assets/P7.png").convert_alpha()
    P7 = pygame.transform.scale(P7, (cot, cot))
    P8 = pygame.image.load("Ressources/assets/P8.png").convert_alpha()
    P8 = pygame.transform.scale(P8, (cot, cot))
    P9 = pygame.image.load("Ressources/assets/P9.png").convert_alpha()
    P9 = pygame.transform.scale(P9, (cot, cot))

    clickable_area_retour = pygame.Rect((10, 650), (240, 50))
    clickable_area_indice = pygame.Rect((10, 400), (240, 50))

    #affichage écran des polices
    screen.blit(subMenuFont.render("Retour", True, (0, 0, 0)), (10, 650))
    screen.blit(subMenuFont.render("Indice", True, (0, 0, 0)), (10, 400))
    screen.blit(titleFont.render("Futoshiki", True, (0, 0, 0)), (330, 30))

    for x in range(difficulte):
        for y in range(difficulte):
            rect = pygame.draw.rect(screen, color, pygame.Rect(x * (cot + mar) + marge_gauche, y * (cot + mar) + marge_haut, cot,
                                                            cot))  # dessine la "grille de dimension n"
            grille_rectangles[x][y] = rect

    X = -1 #coordonneé de la grille x de la dernière case cliquée
    Y = -1  #coordonneé de la grille y de la dernière case cliquée
    clicked = True
    grille = installe_grille()

    # clock settings
    
    clock = pygame.time.Clock()
    minutes = 0
    seconds = 0
    text = '0:00'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    timerfont = pygame.font.Font("Ressources/go3v2.ttf", 90)
    timeLabelFont = pygame.font.Font("Ressources/go3v2.ttf", 30)
    screen.blit(timeLabelFont.render("TEMPS", True, (0, 0, 0)), (85, 150))  
    recorded = False
   
    #############################    MAIN    ############################

    while running:  # Tant que la fentetre est en cours

        for event in pygame.event.get():  # Pour chaque evenement
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if (event.type == MOUSEBUTTONDOWN and clicked):
                clicked = False
                if (click_sur_grille(grille, grille_rectangles)):
                    X = click_sur_grille(grille, grille_rectangles)[0]
                    Y = click_sur_grille(grille, grille_rectangles)[1]
                if (X != -1):
                    changer_num(X, Y)
                if clickable_area_retour.collidepoint(event.pos):
                    from main import menuLevels
                    menuLevels(screen, difficulte)
                if clickable_area_indice.collidepoint(event.pos):
                    afficher_indice()

            if event.type == MOUSEBUTTONUP:  # besoin de cette condition pour triter les clicks 1 a 1
                clicked = True

            if event.type == USEREVENT: # permet de gérer le timer
                if (not recorded): # tant que la partie n'est pas finie on fait tourner le timer
                    seconds += 1
                    if seconds == 60:
                        seconds = 0
                        minutes += 1
                    str_mintes = str(minutes)
                    str_seconds = str(seconds) if seconds > 9 else "0" + str(seconds)
                    text = str_mintes + ":" + str_seconds

                    pygame.draw.rect(screen, background, (50,180, 200, 100))
                    screen.blit(timerfont.render(text, True, (0, 0, 0)), (50, 180))
                    clock.tick(60)

            if (verifie_grille_finie(grille, grille_finie)):
                # on enregistre le score
                diff_key = str(difficulte) + "x" + str(difficulte)
                level_key = "level" + str(level)

                if (not recorded):
                    with open('scores.json', 'r') as scoresfile: # ouverture du fichier en lecture pour en retouner son contenu
                        data = json.load(scoresfile)
                        score = (minutes * 60) + seconds
                        

                    if len(data[diff_key][level_key]) == 10:
                        if data[diff_key][level_key][9] > score:
                            data[diff_key][level_key].remove(data[diff_key][level_key][9])
                            data[diff_key][level_key].append(score)
                            data[diff_key][level_key].sort()
                    else:
                        data[diff_key][level_key].append(score)
                        data[diff_key][level_key].sort()
                    

                    with open('scores.json', 'w') as scoresfile:
                        json.dump(data, scoresfile, indent=4)

                    recorded = True

                gagner()

        pygame.display.flip()

    for element in grille:  # Affichage console de la grille
        print(element)
