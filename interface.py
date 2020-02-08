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
import sys


    #############################    FONCTIONS    ############################

def definterface():
    #############################    VARIABLES    ############################

    pygame.init()
    WINDOW_SIZE = [1080, 720]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Futoshiki")  # titre de la fenetre

    Icone = pygame.image.load("assets/icone.jpg")  # lecture de l'icone
    pygame.display.set_icon(Icone)  # mettre l'icone
    running = True  # Vérifie si la fenetre doit rester ouverte
    screen.fill((0, 105, 102))  # met le fond en vert
    imagetitre = pygame.image.load("assets/titreFutoshiki.png").convert_alpha()  # Lecture du titre Futoshiki

    X4 = pygame.image.load("assets/4x4.png").convert_alpha()  # Lecture des titres des boutons
    X5 = pygame.image.load("assets/5x5.png").convert_alpha()
    X6 = pygame.image.load("assets/6x6.png").convert_alpha()
    X7 = pygame.image.load("assets/7x7.png").convert_alpha()
    X8 = pygame.image.load("assets/8x8.png").convert_alpha()
    X9 = pygame.image.load("assets/9x9.png").convert_alpha()
    REG = pygame.image.load("assets/regles.png").convert_alpha()
    QUIT = pygame.image.load("assets/quitter.png").convert_alpha()

    clickable_area_X4 = pygame.Rect((229, 240), (200, 100))  # Zone cliquable des titres (comme un bouton)
    # rect_surf_G1 = pygame.Surface(clickable_area_G1.size)
    clickable_area_X5 = pygame.Rect((456, 240), (200, 100))
    # rect_surf_G2 = pygame.Surface(clickable_area_G2.size)
    clickable_area_X6 = pygame.Rect((684, 240), (200, 100))
    # rect_surf_G3 = pygame.Surface(clickable_area_G3.size)
    clickable_area_X7 = pygame.Rect((229, 385), (200, 100))
    # rect_surf_G4 = pygame.Surface(clickable_area_G4.size)
    clickable_area_X8 = pygame.Rect((456, 385), (200, 100))
    # rect_surf_G4 = pygame.Surface(clickable_area_G4.size)
    clickable_area_X9 = pygame.Rect((684, 385), (200, 100))
    # rect_surf_G4 = pygame.Surface(clickable_area_G4.size)
    clickable_area_REG = pygame.Rect((320, 500), (200, 100))
    # rect_surf_G4 = pygame.Surface(clickable_area_G4.size)
    clickable_area_QUIT = pygame.Rect((600, 500), (200, 100))
    # rect_surf_G4 = pygame.Surface(clickable_area_G4.size)

    initial = True
    #############################    MAIN    ############################

    while running:  # Tant que la fentetre est en cours

        for event in pygame.event.get():  # Pour chaque evenement
            if event.type == pygame.QUIT:
                running = False

            if initial:
                screen.blit(imagetitre, (290, 50))  # Affichage du titre Futoshiki
                screen.blit(X4, (228, 240))  # Affichage des boutons
                screen.blit(X5, (456, 240))
                screen.blit(X6, (683, 240))
                screen.blit(X7, (228, 385))
                screen.blit(X8, (456, 385))
                screen.blit(X9, (683, 385))
                screen.blit(REG, (320, 500))
                screen.blit(QUIT, (600, 500))

                initial = False
            if (event.type == MOUSEBUTTONDOWN):
                if clickable_area_X4.collidepoint(event.pos):
                    from levels import levels
                    levels(4)

                if clickable_area_X5.collidepoint(event.pos):
                    from levels import levels
                    levels(5)

                if clickable_area_X6.collidepoint(event.pos):
                    from levels import levels
                    levels(6)

                if clickable_area_X7.collidepoint(event.pos):
                    from levels import levels
                    levels(7)

                if clickable_area_X8.collidepoint(event.pos):
                    from levels import levels
                    levels(8)

                if clickable_area_X9.collidepoint(event.pos):
                    from levels import levels
                    levels(9)

                if clickable_area_REG.collidepoint(event.pos):
                    jeu_REG()

                if clickable_area_QUIT.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()


definterface()