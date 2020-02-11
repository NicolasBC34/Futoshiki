def cherche_case_vide(grille):
    ligne = 0
    col = 0
    resultat = False
    for i in range(difficulte):
        for j in range(difficulte):
            if ((grille[i][j] == 0) and (resultat == False)):
                ligne = i
                col = j
                resultat = True
    return resultat, ligne , col

def peut_etre_attribuer(grille_base, grille, ligne, col, val):
    resultat = True
    if ((grille_base[ligne][col] % 10) != 0):
        if (((grille_base[ligne][col] % 10) == 1) or ((grille_base[ligne][col] % 10) == 2.5) or ((grille_base[ligne][col] % 10) == 3.5)):
            if ((val >= grille[ligne+1][col]) and (grille[ligne+1][col] != 0)):
                resultat = False
        if (((grille_base[ligne][col] % 10) == 2) or ((grille_base[ligne][col] % 10) == 3) or ((grille_base[ligne][col] % 10) == 4)):
            if ((val <= grille[ligne+1][col]) and (grille[ligne+1][col] != 0)):
                resultat = False
        if (((grille_base[ligne][col] % 10) == 0.5) or ((grille_base[ligne][col] % 10) == 2.5) or ((grille_base[ligne][col] % 10) == 3)):
            if ((val >= grille[ligne][col+1]) and (grille[ligne][col+1] != 0)):
                resultat = False
        if (((grille_base[ligne][col] % 10) == 1.5) or ((grille_base[ligne][col] % 10) == 3.5) or ((grille_base[ligne][col] % 10) == 4)):
            if ((val <= grille[ligne][col+1]) and (grille[ligne][col+1] != 0)):
                resultat = False
    if (col > 0):
        if (((grille_base[ligne][col-1] % 10) == 0.5) or ((grille_base[ligne][col-1] % 10) == 2.5) or ((grille_base[ligne][col-1] % 10) == 3)):
            if ((val <= grille[ligne][col-1]) and (grille[ligne][col-1] != 0)):
                resultat = False
        elif (((grille_base[ligne][col-1] % 10) == 1.5) or ((grille_base[ligne][col-1] % 10) == 3.5) or ((grille_base[ligne][col-1] % 10) == 4)):
            if ((val >= grille[ligne][col-1]) and (grille[ligne][col-1] != 0)):
                resultat = False
    if (ligne > 0):
        if (((grille_base[ligne-1][col] % 10) == 1) or ((grille_base[ligne-1][col] % 10) == 2.5) or ((grille_base[ligne-1][col] % 10) == 3.5)):
            if ((val <= grille[ligne-1][col]) and (grille[ligne-1][col] != 0)):
                resultat = False
        elif (((grille_base[ligne-1][col] % 10) == 2) or ((grille_base[ligne-1][col] % 10) == 3) or ((grille_base[ligne-1][col] % 10) == 4)):
            if ((val >= grille[ligne-1][col]) and (grille[ligne-1][col] != 0)):
                resultat = False

    for i in range(difficulte):
        if ((i != ligne) and (grille[i][col] == val)):
            resultat = False
        if ((i != col) and (grille[ligne][i] == val)):
            resultat = False
    return resultat


def solveur(grille):
    i = 0
    j = 0
    if (cherche_case_vide(grille)[0] == False):
        return True, grille
    ligne = cherche_case_vide(grille)[1]
    col = cherche_case_vide(grille)[2]
    for val in range(1, difficulte+1):
        if (peut_etre_attribuer(grille_base, grille, ligne, col, val)):
            grille[ligne][col] = val
            if (solveur(grille)):
                return True, grille
            grille[ligne][col] = 0

    return False



difficulte = 4
grille_base = [0, 0, 2, 0], [0.5, 0, 0, 0], [0, 20, 1.5, 2], [0, 0, 10, 0]

grille = [[0] * difficulte for i in range(difficulte)] #Fabrique la grille avec les numéros de base
for a in range(difficulte):
    for b in range(difficulte):
        if (grille_base[a][b] != 0):
            if (grille_base[a][b] > 89):
                grille[a][b] = 9
            elif (grille_base[a][b] > 79):
                grille[a][b] = 8
            elif (grille_base[a][b] > 69):
                grille[a][b] = 7
            elif (grille_base[a][b] > 59):
                grille[a][b] = 6
            elif (grille_base[a][b] > 49):
                grille[a][b] = 5
            elif (grille_base[a][b] > 39):
                grille[a][b] = 4
            elif (grille_base[a][b] > 29):
                grille[a][b] = 3
            elif (grille_base[a][b] > 19):
                grille[a][b] = 2
            elif (grille_base[a][b] > 9):
                grille[a][b] = 1
        else:
            grille[a][b] = 0

print(solveur(grille)[1])
