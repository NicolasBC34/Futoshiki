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


def menuAccueil(screen):
    screen.fill((0, 105, 102))
    
    #Définition des polices
    itemFont = pygame.font.Font("Ressources/go3v2.ttf", 85)
    subMenuFont = pygame.font.Font("Ressources/go3v2.ttf", 60)
    titleFont = pygame.font.Font("Ressources/go3v2.ttf", 100)

    #zones cliquables
    clickable_area_X4 = pygame.Rect((250, 240), (200, 100))  
    clickable_area_X5 = pygame.Rect((478, 240), (200, 100))
    clickable_area_X6 = pygame.Rect((705, 240), (200, 100))
    clickable_area_X7 = pygame.Rect((250, 385), (200, 100))
    clickable_area_X8 = pygame.Rect((478, 385), (200, 100))
    clickable_area_X9 = pygame.Rect((705, 385), (200, 100))
    clickable_area_REG = pygame.Rect((320, 550), (200, 100))
    clickable_area_SOL = pygame.Rect((600, 550), (200, 100))
    clickable_area_QUIT = pygame.Rect((460, 640), (200, 100))

    #affichage à l'écran
    screen.blit(titleFont.render("Futoshiki", True, (0, 0, 0)), (330, 50))  
    screen.blit(itemFont.render("4X4", True, (0, 0, 0)), (250, 240))
    screen.blit(itemFont.render("5X5", True, (0, 0, 0)), (478, 240))
    screen.blit(itemFont.render("6X6", True, (0, 0, 0)), (705, 240))
    screen.blit(itemFont.render("7X7", True, (0, 0, 0)), (250, 385))
    screen.blit(itemFont.render("8X8", True, (0, 0, 0)), (478, 385))
    screen.blit(itemFont.render("9X9", True, (0, 0, 0)), (705, 385))
    screen.blit(subMenuFont.render("Règles", True, (0, 0, 0)), (320, 550))
    screen.blit(subMenuFont.render("Solveur", True, (0, 0, 0)), (600, 550))
    screen.blit(subMenuFont.render("Quitter", True, (0, 0, 0)), (460, 640))

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
                if clickable_area_SOL.collidepoint(event.pos):
                    menuSolveur(screen)
                    menuAccueilActive = False
                if clickable_area_QUIT.collidepoint(event.pos):
                    pygame.quit()
                    quit()

        pygame.display.update()
        

def menuLevels(screen, difficulte):
    screen.fill((0, 105, 102))  # met le fond en vert

    #définition des polices
    titleFont = pygame.font.Font("Ressources/go3v2.ttf", 100)
    subMenuFont = pygame.font.Font("Ressources/go3v2.ttf", 60)

    #chargement assets
    G1 = pygame.image.load("Ressources/assets/G1.png").convert_alpha()
    G2 = pygame.image.load("Ressources/assets/G2.png").convert_alpha()
    G3 = pygame.image.load("Ressources/assets/G3.png").convert_alpha()
    G4 = pygame.image.load("Ressources/assets/G4.png").convert_alpha()
    G5 = pygame.image.load("Ressources/assets/G5.png").convert_alpha()
    G6 = pygame.image.load("Ressources/assets/G6.png").convert_alpha()
    G7 = pygame.image.load("Ressources/assets/G7.png").convert_alpha()
    G8 = pygame.image.load("Ressources/assets/G8.png").convert_alpha()
    G9 = pygame.image.load("Ressources/assets/G9.png").convert_alpha()

    #ajout à l'écran
    screen.blit(G1, (262, 190))  
    screen.blit(G2, (490, 190))
    screen.blit(G3, (717, 190))
    screen.blit(G4, (262, 335))
    screen.blit(G5, (490, 335))
    screen.blit(G6, (717, 335))
    screen.blit(G7, (262, 480))
    screen.blit(G8, (490, 480))
    screen.blit(G9, (717, 480))
    screen.blit(subMenuFont.render("SCORES", True, (0, 0, 0)), (860, 650))
    screen.blit(subMenuFont.render("RETOUR", True, (0, 0, 0)), (10, 650))
    screen.blit(titleFont.render("Niveau " + str(difficulte) + "x" + str(difficulte), True, (0, 0, 0)), (280, 30))

    #zones clickables
    clickable_area_G1 = pygame.Rect((262, 190), (100, 100))
    clickable_area_G2 = pygame.Rect((490, 190), (100, 100))
    clickable_area_G3 = pygame.Rect((717, 190), (100, 100))
    clickable_area_G4 = pygame.Rect((262, 335), (100, 100))
    clickable_area_G5 = pygame.Rect((490, 335), (100, 100))
    clickable_area_G6 = pygame.Rect((717, 335), (100, 100))
    clickable_area_G7 = pygame.Rect((262, 480), (100, 100))
    clickable_area_G8 = pygame.Rect((490, 480), (100, 100))
    clickable_area_G9 = pygame.Rect((717, 480), (100, 100))
    clickable_area_scores = pygame.Rect((860, 650), (240,50))
    clickable_area_retour = pygame.Rect((10, 650), (240, 50))

    levelMenuActive = True

    while levelMenuActive:
        for event in pygame.event.get():  # Pour chaque evenement
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if (event.type == MOUSEBUTTONDOWN):
                if clickable_area_G1.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importData("grids", difficulte, 1)
                    def_Futoshiki(difficulte, 1, grid["grid"], grid["solution"])
                if clickable_area_G2.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importData("grids", difficulte, 2)
                    def_Futoshiki(difficulte, 2, grid["grid"], grid["solution"])
                if clickable_area_G3.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importData("grids", difficulte, 3)
                    def_Futoshiki(difficulte, 3, grid["grid"], grid["solution"])
                if clickable_area_G4.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importData("grids", difficulte, 4)
                    def_Futoshiki(difficulte, 4, grid["grid"], grid["solution"])
                if clickable_area_G5.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importData("grids", difficulte, 5)
                    def_Futoshiki(difficulte, 5, grid["grid"], grid["solution"])
                if clickable_area_G6.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importData("grids", difficulte, 6)
                    def_Futoshiki(difficulte, 6, grid["grid"], grid["solution"])
                if clickable_area_G7.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importData("grids", difficulte, 7)
                    def_Futoshiki(difficulte, 7, grid["grid"], grid["solution"])
                if clickable_area_G8.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importData("grids", difficulte, 8)
                    def_Futoshiki(difficulte, 8, grid["grid"], grid["solution"])
                if clickable_area_G9.collidepoint(event.pos):
                    from Futoshiki import def_Futoshiki
                    grid = importData("grids", difficulte, 9)
                    def_Futoshiki(difficulte, 9, grid["grid"], grid["solution"])
                if clickable_area_scores.collidepoint(event.pos):
                    menuScores(screen, difficulte)
                if clickable_area_retour.collidepoint(event.pos):
                    menuAccueil(screen)
            
            pygame.display.flip()


def menuRegles(screen):
    screen.fill((0, 105, 102))

    # Définition des polices
    titleFont = pygame.font.Font("Ressources/go3v2.ttf", 100)
    subMenuFont = pygame.font.Font("Ressources/go3v2.ttf", 60)
    texteRegles = pygame.font.Font("Ressources/go3v2.ttf", 40)

    # zones cliquables
    clickable_area_retour = pygame.Rect((10, 650), (240, 50))

    # affichage à l'écran
    screen.blit(titleFont.render("Règles", True, (0, 0, 0)), (370, 30))
    screen.blit(subMenuFont.render("Retour", True, (0, 0, 0)), (10, 650))
    screen.blit(texteRegles.render('Le Futoshiki est fondé sur une grille carrée ', True, (0, 0, 0)), (25, 150))
    screen.blit(texteRegles.render('dans laquelle sont inscrits des nombres suivant ', True, (0, 0, 0)), (25, 200))
    screen.blit(texteRegles.render('quelques règles simples. Sur une grille de 5x5, ', True, (0, 0, 0)), (25, 250))
    screen.blit(texteRegles.render('les nombres de un à cinq doivent être placés dans ', True, (0, 0, 0)), (25, 300))
    screen.blit(texteRegles.render('chaque ligne et chaque colonne, sans aucune ', True, (0, 0, 0)), (25, 350))
    screen.blit(texteRegles.render('répétition. Les signes "plus grand que" ou ', True, (0, 0, 0)), (25, 400))
    screen.blit(texteRegles.render('"plus petit que" entre les cases sont des indices ', True, (0, 0, 0)), (25, 450))
    screen.blit(texteRegles.render('qui doivent obligatoirement être respectés. ', True, (0, 0, 0)), (25, 500))
    screen.blit(texteRegles.render('Chaque grille possède une solution unique.', True, (0, 0, 0)), (25, 550))

    menuReglesActive = True

    while menuReglesActive:  # Tant que la fentetre est en cours
        for event in pygame.event.get():  # Pour chaque evenement
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if (event.type == MOUSEBUTTONDOWN):
                if clickable_area_retour.collidepoint(event.pos):
                    menuAccueil(screen)

            pygame.display.flip()


def menuSolveur(screen):
    screen.fill((0, 105, 102))

    # Définition des polices
    itemFont = pygame.font.Font("Ressources/go3v2.ttf", 85)
    titleFont = pygame.font.Font("Ressources/go3v2.ttf", 100)
    subMenuFont = pygame.font.Font("Ressources/go3v2.ttf", 60)

    # zones cliquables
    #zones cliquables
    clickable_area_X4 = pygame.Rect((250, 240), (200, 100))
    clickable_area_X5 = pygame.Rect((478, 240), (200, 100))
    clickable_area_X6 = pygame.Rect((705, 240), (200, 100))
    clickable_area_X7 = pygame.Rect((250, 385), (200, 100))
    clickable_area_X8 = pygame.Rect((478, 385), (200, 100))
    clickable_area_X9 = pygame.Rect((705, 385), (200, 100))
    clickable_area_retour = pygame.Rect((10, 650), (240, 50))

    # affichage à l'écran
    screen.blit(itemFont.render("4X4", True, (0, 0, 0)), (250, 240))
    screen.blit(itemFont.render("5X5", True, (0, 0, 0)), (478, 240))
    screen.blit(itemFont.render("6X6", True, (0, 0, 0)), (705, 240))
    screen.blit(itemFont.render("7X7", True, (0, 0, 0)), (250, 385))
    screen.blit(itemFont.render("8X8", True, (0, 0, 0)), (478, 385))
    screen.blit(itemFont.render("9X9", True, (0, 0, 0)), (705, 385))
    screen.blit(titleFont.render("Solveur", True, (0, 0, 0)), (370, 30))
    screen.blit(subMenuFont.render("Retour", True, (0, 0, 0)), (10, 650))

    menuReglesActive = True

    while menuReglesActive:  # Tant que la fentetre est en cours
        for event in pygame.event.get():  # Pour chaque evenement
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if (event.type == MOUSEBUTTONDOWN):
                if clickable_area_X4.collidepoint(event.pos):
                    from Solveur import def_Solveur
                    def_Solveur(4)
                if clickable_area_X5.collidepoint(event.pos):
                    from Solveur import def_Solveur
                    def_Solveur(5)
                if clickable_area_X6.collidepoint(event.pos):
                    from Solveur import def_Solveur
                    def_Solveur(6)
                if clickable_area_X7.collidepoint(event.pos):
                    from Solveur import def_Solveur
                    def_Solveur(7)
                if clickable_area_X8.collidepoint(event.pos):
                    from Solveur import def_Solveur
                    def_Solveur(8)
                if clickable_area_X9.collidepoint(event.pos):
                    from Solveur import def_Solveur
                    def_Solveur(9)
                if clickable_area_retour.collidepoint(event.pos):
                    menuAccueil(screen)

            pygame.display.flip()

def menuScores(screen, difficulte):
    screen.fill((0,105,102))
    #definition des polices
    titleFont = pygame.font.Font("Ressources/go3v2.ttf", 100)
    subMenuFont = pygame.font.Font("Ressources/go3v2.ttf", 60)

    #chargement assets
    G1 = pygame.image.load("Ressources/assets/G1.png").convert_alpha()  
    G2 = pygame.image.load("Ressources/assets/G2.png").convert_alpha()
    G3 = pygame.image.load("Ressources/assets/G3.png").convert_alpha()
    G4 = pygame.image.load("Ressources/assets/G4.png").convert_alpha()
    G5 = pygame.image.load("Ressources/assets/G5.png").convert_alpha()
    G6 = pygame.image.load("Ressources/assets/G6.png").convert_alpha()
    G7 = pygame.image.load("Ressources/assets/G7.png").convert_alpha()
    G8 = pygame.image.load("Ressources/assets/G8.png").convert_alpha()
    G9 = pygame.image.load("Ressources/assets/G9.png").convert_alpha()

    #ajout à l'écran
    screen.blit(titleFont.render("Scores " + str(difficulte) + "x" + str(difficulte), True, (0, 0, 0)), (270, 30))
    screen.blit(subMenuFont.render("RETOUR", True, (0, 0, 0)), (10, 650))
    screen.blit(G1, (262, 190))  
    screen.blit(G2, (490, 190))
    screen.blit(G3, (717, 190))
    screen.blit(G4, (262, 335))
    screen.blit(G5, (490, 335))
    screen.blit(G6, (717, 335))
    screen.blit(G7, (262, 480))
    screen.blit(G8, (490, 480))
    screen.blit(G9, (717, 480))

    #zones clickables
    clickable_area_retour = pygame.Rect((10, 650), (240, 50))
    clickable_area_G1 = pygame.Rect((262, 190), (100, 100))
    clickable_area_G2 = pygame.Rect((490, 190), (100, 100))
    clickable_area_G3 = pygame.Rect((717, 190), (100, 100))
    clickable_area_G4 = pygame.Rect((262, 335), (100, 100))
    clickable_area_G5 = pygame.Rect((490, 335), (100, 100))
    clickable_area_G6 = pygame.Rect((717, 335), (100, 100))
    clickable_area_G7 = pygame.Rect((262, 480), (100, 100))
    clickable_area_G8 = pygame.Rect((490, 480), (100, 100))
    clickable_area_G9 = pygame.Rect((717, 480), (100, 100))

    menuScoresActive = True

    while menuScoresActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                if clickable_area_G1.collidepoint(event.pos):
                    scoresView(screen, difficulte, 1)
                if clickable_area_G2.collidepoint(event.pos):
                    scoresView(screen, difficulte, 2)
                if clickable_area_G3.collidepoint(event.pos):
                    scoresView(screen, difficulte, 3)
                if clickable_area_G4.collidepoint(event.pos):
                    scoresView(screen, difficulte, 4)
                if clickable_area_G5.collidepoint(event.pos):
                    scoresView(screen, difficulte, 5)
                if clickable_area_G6.collidepoint(event.pos):
                    scoresView(screen, difficulte, 6)
                if clickable_area_G7.collidepoint(event.pos):
                    scoresView(screen, difficulte, 7)
                if clickable_area_G8.collidepoint(event.pos):
                    scoresView(screen, difficulte, 8)
                if clickable_area_G9.collidepoint(event.pos):
                    scoresView(screen, difficulte, 9)
                if clickable_area_retour.collidepoint(event.pos):
                    menuLevels(screen, difficulte)

            pygame.display.flip()

def scoresView(screen, difficulte,level):
    screen.fill((0,105,102))

    #définition des polices
    titleFont = pygame.font.Font("Ressources/go3v2.ttf", 100)
    bodyFont = pygame.font.Font("Ressources/go3v2.ttf", 40)
    subMenuFont = pygame.font.Font("Ressources/go3v2.ttf", 60)


    #ajout à l'écran
    screen.blit(titleFont.render(str(difficulte) + "x" + str(difficulte) + " - Niv. " + str(level) , True, (0, 0, 0)), (300, 30))
    screen.blit(subMenuFont.render("RETOUR", True, (0, 0, 0)), (10, 650))
   
    #zones clickables
    clickable_area_retour = pygame.Rect((10, 650), (240, 50))

    #chargement des données de score
    lvlScores = importData("scores", difficulte, level)

    #affichage des données de score
    i = 0
    y = 150

    if len(lvlScores) == 0: #cas ou l'utilisateur n'a pas joué de partie pour le niveau
        screen.blit(bodyFont.render("Vous n'avez pas encore joué de partie", True, (0, 0, 0)), (200, 300))
        screen.blit(bodyFont.render("pour ce niveau", True, (0, 0, 0)), (420, 355))
    else: #sinon j'affiche tous les scores obtenus pour le niveau en question 
        for score in lvlScores: 
            scoreMinutes = int(score/60)
            scoreSeconds = int(score % 60)
            screen.blit(bodyFont.render(str(i + 1) + " -    " + str(scoreMinutes) + " : " + str(scoreSeconds), True, (0, 0, 0)), (450, y))
            i+=1
            y+=45

    scoresViewActive = True

    while scoresViewActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == MOUSEBUTTONDOWN:
                if clickable_area_retour.collidepoint(event.pos):
                    menuScores(screen, difficulte)

            pygame.display.flip()

def definterface():

    pygame.init()
    WINDOW_SIZE = [1080, 720]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Futoshiki")  # titre de la fenetre

    Icone = pygame.image.load("Ressources/assets/icone.jpg")  # lecture de l'icone
    pygame.display.set_icon(Icone)  # mettre l'icone
    
    menuAccueil(screen)

def importData(file, diff, niveau):
    with open(file + ".json") as grids:
        grids_dict = json.load(grids)
    return grids_dict[str(diff) + "x" + str(diff)]["level" + str(niveau)]
        

definterface()
