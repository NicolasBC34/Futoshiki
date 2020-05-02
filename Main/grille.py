grille1 = [[0]*4 for i in range(4)]
grille1[0][0] = 20
grille1[1][0] = 11.5
grille1[3][2] = 50
grille1[2][2] = 3.5

grille2 = [[0]*7 for i in range(7)]

def afficheGrille(grille):
  for i in range(len(grille[0])):
    for j in range(len(grille[0])):
      print("|",grille[i][j],"|", end="")
    print(" ")


def gestSignes(val, grille, i, j):
  if val % 10 == 0.5:
    grille[i][j+1] = '<' #gauche
  elif val % 10 == 1.5:
    grille[i][j+1] = '>' #droite
  elif val % 10 == 2.5:
    grille[i][j+1] = '<'
    grille[i+1][j] = '<' #haut
  elif val % 10 == 3.5:
    grille[i][j+1] = '>'
    grille[i+1][j] = '<'
  elif val % 10 == 3:
    grille[i][j+1] = '<'
    grille[i+1][j] = '>' #bas
  elif val % 10 == 4:
    grille[i][j+1] = '>'
    grille[i+1][j] = '>'
  elif val % 10 == 1:
    grille[i+1][j] = '<'
  elif val % 10 == 2:
    grille[i+1][j] = '>'

  



def afficheVal(grilleA, grilleB): 
  for i in range(len(grilleA)):
    for j in range(len(grilleA)):
      if grilleA[i][j] != 0:
        gestSignes(grilleA[i][j], grilleB, 2*i, 2*j)
        if (grilleA[i][j] // 10 != 0 and grilleA[i][j] // 10 <=len(grilleA)):
          grilleB[2*i][2*j] = int (grilleA[i][j] // 10)



G1 = [[1.5, 2, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0.5, 0.5, 0]]

afficheVal(G1, grille2)

afficheGrille(grille2)
print(0 % 10)