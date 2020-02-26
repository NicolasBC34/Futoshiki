#! /usr/bin/python3
import sys,random


#initialisation de la grille avec des nombres aléatoires


print("<--------------------->")
def AfficheG(grille,D):
    for i in range(D):
        for j in range(D):
            print(grille[i][j],end='')
        print("")
def GenRandGrille(grille,D):
    compte=0
    for i in range(D):              #génere un grille 4*4 avc 3 chiffres a des endroits aléatoires
        for j in range(D):
            if(compte <= 50 and random.randint(0,1)):
                grille[i][j]=random.randint(1,D)
            else:
                grille[i][j]=0
                compte+=1
            DejaPres(i,j,grille)

def DejaPres(x,y,grille):                   #fonction qui vérifie si une cellule a un valeur déja présente en horizontale et verticale (=sudoku)
    for i in range(len(grille[0])):
        if(i!=x and grille[i][y]==grille[x][y]):
            grille[x][y]=0
            return 1
    for j in range(len(grille[0])):
        if(j!=y and grille[x][j]==grille[x][y]):
            grille[x][y]=0
            return 1
    return 0        

def Chercher_case_vide(grille,i,j,D):
    res=True
    while(grille[i][j]!=0):
        if((i==(D-1) and j==(D-1))):
            res=False
            return (i,j,res)
        if(j==(D-1)):
            i+=1
            j=-1
        j+=1    
    return (i,j,res)    
  
   

def Peut_etre_attr(grille,x,y,val):
    for i in range(len(grille[0])):
        if(i!=x and grille[i][y]==val):
            return 0
    for j in range(len(grille[0])):
        if(j!=y and grille[x][j]==val):
            return 0
    return 1        


def Solveur(grille,D):
    i=j=0
    if (not Chercher_case_vide(grille,i,j,D)[2]):
        return True
    i=Chercher_case_vide(grille,i,j,D)[0]
    j=Chercher_case_vide(grille,i,j,D)[1]
    cellule=Cell(D,i,j)           #tableau de cellules pour acceder aux possibilitées propres a chaque case de la grille
    cellule.update(grille)
    if(cellule.nbrChoix()==1):
        grille[i][j]=cellule.ChoixUnique()
        #print("BRAVO")
        if(Solveur(grille,D)):
            return True
    for val in range(1,(D+1)):
        if(Peut_etre_attr(grille,i,j,val)):
            grille[i][j]=val
            if(Solveur(grille,D)):
                return True
            grille[i][j]=0
    return False

###########################################################
class Cell:
    taille=0
    def __init__(self,diff,x,y):
        self.choix=[[0]for i in range(diff)]
        k=0
        while(k<=(diff-1)):
            self.choix[k]=1
            k+=1
        self.taille=diff
        self.abs=x
        self.ord=y

    def nbrChoix(self):
        som=0
        for i in range(self.taille):
            if self.choix[i]:
                som+=1
        return som

    def update(self,grille):
        for i in range(self.taille):                    #si l
            if(i!=self.abs and grille[i][self.ord]!=0):
                self.choix[grille[i][self.ord]-1]=0
        for j in range(self.taille):
            if(j!=self.ord and grille[self.abs][j]!=0):
                self.choix[grille[self.abs][j]-1]=0
    
    def ChoixUnique(self):
        u=0
        if(self.nbrChoix()==1):
            while(self.choix[u]==0):
                u+=1
            return u+1

    def AfficheChoix(self):
        for i in self.choix:
            if(self.choix[i]!=0):
                print(i,end="")
        print("") 
###########################################################""   

D=int(sys.argv[1])

grille=[[0]*D for i in range(D)]            #génere une grille 4*4 avec des 0 partout (4 '0' pour i de 0 a 3)
TabCell=[[0]*D for i in range(D)]   
#TestG=[[7,0,5,0,0,9,0,2,0],[0,8,4,0,0,2,0,0,0],[5,0,0,0,0,0,0,0,0,0],[0,3,2,0,0,0,0,0,0],[0,0,3,6,7,0,0,9,0],[0,0,0,0,0,8,0,4,0],[0,0,0,0,2,0,4,0,9],[0,5,0,2,0,0,0,6,0],[0,9,1,0,4,0,8,0,0]]
GenRandGrille(grille,D)
AfficheG(grille,D)
# Solveur(TestG,D)
#AfficheG(TestG,D)
print("Résolution de la grille . . .",'\n')
if(Solveur(grille,D)):
    AfficheG(grille,D)
else:
    print("Cette grille n'a pas de solution")
c=Cell(D,0,1)
c.update(grille)
c.AfficheChoix()
            


