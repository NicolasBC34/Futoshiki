#! /usr/bin/python3
import sys,random
from tkinter import *
import tkinter.font as tkFont


grille=[[0]*4 for i in range(4)] #grille de 4*4 initialisée a 0, sera composée d'entry
grilleLi=[[0]*4 for i in range(4)] #copie de la grille, c'est une liste avec les valeurs de la grille
fenetre=Tk()
fenetre.title=("la glissade")

myFont=tkFont.Font(size=20)
#fenetre.geometry("800x500")

def DejaPres(x,y,grille,Entry):                   #fonction qui vérifie si une cellule a un valeur déja présente en horizontale et verticale (=sudoku)
    for i in range(4):
        if(i!=x and grille[i][y]==int(Entry.get())):
            Entry.configure({"background":"red","fg":"white"})
            return 1
    for j in range(4):
        if(j!=y and grille[x][j]==int(Entry.get())):
            Entry.configure({"background":"red","fg":"white"})
            return 1
    # si l'entier est au bon endroit, on reset la couleur de la case        
    Entry.configure({"background":"white","fg":"black"})
    return 0        
    

# Affichage de la grille
for i in range(4):
    for j in range(4):
        grille[i][j]=Entry(fenetre,width=5,font=myFont,justify=CENTER)  # grille est la liste des entry(champs)
        grille[i][j].grid(column=i,row=j)                               # interface de la grille
        #grille[i][j].insert(1,random.randint(0,3))                      # test en complétant la grille en entier avec des entiers random entre 0 et 3
        #grilleLi[i][j]=int(grille[i][j].get())                          # get sort la valeur d'une entrée en chaine

print(grilleLi)
def ChampInt(Entry):            #vérifie si l'entier dans le champs est entre 0 et 4,renvoie 1, efface le contenu sinon et renvoie 0
    if not(int(Entry.get()) in range(4)):
        Entry.delete(0,'end')
        return 0
    return 1
        

def contrl(liste,champs):        # fonction qui évalue la position des valeurs, colorie en rouge le champs si la valeur n'est 
    for i in range(4):           # pas au bon endroit
        for j in range(4):
            if(ChampInt(champs[i][j])):
                grilleLi[i][j]=int(grille[i][j].get())
                DejaPres(i,j,liste,champs[i][j])
            else:    
                liste[i][j]=-1
            

Button_ctrl=Button(master=fenetre,text="click stp",command=lambda:contrl(grilleLi,grille)) # il faut clicker entre chaque modification de valeurs pour évaluer si 
Button_ctrl.grid(column=2,row=4)                                                           # la valeur est au bon endroit ou pas

    
    
fenetre.mainloop()
