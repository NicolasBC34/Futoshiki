

import pygame
import sys

pygame.init()
WINDOW_SIZE = [1080, 720]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Solveur")  # titre de la fenetre
dim = 4
dim_V = (2*dim)-1
grille_rectangles = [[0] * dim_V for i in range(dim_V)]
grille_valeurs = [[0] * dim_V for i in range(dim_V)]

running = True
color = (255, 255, 255)
color_bg = (0, 105, 102)
color_menus = (0, 70, 67)


marS = int((((WINDOW_SIZE[1] * 0.8) / dim) / 6)) # marge des rectangles
marC = 101
cot = int((((WINDOW_SIZE[1] * 0.9) / dim) / 3))
marge_haut = 100
marge_gauche = ((WINDOW_SIZE[0] - (dim * (cot + cot) - cot)) / 2)
from Baktrak import Solveur, AfficheG
screen.fill(color_bg)
pygame.display.update()
def affiche_grille(grille_rectangles):
    for x in range(dim_V):
        for y in range(dim_V):
            if (x % 2 == 1 and y % 2 == 1):
                grille_rectangles[x][y] = 0
            else:
                if( x % 2 == 1 or y % 2 == 1):
                    rect = pygame.draw.rect(screen, color ,pygame.Rect(x * (cot + marS) + marge_gauche , y * (cot + marS) +
                                                                marge_haut, cot, cot), 2 )
                    pygame.display.update()
                    grille_rectangles[x][y] = rect
                else :
                    rect = pygame.draw.rect(screen, color, pygame.Rect(x * (cot + marS) + marge_gauche , y * (cot + marS) +
                                                           marge_haut, cot, cot))
                    grille_rectangles[x][y] = rect
                    pygame.display.update()

def is_valeur(i,j): #teste si une case est éligible a avoir une valeur (cases dont les coordonnées sont paires)
    return (i % 2 == 0 and j % 2 ==0)

def dest(grille, i, j): #donne les coordonées exactes pour blit les nombres dans les cases
    return [(grille[i][j].x - 3), (grille[i][j].y - 4)]


psp = pygame.image.load("Pspé.png")
p0 = pygame.image.load("P0.png")
p1 = pygame.image.load("P1.png")
p2 = pygame.image.load("P2.png")
p3 = pygame.image.load("P3.png")
p4 = pygame.image.load("P4.png")
f1 = pygame.image.load("fleche_gauche.png")
f2 = pygame.image.load("fleche_haut.png")
f3 = pygame.image.load("fleche_droit.png")
f4 = pygame.image.load("fleche_bas.png")
def affichageN():

    p1_C = p1.get_rect(topleft = (10, 20 + marge_haut))
    p2_C = p2.get_rect(topleft = (10, 120 + marge_haut))
    p3_C = p3.get_rect(topleft = (10, 220 + marge_haut))
    p4_C = p4.get_rect(topleft = (10, 320 + marge_haut))
    f1_C = f1.get_rect(topleft = (110, 20 + marge_haut))
    f2_C = f2.get_rect(topleft = (110, 120 + marge_haut))
    f3_C = f3.get_rect(topleft = (110, 220 + marge_haut))
    f4_C = f4.get_rect(topleft = (110, 320 + marge_haut))

    screen.blit(p1, (10, 20 + marge_haut))
    screen.blit(p2, (10, 120 + marge_haut))
    screen.blit(p3, (10, 220 + marge_haut))
    screen.blit(p4, (10, 320 + marge_haut))
    screen.blit(f1, (110, 20 + marge_haut))
    screen.blit(f2, (110, 120 + marge_haut))
    screen.blit(f3, (110, 220 + marge_haut))
    screen.blit(f4, (110, 320 + marge_haut))
    return {p0 : "blanc", p1 : p1_C, p2 : p2_C, p3 : p3_C, p4 : p4_C, f1 : f1_C, f2 : f2_C, f3 : f3_C, f4 : f4_C, psp : "tutu"}


def get_cle(dict, val):  #pour récupérer la clé d'un dico a partir d'une valeur
    for k, v in dict.items():
        if v == val:
            return k

def click_chiffre( li, grille, grilleV, x, y, pos):
    for val in li.values():
        if (val != "blanc" and val != "tutu") and val.collidepoint(pos):
            if grilleV[x][y] != 0:
                if(x % 2 == 1 or y % 2 == 1):
                    screen.blit(get_cle(li, "tutu"), grille[x][y])
                else:
                    screen.blit(get_cle(li, "blanc"), grille[x][y])
            screen.blit(get_cle(li, val), dest(grille, x, y))
            key = get_cle(li, val)
            for i, k in enumerate(li):
                if k == key:
                    grilleV[x][y] = i
    for a in range(dim_V):
        for b in range(dim_V):
            if grilleV[a][b] == 5 or grilleV[a][b] == 6:
                grilleV[a][b] = '<'
            if grilleV[a][b] == 7 or grilleV[a][b] == 8:
                grilleV[a][b] = '>'




def renvoie_coord(grille, pos):
    for i in range(dim_V):
        for j in range(dim_V):
            if grille[i][j] != 0 and grille[i][j].collidepoint(pos):
                return (i,j)
    return (-1, -1)


def pr(grille):
    for i in range(dim_V):
        for j in range(dim_V):
            print(grille[j][i], end="")
        print(" ")

list_val={1 : p1, 2 : p2, 3 : p3, 4 : p4}
def recons(grilleV, grilleRect, li):
    for i in range(dim_V):
        for j in range(dim_V):
            if j % 2 == 0 and i % 2 == 0:
                screen.blit(li[grilleV[i][j]], dest(grilleRect, i, j))


font = pygame.font.SysFont("Times New Roman, Arial", 50)
bouton = font.render("Résoudre", True, color)
bouton_C = bouton.get_rect(topleft = (40, 550))
screen.blit(bouton, (40, 550))

affiche_grille(grille_rectangles)
li = affichageN()
pygame.display.update()


#screen.blit(p1,dest(grille_rectangles, 0, 0))
#screen.blit(p1,dest(grille_rectangles, 4, 0))
pygame.display.update()
clicked = False
TabCell=[[0]*dim_V for i in range(dim_V)]
for i in range(dim_V):
    for j in range(dim_V):
        print(grille_rectangles[i][j])
X = -1
Y = -1
nbC = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            #sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_C.collidepoint( pygame.mouse.get_pos()):
                if Solveur(grille_valeurs, dim_V, dim):
                    AfficheG(grille_valeurs, dim_V)
                    recons(grille_valeurs, grille_rectangles, list_val)
                    pygame.display.update()
                    print("<---------------------------->")
                else:
                    print("Impossible à résoudre")
            if(X != -1 and Y != -1):
                click_chiffre(li, grille_rectangles, grille_valeurs, X, Y, pygame.mouse.get_pos())
            X = renvoie_coord(grille_rectangles, pygame.mouse.get_pos())[0]
            Y = renvoie_coord(grille_rectangles, pygame.mouse.get_pos())[1]
            pygame.display.update()
    if event.type == pygame.MOUSEBUTTONUP:
        clicked = False
pr(grille_valeurs)
