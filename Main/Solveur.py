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


def def_Solveur(difficulte):
    #############################    FONCTIONS    ############################

    def verifie_2_identiques():
        for a in range(difficulte):
            for b in range(difficulte):
                for c in range(difficulte):
                    if ((b != c) and ((grille[a][b] != 0) and (grille[b][a] != 0))):
                        if (grille[a][b] / 10 == grille[a][c] / 10 ):
                            # Réécris le chiffre par dessus la case selectionnée
                            if (grille[a][b] / 10 == 1):
                                screen.blit(P1,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P1,
                                            (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] / 10 == 2):
                                screen.blit(P2,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P2,
                                            (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] / 10 == 3):
                                screen.blit(P3,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P3,
                                            (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] / 10 == 4):
                                screen.blit(P4,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P4,
                                            (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] / 10 == 5):
                                screen.blit(P5,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P5,
                                            (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] / 10 == 6):
                                screen.blit(P6,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P6,
                                            (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] / 10 == 7):
                                screen.blit(P7,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P7,
                                            (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] / 10 == 8):
                                screen.blit(P8,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P8,
                                            (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] / 10 == 9):
                                screen.blit(P9,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P9,
                                            (c * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))

                        if (grille[b][a] / 10 == grille[c][a]/ 10):
                            # Réécris le chiffre par dessus la case selectionnée
                            if (grille[b][a] / 10 == 1):
                                screen.blit(P1,
                                            (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P1,
                                            (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] / 10 == 2):
                                screen.blit(P2,
                                            (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P2,
                                            (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] / 10 == 3):
                                screen.blit(P3,
                                            (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P3,
                                            (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] / 10 == 4):
                                screen.blit(P4,
                                            (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P4,
                                            (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] / 10 == 5):
                                screen.blit(P5,
                                            (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P5,
                                            (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] / 10 == 6):
                                screen.blit(P6,
                                            (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P6,
                                            (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] / 10 == 7):
                                screen.blit(P7,
                                            (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P7,
                                            (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] / 10 == 8):
                                screen.blit(P8,
                                            (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P8,
                                            (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))
                            if (grille[b][a] / 10 == 9):
                                screen.blit(P9,
                                            (a * (cot + mar) + marge_gauche, b * (cot + mar) + marge_haut, cot, cot))
                                screen.blit(P9,
                                            (a * (cot + mar) + marge_gauche, c * (cot + mar) + marge_haut, cot, cot))

    def change_couleur_case_selec_fleche(x, y):
        if event.type == MOUSEBUTTONDOWN:
            if y % 2 == 0:
                pygame.draw.rect(screen, colorclickfleche,
                                 pygame.Rect(cot + x * (cot + mar) + marge_gauche,
                                             (y / 2) * (cot + mar) + marge_haut,
                                             cot / 2,
                                             cot))
            if y % 2 == 1:
                pygame.draw.rect(screen, colorclickfleche,
                                 pygame.Rect(x * (cot + mar) + marge_gauche,
                                             mar /2 + (y / 2) * (cot + mar) + marge_haut,
                                             cot,
                                             cot / 2))


    def change_couleur_case_selec(x, y):
        if event.type == MOUSEBUTTONDOWN:  # a toi de voir si tu veux ne gérer que des clics particuliers
            for a in range(difficulte):  # Remet toutes les cases vide en blanc
                for b in range(difficulte):
                    if (((a != x) or (b != y))):  # Vérifie que la case n'est pas selectionnée
                        # ni une case de base
                        pygame.draw.rect(screen, color, pygame.Rect(b * (cot + mar) + marge_gauche, a * (cot + mar) +
                                                                    marge_haut, cot, cot))  # Remet les cases en blanc
                        if (grille[a][b] != 0):  # Réécris le chiffre par dessus
                            if (grille[a][b] - (grille[a][b] % 10) == 10):
                                screen.blit(P1,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] - (grille[a][b] % 10) == 20):
                                screen.blit(P2,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] - (grille[a][b] % 10) == 30):
                                screen.blit(P3,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] - (grille[a][b] % 10) == 40):
                                screen.blit(P4,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] - (grille[a][b] % 10) == 50):
                                screen.blit(P5,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] - (grille[a][b] % 10) == 60):
                                screen.blit(P6,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] - (grille[a][b] % 10) == 70):
                                screen.blit(P7,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] - (grille[a][b] % 10) == 80):
                                screen.blit(P8,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))
                            if (grille[a][b] - (grille[a][b] % 10) == 90):
                                screen.blit(P9,
                                            (b * (cot + mar) + marge_gauche, a * (cot + mar) + marge_haut, cot, cot))

            verifie_2_identiques()
            pygame.draw.rect(screen, colorclick,
                             pygame.Rect(y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
            if (grille[x][y] != 0):  # Réécris le chiffre par dessus la case selectionnée
                if (grille[x][y] - (grille[x][y] % 10) == 10):
                    screen.blit(P1, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] - (grille[x][y] % 10) == 20):
                    screen.blit(P2, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] - (grille[x][y] % 10) == 30):
                    screen.blit(P3, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] - (grille[x][y] % 10) == 40):
                    screen.blit(P4, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] - (grille[x][y] % 10) == 50):
                    screen.blit(P5, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] - (grille[x][y] % 10) == 60):
                    screen.blit(P6, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] - (grille[x][y] % 10) == 70):
                    screen.blit(P7, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] - (grille[x][y] % 10) == 80):
                    screen.blit(P8, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))
                if (grille[x][y] - (grille[x][y] % 10) == 90):
                    screen.blit(P9, (y * (cot + mar) + marge_gauche, x * (cot + mar) + marge_haut, cot, cot))

    # Lecture des flèches,
    # gauche = 0.5, gauche + haut = 2.5, gauche + bas = 3
    # droite = 1.5, droite + haut = 3.5, droite + bas = 4
    # haut = 1
    # bas = 2
    def changer_fleche(x, y):
        if y % 2 == 0:
            a = int(y/2)
            b = x
        if y % 2 == 1:
            if y == 1:
                a = 0
            else:
                a = int((y+1) / 2 - 1)
            b = x

        if clickable_area_fleche_bas.collidepoint(event.pos):
            if y % 2 == 1:
                if (grille[a][b] % 10 == 3 or grille[a][b] % 10 == 4 or grille[a][
                    b] % 10 == 2):  # Si la fleche est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclickfleche,
                                     pygame.Rect(x * (cot + mar) + marge_gauche,
                                                 mar / 2 + (y / 2) * (cot + mar) + marge_haut,
                                                 cot,
                                                 cot / 2))
                    if (grille[a][b] % 10 == 2):
                        grille[a][b] = grille[a][b] - 2
                    if (grille[a][b] % 10 == 3):
                        grille[a][b] = grille[a][b] - 1
                    if (grille[a][b] % 10 == 4):
                        grille[a][b] = grille[a][b] - 2

                else:
                    pygame.draw.rect(screen, colorclickfleche,
                                     pygame.Rect(x * (cot + mar) + marge_gauche,
                                                 mar / 2 + (y / 2) * (cot + mar) + marge_haut,
                                                 cot,
                                                 cot / 2))
                    screen.blit(fleche_bas, (x * (cot + mar) + marge_gauche,
                                             mar / 2 + (y / 2) * (cot + mar) + marge_haut, cot, (cot / 2)))
                    if (grille[a][b] % 10 == 0):
                        grille[a][b] = grille[a][b] + 2
                    if (grille[a][b] % 10 == 0.5):
                        grille[a][b] = grille[a][b] + 2.5
                    if (grille[a][b] % 10 == 1):
                        grille[a][b] = grille[a][b] + 1
                    if (grille[a][b] % 10 == 1.5):
                        grille[a][b] = grille[a][b] + 2.5
                    if (grille[a][b] % 10 == 2.5):
                        grille[a][b] = grille[a][b] + 0.5
                    if (grille[a][b] % 10 == 3.5):
                        grille[a][b] = grille[a][b] + 0.5

        if clickable_area_fleche_haut.collidepoint(event.pos):
            if y % 2 == 1:
                if (grille[a][b] % 10 == 1 or grille[a][b] % 10 == 2.5 or grille[a][b] % 10 == 3.5):
                    # Si la fleche est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclickfleche,
                                     pygame.Rect(x * (cot + mar) + marge_gauche,
                                                 mar / 2 + (y / 2) * (cot + mar) + marge_haut,
                                                 cot,
                                                 cot / 2))
                    if (grille[a][b] % 10 == 1):
                        grille[a][b] = grille[a][b] - 1
                    if (grille[a][b] % 10 == 2.5):
                        grille[a][b] = grille[a][b] - 2
                    if (grille[a][b] % 10 == 3.5):
                        grille[a][b] = grille[a][b] - 2

                else:
                    pygame.draw.rect(screen, colorclickfleche,
                                     pygame.Rect(x * (cot + mar) + marge_gauche,
                                                 mar / 2 + (y / 2) * (cot + mar) + marge_haut,
                                                 cot,
                                                 cot / 2))
                    screen.blit(fleche_haut, (x * (cot + mar) + marge_gauche,
                                             mar / 2 + (y / 2) * (cot + mar) + marge_haut, cot, (cot / 2)))
                    if (grille[a][b] % 10 == 0):
                        grille[a][b] = grille[a][b] + 1
                    if (grille[a][b] % 10 == 0.5):
                        grille[a][b] = grille[a][b] + 2
                    if (grille[a][b] % 10 == 1.5):
                        grille[a][b] = grille[a][b] + 2
                    if (grille[a][b] % 10 == 2):
                        grille[a][b] = grille[a][b] - 1
                    if (grille[a][b] % 10 == 3):
                        grille[a][b] = grille[a][b] - 0.5
                    if (grille[a][b] % 10 == 4):
                        grille[a][b] = grille[a][b] - 0.5

        if clickable_area_fleche_gauche.collidepoint(event.pos):
            if y % 2 == 0:
                if (grille[a][b] % 10 == 0.5 or grille[a][b] % 10 == 2.5 or grille[a][
                    b] % 10 == 3):  # Si la fleche est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclickfleche,
                                     pygame.Rect(cot + x * (cot + mar) + marge_gauche,
                                             (y / 2) * (cot + mar) + marge_haut,
                                             cot / 2,
                                             cot))
                    if (grille[a][b] % 10 == 0.5):
                        grille[a][b] = grille[a][b] - 0.5
                    if (grille[a][b] % 10 == 2.5):
                        grille[a][b] = grille[a][b] - 1.5
                    if (grille[a][b] % 10 == 3):
                        grille[a][b] = grille[a][b] - 1

                else:
                    pygame.draw.rect(screen, colorclickfleche,
                                     pygame.Rect(cot + x * (cot + mar) + marge_gauche,
                                             (y / 2) * (cot + mar) + marge_haut,
                                             cot / 2,
                                             cot))
                    screen.blit(fleche_gauche, (cot + x * (cot + mar) + marge_gauche,
                                             (y / 2) * (cot + mar) + marge_haut,
                                             cot / 2,
                                             cot))
                    if (grille[a][b] % 10 == 0):
                        grille[a][b] = grille[a][b] + 0.5
                    if (grille[a][b] % 10 == 1):
                        grille[a][b] = grille[a][b] + 1.5
                    if (grille[a][b] % 10 == 1.5):
                        grille[a][b] = grille[a][b] - 1
                    if (grille[a][b] % 10 == 2):
                        grille[a][b] = grille[a][b] + 1
                    if (grille[a][b] % 10 == 3.5):
                        grille[a][b] = grille[a][b] - 1
                    if (grille[a][b] % 10 == 4):
                        grille[a][b] = grille[a][b] - 1

        if clickable_area_fleche_droit.collidepoint(event.pos):
            if y % 2 == 0:
                if (grille[a][b] % 10 == 1.5 or grille[a][b] % 10 == 3.5 or grille[a][b] % 10 == 4):
                    # Si la fleche est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclickfleche,
                                     pygame.Rect(cot + x * (cot + mar) + marge_gauche,
                                             (y / 2) * (cot + mar) + marge_haut,
                                             cot / 2,
                                             cot))
                    if (grille[a][b] % 10 == 1.5):
                        grille[a][b] = grille[a][b] - 1.5
                    if (grille[a][b] % 10 == 3.5):
                        grille[a][b] = grille[a][b] - 2.5
                    if (grille[a][b] % 10 == 4):
                        grille[a][b] = grille[a][b] - 2
                        # Lecture des flèches,
                        # gauche = 0.5, gauche + haut = 2.5, gauche + bas = 3
                        # droite = 1.5, droite + haut = 3.5, droite + bas = 4
                        # haut = 1
                        # bas = 2

                else:
                    pygame.draw.rect(screen, colorclickfleche,
                                     pygame.Rect(cot + x * (cot + mar) + marge_gauche,
                                             (y / 2) * (cot + mar) + marge_haut,
                                             cot / 2,
                                             cot))
                    screen.blit(fleche_droit, (cot + x * (cot + mar) + marge_gauche,
                                             (y / 2) * (cot + mar) + marge_haut,
                                             cot / 2,
                                             cot))
                    if (grille[a][b] % 10 == 0):
                        grille[a][b] = grille[a][b] + 1.5
                    if (grille[a][b] % 10 == 0.5):
                        grille[a][b] = grille[a][b] + 1
                    if (grille[a][b] % 10 == 1):
                        grille[a][b] = grille[a][b] + 2.5
                    if (grille[a][b] % 10 == 2):
                        grille[a][b] = grille[a][b] + 2
                    if (grille[a][b] % 10 == 2.5):
                        grille[a][b] = grille[a][b] + 1
                    if (grille[a][b] % 10 == 3):
                        grille[a][b] = grille[a][b] + 1


        print(grille)

    def changer_num(X, Y):  # commande pour ecrire un chiffre cliquée
        if clickable_area_G1.collidepoint(event.pos):
            if (grille[X][Y] - (grille[X][Y] % 10) == 10):  # Si le chiffre clique est deja sur la case alors efface la case
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = grille[X][Y] % 10  # remet la case à 0 dans la matrice

            else:
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P1, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = grille[X][Y] % 10 + 10

        elif clickable_area_G2.collidepoint(event.pos):
            if (grille[X][Y] - (grille[X][Y] % 10) == 20):  # Si le chiffre clique est deja sur la case alors efface la case
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = grille[X][Y] % 10  # remet la case à 0 dans la matrice
            else:
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P2, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = grille[X][Y] % 10 + 20
        elif clickable_area_G3.collidepoint(event.pos):
            if (grille[X][Y] - (grille[X][Y] % 10) == 30):  # Si le chiffre clique est deja sur la case alors efface la case
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = grille[X][Y] % 10  # remet la case à 0 dans la matrice
            else:
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P3, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = grille[X][Y] % 10 + 30
        elif clickable_area_G4.collidepoint(event.pos):
            if (grille[X][Y] - (grille[X][Y] % 10) == 40):  # Si le chiffre clique est deja sur la case alors efface la case
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = grille[X][Y] % 10  # remet la case à 0 dans la matrice
            else:
                pygame.draw.rect(screen, colorclick,
                                 pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                screen.blit(P4, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                grille[X][Y] = grille[X][Y] % 10 + 40
        if (difficulte >= 5):
            if clickable_area_G5.collidepoint(event.pos):
                if (grille[X][Y] - (grille[X][Y] % 10) == 50):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    grille[X][Y] = grille[X][Y] % 10  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    screen.blit(P5, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = grille[X][Y] % 10 + 50
        if (difficulte >= 6):
            if clickable_area_G6.collidepoint(event.pos):
                if (grille[X][Y] - (grille[X][Y] % 10) == 60):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    grille[X][Y] = grille[X][Y] % 10  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    screen.blit(P6, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = grille[X][Y] % 10 + 60
        if (difficulte >= 7):
            if clickable_area_G7.collidepoint(event.pos):
                if (grille[X][Y] - (grille[X][Y] % 10) == 70):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    grille[X][Y] = grille[X][Y] % 10  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    screen.blit(P7, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = grille[X][Y] % 10 + 70
        if (difficulte >= 8):
            if clickable_area_G8.collidepoint(event.pos):
                if (grille[X][Y] - (grille[X][Y] % 10) == 80):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    grille[X][Y] = grille[X][Y] % 10  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    screen.blit(P8, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = grille[X][Y] % 10 + 80
        if (difficulte >= 9):
            if clickable_area_G9.collidepoint(event.pos):
                if (grille[X][Y] - (grille[X][Y] % 10) == 90):  # Si le chiffre clique est deja sur la case alors efface la case
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    grille[X][Y] = grille[X][Y] % 10  # remet la case à 0 dans la matrice
                else:
                    pygame.draw.rect(screen, colorclick,
                                     pygame.Rect(Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot,
                                                 cot))
                    screen.blit(P9, (Y * (cot + mar) + marge_gauche, X * (cot + mar) + marge_haut, cot, cot))
                    grille[X][Y] = grille[X][Y] % 10 + 90

    def click_sur_grille(grille, grille_rectangles):  # Sert a avoir les coordonnees du click sur la grille
        for i in range(difficulte):  # on cherche sur quel rectangle on a cliqué
            for j in range(difficulte):
                if (grille_rectangles[i][j].collidepoint(
                        event.pos)):  # rectangle trouvé, on renvoie ses coordonées dans la grille
                    x = math.floor(((event.pos[1] - marge_haut) / (cot + mar)))  #
                    # les coordonées sont inversées quand on passe de la grille a l'interface
                    y = math.floor((event.pos[0] - marge_gauche) / (cot + mar))
                    change_couleur_case_selec(x, y)
                    co = (x, y)  # renvoie les coordonées a la place de les passer en variable globale
                    return co
        return 0

    def click_sur_grille_fleches(grille, grille_fleches):  # Sert a avoir les coordonnees du click sur la grille
        for i in range(difficulte):  # on cherche sur quel rectangle on a cliqué
            for j in range(difficulte * 2):
                if (grille_fleches[i][j].collidepoint(
                        event.pos)):  # rectangle trouvé, on renvoie ses coordonées dans la grille
                    x = math.floor((event.pos[0] - marge_gauche) / (cot + mar))
                    y = math.floor(((event.pos[1] - marge_haut) / (mar)))
                    if y == 0 or y == 1:
                        y = 0
                    elif y == 2:
                        y = 1
                    elif y == 3 or y == 4:
                        y = 2
                    elif y == 5:
                        y = 3
                    elif y == 7 or y == 6:
                        y = 4
                    elif y == 8:
                        y = 5
                    elif y == 10 or y == 9:
                        y = 6
                    elif y == 11:
                        y = 7
                    elif y == 13 or y == 12:
                        y = 8
                    elif y == 14:
                        y = 9
                    elif y == 15 or y == 16:
                        y = 10
                    elif y == 17:
                        y = 11
                    elif y == 18 or y == 19:
                        y = 12
                    elif y == 20:
                        y = 13
                    elif y == 21 or y == 22:
                        y = 14
                    elif y == 23:
                        y = 15
                    elif y == 24 or y == 25:
                        y = 16
                    change_couleur_case_selec_fleche(x,y)
                    co = (x, y)  # renvoie les coordonées a la place de les passer en variable globale
                    return co
        return 0

    def reset():
        grille = [[0] * difficulte for i in
                  range(
                      difficulte)]
        for x in range(difficulte):
            for y in range(difficulte):
                rect = pygame.draw.rect(screen, color,
                                        pygame.Rect(x * (cot + mar) + marge_gauche, y * (cot + mar) + marge_haut, cot,
                                                    cot))  # dessine la "grille de dimension n"
                if x != difficulte - 1:
                    pygame.draw.rect(screen, background,
                                     pygame.Rect(cot + x * (cot + mar) + marge_gauche,
                                                 y * (cot + mar) + marge_haut, cot / 2,
                                                 cot))
                if y != difficulte - 1:
                    pygame.draw.rect(screen, background,
                                     pygame.Rect(x * (cot + mar) + marge_gauche,
                                                 cot + y * (cot + mar) + marge_haut,
                                                 cot,
                                                 cot / 2))

        return grille

    #############################    VARIABLES    ############################
    pygame.init()
    WINDOW_SIZE = [1080, 720]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    background = (0, 105, 102)
    pygame.display.set_caption("Futoshiki")  # titre de la fenetre

    # grille ou on appliquera les algo
    # la grille est initialisée a 0 partout
    grille_rectangles = [[0] * difficulte for i in
                         range(
                             difficulte)]  # grille interface (correspond aux rectangles qui sont des zones cliquables)

    grille_fleches = [[0] * (difficulte * 2) for i in
                         range(
                             difficulte)]  # grille interface (correspond aux rectangles qui sont des zones cliquables)

    grille = [[0] * difficulte for i in
                         range(
                             difficulte)]


    mar = int((((WINDOW_SIZE[1] * 0.8) / difficulte) / 3))  # marge des rectangles
    cot = int((((WINDOW_SIZE[1] * 0.8) / difficulte) / 3 * 2))
    marge_haut = 150
    marge_gauche = ((WINDOW_SIZE[0] - (difficulte * (cot + mar) - mar)) / 2)

    Icone = pygame.image.load("Ressources/assets/icone.jpg")  # lecture de l'icone
    pygame.display.set_icon(Icone)  # mettre l'icone
    running = True  # Vérifie si la fenetre doit rester ouverte
    screen.fill(background)  # met le fond en vert
    color = (255, 255, 255)  # couleur que l'on utilise pour les rectangles
    colorerreur = (255, 0, 0)  # Couleur quand deux chiffres sont identiques sur la même ligne
    colorclick = (255, 255, 35)  # couleur quand on click sur un rectangle
    colorclickfleche = (255, 139, 0)  # couleur quand on click sur un rectangle pour fleche
    colorbase = (170, 170, 170)  # couleur des chiffres de base non modifiables

    # Chargement des polices
    titleFont = pygame.font.Font("Ressources/go3v2.ttf", 100)
    subMenuFont = pygame.font.Font("Ressources/go3v2.ttf", 60)

    # chargement assets, zones cliquables et affichage écran
    G1 = pygame.image.load("Ressources/assets/G1.png").convert_alpha()
    G2 = pygame.image.load("Ressources/assets/G2.png").convert_alpha()
    G3 = pygame.image.load("Ressources/assets/G3.png").convert_alpha()
    G4 = pygame.image.load("Ressources/assets/G4.png").convert_alpha()
    G5 = pygame.image.load("Ressources/assets/G5.png").convert_alpha()
    G6 = pygame.image.load("Ressources/assets/G6.png").convert_alpha()
    G7 = pygame.image.load("Ressources/assets/G7.png").convert_alpha()
    G8 = pygame.image.load("Ressources/assets/G8.png").convert_alpha()
    G9 = pygame.image.load("Ressources/assets/G9.png").convert_alpha()

    fleche_gauche = pygame.image.load("Ressources/assets/fleche_gauche.png").convert_alpha()
    fleche_gauche = pygame.transform.scale(fleche_gauche, (50, 100))
    fleche_haut = pygame.image.load("Ressources/assets/fleche_haut.png").convert_alpha()
    fleche_haut = pygame.transform.scale(fleche_haut, (100, 50))
    fleche_droit = pygame.image.load("Ressources/assets/fleche_droit.png").convert_alpha()
    fleche_droit = pygame.transform.scale(fleche_droit, (50, 100))
    fleche_bas = pygame.image.load("Ressources/assets/fleche_bas.png").convert_alpha()
    fleche_bas = pygame.transform.scale(fleche_bas, (100, 50))

    screen.blit(fleche_gauche, (50, 200))
    screen.blit(fleche_haut, (25, 350))
    screen.blit(fleche_droit, (175, 200))
    screen.blit(fleche_bas, (150, 350))

    clickable_area_fleche_gauche = pygame.Rect((50, 200), (50, 100))
    clickable_area_fleche_haut = pygame.Rect((25, 350), (100, 50))
    clickable_area_fleche_droit = pygame.Rect((175, 200), (50, 100))
    clickable_area_fleche_bas = pygame.Rect((150, 350), (100, 50))

    fleche_gauche = pygame.transform.scale(fleche_gauche, (mar, cot))
    fleche_haut = pygame.transform.scale(fleche_haut, (cot, mar))
    fleche_droit = pygame.transform.scale(fleche_droit, (mar, cot))
    fleche_bas = pygame.transform.scale(fleche_bas, (cot, mar))


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

    clickable_area_resoudre = pygame.Rect((10, 580), (240, 50))
    clickable_area_reset = pygame.Rect((10, 510), (240, 50))
    clickable_area_retour = pygame.Rect((10, 650), (240, 50))

    # affichage écran des polices
    screen.blit(subMenuFont.render("Reset", True, (0, 0, 0)), (10, 510))
    screen.blit(subMenuFont.render("Résoudre", True, (0, 0, 0)), (1, 580))
    screen.blit(subMenuFont.render("Retour", True, (0, 0, 0)), (10, 650))
    screen.blit(titleFont.render("Solveur", True, (0, 0, 0)), (330, 30))

    for x in range(difficulte):
        for y in range(difficulte):
            rect = pygame.draw.rect(screen, color,
                                    pygame.Rect(x * (cot + mar) + marge_gauche, y * (cot + mar) + marge_haut, cot,
                                                cot))  # dessine la "grille de dimension n"
            grille_rectangles[x][y] = rect

    for x in range(difficulte):
        for y in range(difficulte):
            if x == difficulte - 1:
                rect = pygame.draw.rect(screen, background,
                                        pygame.Rect(0, 0, 0, 0)) # dessine la "grille de dimension n"

                grille_fleches[x][y * 2] = rect
            if x != difficulte - 1:
                rect = pygame.draw.rect(screen, background,
                                        pygame.Rect(cot + x * (cot + mar) + marge_gauche, y * (cot + mar) + marge_haut, cot/2,
                                                    cot))  # dessine la "grille de dimension n"

                grille_fleches[x][y * 2] = rect
            if y == difficulte - 1:
                rect = pygame.draw.rect(screen, background,
                                        pygame.Rect(0, 0, 0, 0)) # dessine la "grille de dimension n"

                grille_fleches[x][y * 2 + 1] = rect
            if y != difficulte - 1:
                rect = pygame.draw.rect(screen, background,
                                        pygame.Rect(x * (cot + mar) + marge_gauche,cot + y * (cot + mar) + marge_haut,
                                                    cot,
                                                    cot/2))  # dessine la "grille de dimension n"
                grille_fleches[x][y * 2 + 1] = rect
    def reconsVal(difficulte,grilleG,list):
        for i in range(difficulte):
            for j in range (difficulte):
                if grilleG[2*i][2*j]!=0:
                    screen.blit(list[grilleG[2*i][2*j]],(j*(cot+mar) + marge_gauche, i * (cot+mar) + marge_haut, cot, cot))
    def verif_case(x, y, grille):
        for i in range(0, len(grille), 2):
            if (i != x and grille[i][y] == grille[x][y]):
                return True
        for j in range(0, len(grille), 2):
            if (j != y and grille[x][j] == grille[x][y]):
                return True
        return False


    def verif_grille(grille):
        for i in range(0, len(grille), 2):
            for j in range(0, len(grille), 2):
                if grille[i][j] != 0 and verif_case(i, j, grille):
                    return False
        return True




    X = -1  # coordonneé de la grille x de la dernière case cliquée
    Y = -1  # coordonneé de la grille y de la dernière case cliquée
    A = -1
    B = -1
    clicked = True
    D=difficulte
    Dval=(difficulte*2)-1
    list_val = {1: P1, 2: P2, 3: P3, 4: P4, 5: P5, 6: P6, 7: P7, 8: P8, 9: P9}
    

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
                if (click_sur_grille_fleches(grille, grille_fleches)):
                    A = click_sur_grille_fleches(grille, grille_fleches)[0]
                    B = click_sur_grille_fleches(grille, grille_fleches)[1]
                if (X != -1):
                    changer_num(X, Y)
                if(A != -1):
                    changer_fleche(A, B)
                if clickable_area_reset.collidepoint(event.pos):
                    grille = reset()
                if clickable_area_retour.collidepoint(event.pos):
                    from main import menuSolveur
                    menuSolveur(screen)
                if clickable_area_resoudre.collidepoint(event.pos):
                                    from Baktrak import Solveur
                                    from grille import afficheVal
                                    grille2= [[0]*((difficulte*2)-1) for i in range((difficulte*2)-1)]
                                    afficheVal(grille,grille2)
                                    if verif_grille(grille2):
                                        if Solveur(grille2, Dval, D):
                                            reconsVal(difficulte, grille2, list_val)
                                            pygame.display.update()
                                            print("<---------------------------->")
                                            for element in grille2:  # Affichage console de la grille
                                                print(element)
                                        else:
                                            print("Impossible à résoudre")
                                    else:
                                        print("Impossiblee a résoudre") 

            if event.type == MOUSEBUTTONUP:  # besoin de cette condition pour triter les clicks 1 a 1
                clicked = True



        pygame.display.flip()

    for element in grille:  # Affichage console de la grille
        print(element)
    # !/usr/bin/python3
