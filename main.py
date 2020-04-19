    #!/usr/bin/python3

    #############################################################################
    #############################################################################
    ###########################       FUTOSHIKI       ###########################
    ########      FAIT PAR : Allan, Rayan, Nico, Alexandre et Mattéo      #######
    ############################     Version 1.0     ############################
    #############################################################################
    #############################################################################


import pygame, os, math, sys, json
from pygame.locals import *

fond = (0, 105, 102)

def menuAccueil(screen):
    screen.fill((0, 105, 102))
    #Chargement assets 
    X4 = pygame.image.load("assets/4x4.png").convert_alpha()
    X5 = pygame.image.load("assets/5x5.png").convert_alpha()
    X6 = pygame.image.load("assets/6x6.png").convert_alpha()
    X7 = pygame.image.load("assets/7x7.png").convert_alpha()
    X8 = pygame.image.load("assets/8x8.png").convert_alpha()
    X9 = pygame.image.load("assets/9x9.png").convert_alpha()
    REG = pygame.image.load("assets/regles.png").convert_alpha()
    QUIT = pygame.image.load("assets/quitter.png").convert_alpha()
    imagetitre = pygame.image.load("assets/titreFutoshiki.png").convert_alpha()

    #zones cliquables
    clickable_area_X4 = pygame.Rect((229, 240), (200, 100))  
    clickable_area_X5 = pygame.Rect((456, 240), (200, 100))
    clickable_area_X6 = pygame.Rect((684, 240), (200, 100))
    clickable_area_X7 = pygame.Rect((229, 385), (200, 100))
    clickable_area_X8 = pygame.Rect((456, 385), (200, 100))
    clickable_area_X9 = pygame.Rect((684, 385), (200, 100))
    clickable_area_REG = pygame.Rect((320, 500), (200, 100))
    clickable_area_QUIT = pygame.Rect((600, 500), (200, 100))

    #affichage à l'écran
    screen.blit(imagetitre, (290, 50))  
    screen.blit(X4, (228, 240))  
    screen.blit(X5, (456, 240))
    screen.blit(X6, (683, 240))
    screen.blit(X7, (228, 385))
    screen.blit(X8, (456, 385))
    screen.blit(X9, (684, 385))
    screen.blit(REG, (320, 500))
    screen.blit(QUIT, (600, 500))

    menuAccueilActive = True

    while menuAccueilActive:  # Tant que la fentetre est en cours
        for event in pygame.event.get():  # Detecte la position de la souris constament 
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
            if event.type == MOUSEBUTTONDOWN:
                if clickable_area_X4.collidepoint(event.pos):
                    menuLevels(screen, 4)
                    menuAccueilActive = False
                if clickable_area_X5.collidepoint(event.pos):
                    menuLevels(screen, 5)
                    menuAccueilActive = False
                if clickable_area_X6.collidepoint(event.pos):
                    menuLevels(screen, 6)
                    menuAccueilActive = False
                if clickable_area_X7.collidepoint(event.pos):
                    menuLevels(screen, 7)
                    menuAccueilActive = False
                if clickable_area_X8.collidepoint(event.pos):
                    menuLevels(screen, 8)
                    menuAccueilActive = False
                if clickable_area_X9.collidepoint(event.pos):
                    menuLevels(screen, 9)
                    menuAccueilActive = False
                if clickable_area_REG.collidepoint(event.pos):
                    menuRegles(screen)
                    menuAccueilActive = False
                if clickable_area_QUIT.collidepoint(event.pos):
                    pygame.quit()
                    quit()

        pygame.display.update()
        

def menuLevels(screen, level):
    screen.fill((0, 105, 102))  # met le fond en vert

    title = pygame.image.load("assets/niveaux_" + str(level) + "x" + str(level) + ".png").convert_alpha()
    retour = pygame.image.load("assets/retour.png").convert_alpha()
    clickable_area_retour = pygame.Rect((-10, 670), (240, 50))

    G1 = pygame.image.load("assets/G1.png").convert_alpha()  # Lecture des images des niveaux
    G2 = pygame.image.load("assets/G2.png").convert_alpha()
    G3 = pygame.image.load("assets/G3.png").convert_alpha()
    G4 = pygame.image.load("assets/G4.png").convert_alpha()
    G5 = pygame.image.load("assets/G5.png").convert_alpha()
    G6 = pygame.image.load("assets/G6.png").convert_alpha()
    G7 = pygame.image.load("assets/G7.png").convert_alpha()
    G8 = pygame.image.load("assets/G8.png").convert_alpha()
    G9 = pygame.image.load("assets/G9.png").convert_alpha()

    screen.blit(G1, (262, 190))  # Affichage des boutons
    screen.blit(G2, (490, 190))
    screen.blit(G3, (717, 190))
    screen.blit(G4, (262, 335))
    screen.blit(G5, (490, 335))
    screen.blit(G6, (717, 335))
    screen.blit(G7, (262, 480))
    screen.blit(G8, (490, 480))
    screen.blit(G9, (717, 480))
    screen.blit(retour, (-10, 670))
    screen.blit(title, (180,50))

    clickable_area_G1 = pygame.Rect((262, 190), (100, 100))
    clickable_area_G2 = pygame.Rect((490, 190), (100, 100))
    clickable_area_G3 = pygame.Rect((717, 190), (100, 100))
    clickable_area_G4 = pygame.Rect((262, 335), (100, 100))
    clickable_area_G5 = pygame.Rect((490, 335), (100, 100))
    clickable_area_G6 = pygame.Rect((717, 335), (100, 100))
    clickable_area_G7 = pygame.Rect((262, 480), (100, 100))
    clickable_area_G8 = pygame.Rect((490, 480), (100, 100))
    clickable_area_G9 = pygame.Rect((717, 480), (100, 100))

    levelMenuActive = True

    while levelMenuActive:
        for event in pygame.event.get():  # Pour chaque evenement
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if (event.type == MOUSEBUTTONDOWN):
                if clickable_area_G1.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importGrid(level, 1)
                    def_Futoshiki(level, grid["grid"], grid["solution"])
                if clickable_area_G2.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importGrid(level, 2)
                    def_Futoshiki(level, grid["grid"], grid["solution"])
                if clickable_area_G3.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importGrid(level, 3)
                    def_Futoshiki(level, grid["grid"], grid["solution"])
                if clickable_area_G4.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importGrid(level, 4)
                    def_Futoshiki(level, grid["grid"], grid["solution"])
                if clickable_area_G5.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importGrid(level, 5)
                    def_Futoshiki(level, grid["grid"], grid["solution"])
                if clickable_area_G6.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importGrid(level, 6)
                    def_Futoshiki(level, grid["grid"], grid["solution"])
                if clickable_area_G7.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importGrid(level, 7)
                    def_Futoshiki(level, grid["grid"], grid["solution"])
                if clickable_area_G8.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importGrid(level, 8)
                    def_Futoshiki(level, grid["grid"], grid["solution"])
                if clickable_area_G9.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importGrid(level, 9)
                    def_Futoshiki(level, grid["grid"], grid["solution"])
                if clickable_area_retour.collidepoint(event.pos):
                    menuAccueil(screen)
            
            pygame.display.flip()

                
def menuRegles(screen):
    screen.fill((0, 105, 102))  # met le fond en vert
    #Titre
    title = pygame.image.load("assets/regles.png").convert_alpha()
    screen.blit(title, (450, 0))
    #Bouton retour
    retour = pygame.image.load("assets/retour.png").convert_alpha()
    screen.blit(retour, (-10, 670))
    clickable_area_retour = pygame.Rect((-10, 670), (240, 50))

    running = True

    while running:  # Tant que la fentetre est en cours

        for event in pygame.event.get():  # Pour chaque evenement
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if (event.type == MOUSEBUTTONDOWN):
                if clickable_area_retour.collidepoint(event.pos):
                    menuAccueil(screen)

            pygame.display.flip()


def definterface():

    pygame.init()
    WINDOW_SIZE = [1080, 720]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Futoshiki")  # titre de la fenetre

    Icone = pygame.image.load("assets/icone.jpg")  # lecture de l'icone
    pygame.display.set_icon(Icone)  # mettre l'icone
    
    menuAccueil(screen)

def importGrid(diff, niveau):
    with open('grids.json') as grids:
        grids_dict = json.load(grids)
    return grids_dict[str(diff) + "x" + str(diff)]["level" + str(niveau)]
        

definterface()
