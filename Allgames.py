from tkinter import *
from random import *
import math
import random
from tkinter import messagebox
lf=1



def jp():
    global lf,tentatives
    if lf==1:
        Mafenetretemp.destroy()
        lf=0 
    L=1000
    H=600
    ##génération du nombre
    hasard=random.randint(1,10000)
    print(hasard)

    f=Tk()
    f.title("Just price")
    Canevas=Canvas(f, width=L, height=H, background="gold")


    tentatives=16
    ##nombre que met le joueur
    nombre = StringVar()
    nombre.set("Entrez 0 pour commencer")
    reponse = StringVar()
    reponse.set("On joue !")
    ##barre où le joueur met son nombre
    champs=Entry(f, textvariable=nombre, font=100)
    ##création du jeu
    def jeu(event):
        global tentatives
        print(hasard)
        nbre=int(nombre.get())
        ##définir le gain du joueur ou la position de son nombre par rapport au nombre aleatoire choisi 
        if tentatives>=1:
            tentatives -=1
            if hasard==nbre:
                reponse.set("Bien joué !")
                f.after(5000,f.destroy)
                tent()
            elif hasard < nbre :
                reponse.set("Plus petit")
                tent()
            elif hasard > nbre:
                reponse.set("Plus grand")
                tent()
        else :
            reponse.set("Dommage... Le nombre était : "+str(hasard))
            f.after(5000,f.destroy)
            tent()



    champs.focus_set()

    ##quand la touche entrée est tapée, la fonction se lance
    champs.bind("<Return>", jeu)
    champs.pack(pady=300)

    ##afficher def jeu()
    Label1 = Label(f,textvariable=reponse)
    Label1.pack()
    ##nombre de tentatives restantes
    def tent():
        global tentatives
        Canevas.delete("tenta")
        Canevas.create_text(L/2,15,font=50,text="Nombre de tentatives :",tag="tenta")
        Canevas.create_text(L/2+115,15,font=50,text=tentatives,tag="tenta")

    Canevas.pack(padx=5,pady=5)
    champs.focus_set()
    f.mainloop()



def ttt():
    global lf,c,l,j,q,w,li,co,di,dt,L,B,D,pa,ep,tr
    if lf==1:
        Mafenetretemp.destroy()
        lf=0 
    H=700 ## taille de la fenetre
    root=Tk()
    canvas=Canvas(root,height= H, width= H,bg='skyblue')
    canvas.pack()
    ################
    ## Paramètres ##
    ################
    tail=H//3 ## taille des cases
    c=randint(0,1) ## changement de joueur
    v=tail//3 ## rayon cercle
    l=0 ## yc des ronds
    j=0 ## xc des ronds
    q=0 ## yc des croix
    w=0 ##xc des croix
    li=0 ## ajouter dans les sous listes des lignes et colonnes
    co=0 ## ajouter dans les sous listes des lignes et colonnes
    di=0 ## pour bot difficile liste des lignes et colonnes
    dt=0## pour bot difficile liste des lignes et colonnes
    L=[[0,0,0],[0,0,0],[0,0,0]]##liste pour les lignes
    B=[[0,0,0],[0,0,0],[0,0,0]]## liste pour les colonnes
    D=[[0,0,0],[0,0,0]] ## liste pour les diagonales
    pa=4 ## épaisseur des lignes, ronds et des croix
    ep=0 ## nombre de manche gagné par les ronds
    tr=0 ## nombre de manche gagné par les croix
    #################

    ## Création des 9 cases ##
    canvas.create_line(tail+1,0,tail+1,H, fill="black",width= pa-2)
    canvas.create_line((tail*2)+2,0,(tail*2)+2,H, fill="black",width= pa-2)
    canvas.create_line(0,tail+1,H,tail+1, fill="black",width= pa-2)
    canvas.create_line(0,(tail*2)+2,H,(tail*2)+2, fill="black",width= pa-2)
    ##########################"

    def pointA(event): ## fonction de base pour créer les ronds et les croix pour le mode 2 joueurs
        global c,j,l,w,q,li,co,fort,ep,xc,yc
        xc,yc=event.x,event.y
        if c%2==0:    ## Les ronds ##
            easteregg()
            li=xc//tail
            co=yc//tail        ### Calcul de la position pour créer les ronds grace aux coordonnées de la souris et de la taille de la case ###
            j=(li)*tail+tail/2
            l=(co)*tail+tail/2
            if L[co][li]==0: ## pour savoir si la case est vide pour pouvoir jouer, si dans la case il y a déjà une figure on ne peux pas jouer ##
                liste1() ## pour ajouter a la liste en fonction de la position des croix ##
                canvas.create_oval(j-v,l-v,j+v,l+v, outline="black",  width=pa,tag= "b") ##création des ronds ##
                c=c+1  ## ajout de 1 pour que ça soit à l'adversaire de jouer ##
                score() ## appel de la fonction "score" pour savoir si un des deux joueurs a gagné ##
        elif c%2==1 and N==2: ## les croix ##
            easteregg()
            li=xc//tail
            co=yc//tail          ### Calcul de la position pour créer les croix grace aux coordonnées de la souris et de la taille de la case ###
            w=(li)*tail+tail/2
            q=(co)*tail+tail/2
            if L[co][li]==0: ## pour savoir si la case est vide pour pouvoir jouer, si dans la case il y a déjà une figure on ne peux pas jouer ##
                liste1() ## pour ajouter a la liste en fonction de la position des croix ##
                canvas.create_line(w-v,q-v, w+v, q+v, fill="black", width=pa,tag= "b") ## création des croix ##
                canvas.create_line(w-v, q+v, w+v, q-v, fill="black", width=pa,tag= "b")
                c=c+1
                score()
        elif c%2==1 and N==1 and ft==1:  ## appel de la fonction pour le bot facile ##
            bot()
        elif c%2==1 and N==1 and ft==2: ## appel de la fonction pour le bots difficile ##
            botFort()
    ######################################

    def easteregg(): ## petit easteregg, si on touche une certaine position on gagne des points
        global xc,yc,ep
        if xc==H/2 and yc==H/2 or xc==tail and yc==tail:
                ep+=20
                pointR()
    ######################################

    def bot(): ## fonction du bot facile qui choisit aléatoirement une place sur la grille ##
        global c,u,w,p,q,L,m,dt,di
        if c%2==1:
            u=(randint(0,H))//tail  ### au hasard des coordonnées sont choisis comme si on utilisait la souris avec randint() pour ensuite calculer la position pour créer les croix ###
            m=(randint(0,H))//tail
            if L[m][u]==0:    ## pour savoir si la case est vide pour pouvoir jouer, si dans la case il y a déjà une figure on ne peux pas jouer ##
                w=u*tail+tail//2     ### Calcul de la position pour créer les croix grace aux coordonnées de la souris et de la taille de la case ###
                q=m*tail+tail//2
                dt=w  ## ajouter à la liste pour le bot difficile lorsqu'il fait appel au bot facile ##
                di=q  ## ajouter à la liste pour le bot difficile lorsqu'il fait appel au bot facile ##
                liste1()
                canvas.create_line(w-v,q-v, w+v, q+v, fill="black", width=pa,tag= "b")  ## création des croix ##
                canvas.create_line(w-v, q+v, w+v, q-v, fill="black", width=pa,tag= "b")
                c=c+1
                score()
            elif L[m][u]!=0:
                bot()
    ######################################

    def croix(): ## fonction qui crée les croix pour le bot difficile pour éviter d'ajouter des lignes pour rien ##
        global q,w,di,dt,c
        w=dt+tail//2     ### Calcul de la position pour créer les croix grace aux coordonnées de la souris et de la taille de la case ###
        q=di+tail//2
        canvas.create_line(w-v,q-v, w+v, q+v, fill="black", width=pa,tag= "b") ## création des croix ##
        canvas.create_line(w-v, q+v, w+v, q-v, fill="black", width=pa,tag= "b")
        c+=1 ## ajout de 1 pour que ça soit à l'adversaire de jouer ##
    ######################################

    def botFort(): ## fonction pour le bot difficile qui analyse les coups pour bloquer l'adversaire et gagner ##
        global c,L,di,dt,B,D,q,w
        if c%2==1:
            dt=0 ## variable pour ajouter à la liste pour les scores ##
            di=0 ## variable pour ajouter à la liste pour les scores ##
            po=0
            if not 1 in L[0] and not 1 in L[1] and not 1 in L[2]:  ## si c'est le premier à jouer, il va choisir aléatoirement une case dans les 4 coins de la grille
                dt=choice([0,H-tail]) ## il choisit aléatoirement entre les quatre coins de la grille si c'est le premier à jouer ##
                di=choice([0,H-tail])
                if L[di//tail][dt//tail]==0: ## pour savoir si la case est vide pour pouvoir jouer, si dans la case il y a déjà une figure on ne peux pas jouer ##
                    liste1()
                    w=((dt//tail)*tail)+tail//2 ## Calcul de la position pour créer les croix grace aux coordonnées de la souris et de la taille de la case ##
                    q=((di//tail)*tail)+tail//2
                    canvas.create_line(w-v,q-v, w+v, q+v, fill="black", width=pa,tag= "b")   ## création des croix ##
                    canvas.create_line(w-v, q+v, w+v, q-v, fill="black", width=pa,tag= "b")
                    c+=1
                    score()
            for s in range(3): ## si c'est le deuxième à jouer et que les ronds ont joué n'importe où sauf au milieu il va jouer au milieu ##
                for y in range(3):
                    if L[s][y]==1:
                        po+=1 ## savoir le nombre de fois que les ronds ont joué pour determiner si il va jouer au milieu en deuxième ##
            if po==1 and L[1][1]==0: ## pour savoir si c'est le deuxième à jouer et si la case est vide pour pouvoir jouer, si dans la case il y a déjà une figure on ne peux pas jouer ##
                dt=tail ## pour ajouter à la bonne place dans la liste ##
                di=tail ## pour ajouter à la bonne place dans la liste ##
                liste1()
                croix()
                score()       #################################################################################################################
            dt=0
            di=0
            ##### Etude des possibilités pour qu'il gagne grace à la liste ###
            if L[0][1]==2 and L[0][2]==2 and c%2==1 and L[0][0]==0 or L[1][0]==2 and L[2][0]==2 and c%2==1 and L[0][0]==0 or L[1][1]==2 and L[2][2]==2 and c%2==1 and L[0][0]==0: #### Différentes conditions pour étudier chaque coup ####
                liste1() ## pour ajouter à la liste lorsqu'il a jouer
                croix() ## pour créer les croix ##
                score() ## appel de la fonction score pour déterminer si soit les ronds ou les croix ont gagné ##
            dt+=tail
            if L[0][0]==2 and L[0][2]==2 and c%2==1 and L[0][1]==0 or L[1][1]==2 and L[2][1]==2 and c%2==1 and L[0][1]==0:
                liste1()
                croix()
                score()
            dt+=tail
            if L[0][0]==2 and L[0][1]==2 and c%2==1 and L[0][2]==0 or L[1][1]==2 and L[2][0]==2 and c%2==1 and L[0][2]==0 or L[1][2]==2 and L[2][2]==2 and c%2==1 and L[0][2]==0:
                liste1()
                croix()
                score()
            dt=dt-(2*tail)
            di+=tail
            if L[0][0]==2 and L[2][0]==2 and c%2==1 and L[1][0]==0 or L[1][1]==2 and L[1][2]==2 and c%2==1 and L[1][0]==0:
                liste1()
                croix()
                score()
            dt+=tail
            if L[0][0]==2 and L[2][2]==2 and c%2==1 and L[1][1]==0 or L[0][2]==2 and L[2][0]==2 and c%2==1 and L[1][1]==0 or L[1][0]==2 and L[1][2]==2 and c%2==1 and L[1][1]==0 or L[1][0]==2 and L[1][2]==2 and c%2==1 and L[1][1]==0 :
                liste1()
                croix()
                score()
            dt+=tail
            if L[1][0]==2 and L[1][1]==2 and c%2==1 and L[1][2]==0 or L[0][2]==2 and L[2][2]==2 and c%2==1 and L[1][2]==0 :
                liste1()
                croix()
                score()
            dt=dt-(2*tail)
            di+=tail
            if L[0][0]==2 and L[1][0]==2 and c%2==1 and L[2][0]==0 or L[1][1]==2 and L[0][2]==2 and c%2==1 and L[2][0]==0 or L[2][1]==2 and L[2][2]==2 and c%2==1 and L[2][0]==0 :
                liste1()
                croix()
                score()
            dt+=tail
            if L[0][1]==2 and L[1][1]==2 and c%2==1 and L[2][1]==0 or L[2][0]==2 and L[2][2]==2 and c%2==1 and L[2][1]==0 :
                liste1()
                croix()
                score()
            dt+=tail
            if L[0][2]==2 and L[1][2]==2 and c%2==1 and L[2][2]==0 or L[0][0]==2 and L[1][1]==2 and c%2==1 and L[2][2]==0 or L[2][0]==2 and L[2][1]==2 and c%2==1 and L[2][2]==0 :
                liste1()
                croix()
                score()
            dt=dt-(2*tail)
            di=di-(2*tail)
            ##############################################################

            ##### Etudes des possibilités pour bloquer les ronds et les empêcher de gagner ###
            if L[0][1]==1 and L[0][2]==1 and c%2==1 and L[0][0]==0 or L[1][0]==1 and L[2][0]==1 and c%2==1 and L[0][0]==0 or L[1][1]==1 and L[2][2]==1 and c%2==1 and L[0][0]==0 :
                liste1() ## pour ajouter à la liste lorsqu'il a jouer
                croix() ## pour créer les croix ##
                score() ## appel de la fonction score pour déterminer si soit les ronds ou les croix ont gagné ##
            dt+=tail
            if L[0][0]==1 and L[0][2]==1 and c%2==1 and L[0][1]==0 or L[1][1]==1 and L[2][1]==1 and c%2==1 and L[0][1]==0 :
                liste1()
                croix()
                score()
            dt+=tail
            if L[0][0]==1 and L[0][1]==1 and c%2==1 and L[0][2]==0 or L[1][1]==1 and L[2][0]==1 and c%2==1 and L[0][2]==0 or L[1][2]==1 and L[2][2]==1 and c%2==1 and L[0][2]==0 :
                liste1()
                croix()
                score()
            dt=dt-(2*tail)
            di+=tail
            if L[0][0]==1 and L[2][0]==1 and c%2==1 and L[1][0]==0 or L[1][1]==1 and L[1][2]==1 and c%2==1 and L[1][0]==0 :
                liste1()
                croix()
                score()
            dt+=tail
            if L[0][0]==1 and L[2][2]==1 and c%2==1 and L[1][1]==0 or L[0][2]==1 and L[2][0]==1 and c%2==1 and L[1][1]==0 or L[1][0]==1 and L[1][2]==1 and c%2==1 and L[1][1]==0 or L[1][0]==1 and L[1][2]==1 and c%2==1 and L[1][1]==0 :
                liste1()
                croix()
                score()
            dt+=tail
            if L[1][0]==1 and L[1][1]==1 and c%2==1 and L[1][2]==0 or L[0][2]==1 and L[2][2]==1 and c%2==1 and L[1][2]==0 :
                liste1()
                croix()
                score()
            dt=dt-(2*tail)
            di+=tail
            if L[0][0]==1 and L[1][0]==1 and c%2==1 and L[2][0]==0 or L[1][1]==1 and L[0][2]==1 and c%2==1 and L[2][0]==0 or L[2][1]==1 and L[2][2]==1 and c%2==1 and L[2][0]==0 :
                liste1()
                croix()
                score()
            dt+=tail
            if L[0][1]==1 and L[1][1]==1 and c%2==1 and L[2][1]==0 or L[2][0]==1 and L[2][2]==1 and c%2==1 and L[2][1]==0 :
                liste1()
                croix()
                score()
            dt+=tail
            if L[0][2]==1 and L[1][2]==1 and c%2==1 and L[2][2]==0 or L[0][0]==1 and L[1][1]==1 and c%2==1 and L[2][2]==0 or L[2][0]==1 and L[2][1]==1 and c%2==1 and L[2][2]==0:
                liste1()
                croix()
                score()
            ######################
            while c%2==1:
                bot() ### Si aucune des conditions sont remplies, il va jouer aléatoirement à l'aide de la fonction du bot facile ##
    ######################################

    def liste1(): ## fonction pour ajouter aux différentes listes qui permet de savoir qui a gagné
        global li,c,co,L,B,D,u,p,m,dt,di
        p=0 ## pour ajouter à la liste des diagonales
        a=2 ## pour ajouter à la liste des diagonales
        if c%2==0: ## ajout dans les listes pour les ronds
            L[co][li]=1 ## chaque place dans la liste correspond à une case sur la grille
            B[li][co]=1 ## on ajoute à la liste des colones
            for f in range(3): ## on ajoute à la liste des diagonales
                D[0][f]=L[p][p]
                D[1][f]=L[a][p]
                a=a-1
                p=p+1
            li=0
            co=0
        if c%2==1 and N==2: ## ajout dans les listes pour les croix (2 joueurs)
            L[co][li]=2
            B[li][co]=2
            for f in range(3):
                D[0][f]=L[p][p]
                D[1][f]=L[a][p]
                a=a-1
                p=p+1
            li=0
            co=0
        elif c%2==1 and N==1 and ft==1: ## ajout dans les listes pour les croix (bot facile)
            L[m][u]=2
            B[u][m]=2
            for f in range(3):
                D[0][f]=L[p][p]
                D[1][f]=L[a][p]
                a=a-1
                p=p+1
            u=0
            m=0
        elif c%2==1 and N==1 and ft==2: ## ajout dans les listes pour les croix (bot difficile)
            pm=di//tail
            pl=dt//tail
            L[pm][pl]=2
            B[pl][pm]=2
            for f in range(3):
                D[0][f]=L[p][p]
                D[1][f]=L[a][p]
                a=a-1
                p=p+1
            pm=0
            pl=0
    ######################################

    def score(): ## fonction qui permet de savoir qui a gagné entre les rond et les croix ##
        global L,B,D,ep,tr
        thj=0 ## variable pour match nul, cela permet d'afficher que la victoire si on gagne et que la grille est remplie ##
        for i in range(3): ## boucle pour savoir si les ronds ou les croix ont gagné grace à la liste des lignes ##
            if L[i][0] ==1 and L[i][1] ==1 and L[i][2] ==1:
                messagebox.showinfo("Winner","le joueur 1 a gagné (rond), pour recommencer appuyer sur d") ## message d'information sur le gagnant ##
                thj+=1
                ep+=1 ## variable pour les nobmre de manche gagné par les ronds
                pointR() ## on appelle la fonction pour mettre à jour le score
            elif L[i][0]==2 and L[i][1]==2 and L[i][2] ==2:
                messagebox.showinfo("Winner","le joueur 2 a gagné (croix),pour recommencer appuyer sur d")
                thj+=1
                tr+=1 ## variable pour les nombre de manche gagné par les croix
                pointC()  ## on appelle la fonction pour mettre à jour le score
        for g in range(3): ## boucle pour savoir si les ronds ou les croix ont gagné grace à la liste des colonnes ##
            if B[g][0] ==1 and B[g][1] ==1 and B[g][2] ==1:
                messagebox.showinfo("Winner","le joueur 1 a gagné (rond), pour recommencer appuyer sur d")
                thj+=1
                ep+=1
                pointR()
            elif B[g][0]==2 and B[g][1]==2 and B[g][2] ==2:
                messagebox.showinfo("Winner","le joueur 2 a gagné (croix), pour recommencer appuyer sur d")
                thj+=1
                tr+=1
                pointC()
        for o in range(2): ## boucle pour savoir si les ronds ou les croix ont gagné grace à la linge des diagonales ##
            if D[o][0] ==1 and D[o][1] ==1 and D[o][2] ==1:
                messagebox.showinfo("Winner","le joueur 1 a gagné (rond), pour recommencer appuyer sur d")
                thj+=1
                ep+=1
                pointR()
            elif D[o][0]==2 and D[o][1]==2 and D[o][2] ==2 :
                messagebox.showinfo("Winner","le joueur 2 a gagné (croix), pour recommencer appuyer sur d")
                thj+=1
                tr+=1
                pointC()
        if not 0 in L[0] and not 0 in L[1] and not 0 in L[2] and thj==0: ## si toutes les cases sont jouées on va afficher match nul et si il n'y a eu 0 message avant avec la variable thj ##
            messagebox.showinfo("match nul ","match nul (aucun joueur a gagner), pour recommencer appuyer sur d")
    ######################################

    def recommencer(event): ## fonction pour recommencer une manche avec l'event pour bind une touche
        global c,li,co,L,B,D
        canvas.delete("b") ## on supprime les ronds et les croix présents sur la grille grâce au tag mis précédemment ##
        L=[[0,0,0],[0,0,0],[0,0,0]] ## initialisation des listes des lignes, colonnes et diagonales ##
        B=[[0,0,0],[0,0,0],[0,0,0]]
        D=[[0,0,0],[0,0,0]]
        c=randint(0,1) ## initialisation de la variable qui permet d'alterner entre les croix et les ronds

    def changer(): ## fonction qui sert à changer de mode de joueur
        global N,ft,tr,ep
        demande = messagebox.askquestion("Choix du nombre de joueur", "2 joueurs (oui) ou 1 joueur (non), appuyez sur d pour recommencer ?") ## on pose une question avec une boite de message pour les différents modes de joueur ##
        if demande=="yes":
            N=2 ## variable qui permet de joueur avec queqlu'un d'autre que l'ordinateur ( en mode 2 joueur )
            ep,tr=0,0 ## j'initialise mes varaible à 0 qui sert pour les manches gagné des ronds et des croix
            pointR() ## je rappelle mes fonctions pour mettre à jour l'initialisation
            pointC()
        if demande== "no":
            N=1 ## variable qui permet de jouer avec un bot
            niveau= messagebox.askquestion("niveau du bot","difficile (oui) ou facile (non) ? appuyez sur d pour recommencer, clic gauche pour faire jouer le bot ") ## on pose la question avec une boite de message pour la difficulté du bot
            if niveau =="yes":
                ft=2 ## variable qui permet de joueur avec le bot difficile
                ep,tr=0,0
                pointR()
                pointC()
            if niveau=="no":
                ft=1 ## variable qui permet de joueur avec le bot plus facile
                ep,tr=0,0
                pointR()
                pointC()
    ######################################

    def pointR(): ## fonction pour afficher des manches gagnées par ronds ##
        global ep  ## on crée des textes avec le nombre de manches gagnées et le texte rond
        canvas.delete("y") ## à chaque initialisation de la fonction on supprime le message pour le mettre à jour
        canvas.create_text(H//6,H-10, text=" ronds:",tag="y") ## et on le recrée pour mettre à jour le nombre de manches gagnées par les ronds
        canvas.create_text((H//6)+25,H-10,text= str(ep), tag="y")
        if ep==55:
            messagebox.showinfo("ERREUR","ERREUR, vous êtes trop bon ")
            canvas.destroy()
    ######################################

    def pointC(): ## fonction pour affichage des maches gagné par les croix
        global tr ## on crée des textes avec le nombre de manches gagnées et le texte croix
        canvas.delete("p") ## à chaque initialisation de la fonction on le supprime
        canvas.create_text((H//6)*5,H-10, text="croix:",tag="p") ## et on le recrée pour mettre à jour le nombre de manches gagnées par les croix
        canvas.create_text(((H//6)*5)+22,H-10,text= str(tr), tag="p")
    ######################################

    changer() ## j'appelle ma variable pour choisir le mode de joueur au lancement du programme
    canvas.bind("d", recommencer) ## je lie la touche "d" à la fonction recommencer pour pouvoir rejouer en appuyant sur d
    canvas.bind('<Button-1>', pointA) ## je lie le clic gauche à la fonction pour pouvoir jouer
    canvas.focus_set()
    bouton = Button(root,text= "mode de joueur", command=changer) ## j'ajoute un bouton pour changer le mode de jeux
    bouton.pack(padx=H/2, pady=5) ## j'ajuste la position du bouton dans la fenêtre
    root.mainloop()



def p4():
    global lf
    if lf==1:
        Mafenetretemp.destroy()
        lf=0 
    global nj,couleurjoueur,h1,h2,h3,h4,h5,h6,h7,liste
    ##Largeur et hauteur de la fenêtre, rayon du cercle
    W=700
    H=600
    R=42.5
    ##c,dc,tc == 50,100,150 pour définir la grille de jeu
    c=50
    dc=100
    tc=150
    ##liste utilisée uniquement pour définir la victoire
    liste=[["temp"]*7 for _ in range (5)]
    ##h* pour pour faire monter les pions (éviter qu'ils se superposent+)
    h1,h2,h3,h4,h5,h6,h7=5,5,5,5,5,5,5
    ##choisir la couleur des pions
    nj=randint(0,1)
    couleurjoueur=["red","yellow"]

    def attente(event):
        #défini la zone d'attente et fait apparaître un cercle sur la souris (zone définie de gauche à droite)
        i = event.x
        if i<100:
            Canevas.delete("temp")
            Canevas.create_oval(50-R,50-R,50+R,50+R,tag="temp",fill=couleurjoueur[nj%2])
        elif i>=100 and i<200:
            Canevas.delete("temp")
            Canevas.create_oval(150-R,50-R,150+R,50+R,tag="temp",fill=couleurjoueur[nj%2])
        elif i>= 200 and  i<300:
            Canevas.delete("temp")
            Canevas.create_oval(250-R,50-R,250+R,50+R,tag="temp",fill=couleurjoueur[nj%2])
        elif i>=300 and i<400:
            Canevas.delete("temp")
            Canevas.create_oval(350-R,50-R,350+R,50+R,tag="temp",fill=couleurjoueur[nj%2])
        elif i>=400 and i<500:
            Canevas.delete("temp")
            Canevas.create_oval(450-R,50-R,450+R,50+R,tag="temp",fill=couleurjoueur[nj%2])
        elif i>=500 and i<600:
            Canevas.delete("temp")
            Canevas.create_oval(550-R,50-R,550+R,50+R,tag="temp",fill=couleurjoueur[nj%2])
        elif i>=600 and i<700:
            Canevas.delete("temp")
            Canevas.create_oval(650-R,50-R,650+R,50+R,tag="temp",fill=couleurjoueur[nj%2])

    def placer(event):
        global nj,couleurjoueur,h1,h2,h3,h4,h5,h6,h7,liste
        ##défini les zones de placements des pions et les place
        i = event.x
        ##case *
        if i<100:
            ##si ça ne dépasse pas le haut de la grille de jeu
            if h1>0:
                Canevas.delete("temp")
                Canevas.create_oval(50-R,(h1*100)+50-R,50+R,(h1*100)+50+R,tag="oui",fill=couleurjoueur[nj%2])
                nj+=1
                ##fait monter les pions à chaque placement pour éviter la superposition
                for i in range(4,-1,-1):
                    if h1-1==i:
                        liste[h1-1][0]=nj%2
                h1-=1
                score()
        elif i>=100 and i<200:
            ##si ça ne dépasse pas le haut de la grille de jeu
            if h2>0:
                Canevas.delete("temp")
                Canevas.create_oval(150-R,(h2*100)+50-R,150+R,(h2*100)+50+R,tag="oui",fill=couleurjoueur[nj%2])
                nj+=1
                ##fait monter les pions à chaque placement pour éviter la superposition
                for i in range(4,-1,-1):
                    if h2-1==i:
                        liste[h2-1][1]=nj%2
                h2-=1
                score() 
        elif i>= 200 and  i<300:
            ##si ça ne dépasse pas le haut de la grille de jeu
            if h3>0:
                Canevas.delete("temp")
                Canevas.create_oval(250-R,(h3*100)+50-R,250+R,(h3*100)+50+R,tag="oui",fill=couleurjoueur[nj%2])
                nj+=1
                ##fait monter les pions à chaque placement pour éviter la superposition
                for i in range(4,-1,-1):
                    if h3-1==i:
                        liste[h3-1][2]=nj%2
                h3-=1
                score()
        elif i>=300 and i<400:
            ##si ça ne dépasse pas le haut de la grille de jeu
            if h4>0:
                Canevas.delete("temp")
                Canevas.create_oval(350-R,(h4*100)+50-R,350+R,(h4*100)+50+R,tag="oui",fill=couleurjoueur[nj%2])
                nj+=1
                ##fait monter les pions à chaque placement pour éviter la superposition
                for i in range(4,-1,-1):
                    if h4-1==i:
                        liste[h4-1][3]=nj%2
                h4-=1
                score()
        elif i>=400 and i<500:
            ##si ça ne dépasse pas le haut de la grille de jeu
            if h5>0:
                Canevas.delete("temp")
                Canevas.create_oval(450-R,(h5*100)+50-R,450+R,(h5*100)+50+R,tag="oui",fill=couleurjoueur[nj%2])
                nj+=1
                ##fait monter les pions à chaque placement pour éviter la superposition
                for i in range(4,-1,-1):
                    if h5-1==i:
                        liste[h5-1][4]=nj%2
                h5-=1
                score()
        elif i>=500 and i<600:
            ##si ça ne dépasse pas le haut de la grille de jeu
            if h6>0:
                Canevas.delete("temp")
                Canevas.create_oval(550-R,(h6*100)+50-R,550+R,(h6*100)+50+R,tag="oui",fill=couleurjoueur[nj%2])
                nj+=1
                ##fait monter les pions à chaque placement pour éviter la superposition
                for i in range(4,-1,-1):
                    if h6-1==i:
                        liste[h6-1][5]=nj%2
                h6-=1
                score()
        elif i>=600 and i<700:
            ##si ça ne dépasse pas le haut de la grille de jeu
            if h7>0:
                Canevas.delete("temp")
                Canevas.create_oval(650-R,(h7*100)+50-R,650+R,(h7*100)+50+R,tag="oui",fill=couleurjoueur[nj%2])
                nj+=1
                ##fait monter les pions à chaque placement pour éviter la superposition
                for i in range(4,-1,-1):
                    if h7-1==i:
                        liste[h7-1][6]=nj%2
                h7-=1   
                score()

    def score():
        ##pour calculer les scores
        if liste[4][0]==liste[3][0]==liste[2][0]==liste[1][0]==0 or liste[3][0]==liste[2][0]==liste[1][0]==liste[0][0]==0 or liste[4][1]==liste[3][1]==liste[2][1]==liste[1][1]==0 or liste[3][1]==liste[2][1]==liste[1][1]==liste[0][1]==0 or liste[4][2]==liste[3][2]==liste[2][2]==liste[1][2]==0 or liste[3][2]==liste[2][2]==liste[1][2]==liste[0][2]==0 or liste[4][3]==liste[3][3]==liste[2][3]==liste[1][3]==0 or liste[3][3]==liste[2][3]==liste[1][3]==liste[0][3]==0 or liste[4][4]==liste[3][4]==liste[2][4]==liste[1][4]==0 or liste[3][4]==liste[2][4]==liste[1][4]==liste[0][4]==0 or liste[4][5]==liste[3][5]==liste[2][5]==liste[1][5]==0 or liste[3][5]==liste[2][5]==liste[1][5]==liste[0][5]==0 or liste[4][6]==liste[3][6]==liste[2][6]==liste[1][6]==0 or liste[3][6]==liste[2][6]==liste[1][6]==liste[0][6]==0 or liste[0][0]==liste[0][1]==liste[0][2]==liste[0][3]==0 or liste[0][0]==liste[0][1]==liste[0][2]==liste[0][3]==0 or liste[0][1]==liste[0][2]==liste[0][3]==liste[0][4]==0 or liste[0][2]==liste[0][3]==liste[0][4]==liste[0][5]==0 or liste[0][3]==liste[0][4]==liste[0][5]==liste[0][6]==0 or liste[1][0]==liste[1][1]==liste[1][2]==liste[1][3]==0 or liste[1][1]==liste[1][2]==liste[1][3]==liste[1][4]==0 or liste[1][2]==liste[1][3]==liste[1][4]==liste[1][5]==0 or liste[1][3]==liste[1][4]==liste[1][5]==liste[1][6]==0 or liste[2][0]==liste[2][1]==liste[2][2]==liste[2][3]==0 or liste[2][1]==liste[2][2]==liste[2][3]==liste[2][4]==0 or liste[2][2]==liste[2][3]==liste[2][4]==liste[2][5]==0 or liste[2][3]==liste[2][4]==liste[2][5]==liste[2][6]==0 or liste[3][0]==liste[3][1]==liste[3][2]==liste[3][3]==0 or liste[3][1]==liste[3][2]==liste[3][3]==liste[3][4]==0 or liste[3][2]==liste[3][3]==liste[3][4]==liste[3][5]==0 or liste[3][3]==liste[3][4]==liste[3][5]==liste[3][6]==0 or liste[4][0]==liste[4][1]==liste[4][2]==liste[4][3]==0 or liste[4][1]==liste[4][2]==liste[4][3]==liste[4][4]==0 or liste[4][2]==liste[4][3]==liste[4][4]==liste[4][5]==0 or liste[4][3]==liste[4][4]==liste[4][5]==liste[4][6]==0 or liste[4][0]==liste[3][1]==liste[2][2]==liste[1][3]==0 or liste[3][1]==liste[2][2]==liste[1][3]==liste[0][4]==0 or liste[4][1]==liste[3][2]==liste[2][3]==liste[1][4]==0 or liste[3][2]==liste[2][3]==liste[1][4]==liste[0][5]==0 or liste[4][2]==liste[3][3]==liste[2][4]==liste[1][5]==0 or liste[3][3]==liste[2][4]==liste[1][5]==liste[0][6]==0 or liste[4][3]==liste[3][4]==liste[2][5]==liste[1][6]==0 or liste[3][0]==liste[2][1]==liste[1][2]==liste[0][3]==0 or liste[1][0]==liste[2][1]==liste[3][2]==liste[4][3]==0 or liste[0][0]==liste[1][1]==liste[2][2]==liste[3][3]==0 or liste[1][1]==liste[2][2]==liste[3][3]==liste[4][4]==0 or liste[0][1]==liste[1][2]==liste[2][3]==liste[3][4]==0 or liste[1][2]==liste[2][3]==liste[3][4]==liste[4][5]==0 or liste[0][2]==liste[1][3]==liste[2][4]==liste[3][5]==0 or liste[1][3]==liste[2][4]==liste[3][5]==liste[4][6]==0 or liste[0][3]==liste[1][4]==liste[2][5]==liste[3][6]==0:
            messagebox.showinfo("Victoire", "Victoire du jaune")
            Mafenetre.destroy()
        if liste[4][0]==liste[3][0]==liste[2][0]==liste[1][0]==1 or liste[3][0]==liste[2][0]==liste[1][0]==liste[0][0]==1 or liste[4][1]==liste[3][1]==liste[2][1]==liste[1][1]==1 or liste[3][1]==liste[2][1]==liste[1][1]==liste[0][1]==1 or liste[4][2]==liste[3][2]==liste[2][2]==liste[1][2]==1 or liste[3][2]==liste[2][2]==liste[1][2]==liste[0][2]==1 or liste[4][3]==liste[3][3]==liste[2][3]==liste[1][3]==1 or liste[3][3]==liste[2][3]==liste[1][3]==liste[0][3]==1 or liste[4][4]==liste[3][4]==liste[2][4]==liste[1][4]==1 or liste[3][4]==liste[2][4]==liste[1][4]==liste[0][4]==1 or liste[4][5]==liste[3][5]==liste[2][5]==liste[1][5]==1 or liste[3][5]==liste[2][5]==liste[1][5]==liste[0][5]==1 or liste[4][6]==liste[3][6]==liste[2][6]==liste[1][6]==1 or liste[3][6]==liste[2][6]==liste[1][6]==liste[0][6]==1 or liste[0][0]==liste[0][1]==liste[0][2]==liste[0][3]==1 or liste[0][0]==liste[0][1]==liste[0][2]==liste[0][3]==1 or liste[0][1]==liste[0][2]==liste[0][3]==liste[0][4]==1 or liste[0][2]==liste[0][3]==liste[0][4]==liste[0][5]==1 or liste[0][3]==liste[0][4]==liste[0][5]==liste[0][6]==1 or liste[1][0]==liste[1][1]==liste[1][2]==liste[1][3]==1 or liste[1][1]==liste[1][2]==liste[1][3]==liste[1][4]==1 or liste[1][2]==liste[1][3]==liste[1][4]==liste[1][5]==1 or liste[1][3]==liste[1][4]==liste[1][5]==liste[1][6]==1 or liste[2][0]==liste[2][1]==liste[2][2]==liste[2][3]==1 or liste[2][1]==liste[2][2]==liste[2][3]==liste[2][4]==1 or liste[2][2]==liste[2][3]==liste[2][4]==liste[2][5]==1 or liste[2][3]==liste[2][4]==liste[2][5]==liste[2][6]==1 or liste[3][0]==liste[3][1]==liste[3][2]==liste[3][3]==1 or liste[3][1]==liste[3][2]==liste[3][3]==liste[3][4]==1 or liste[3][2]==liste[3][3]==liste[3][4]==liste[3][5]==1 or liste[3][3]==liste[3][4]==liste[3][5]==liste[3][6]==1 or liste[4][0]==liste[4][1]==liste[4][2]==liste[4][3]==1 or liste[4][1]==liste[4][2]==liste[4][3]==liste[4][4]==1 or liste[4][2]==liste[4][3]==liste[4][4]==liste[4][5]==1 or liste[4][3]==liste[4][4]==liste[4][5]==liste[4][6]==1 or liste[4][0]==liste[3][1]==liste[2][2]==liste[1][3]==1 or liste[3][1]==liste[2][2]==liste[1][3]==liste[0][4]==1 or liste[4][1]==liste[3][2]==liste[2][3]==liste[1][4]==1 or liste[3][2]==liste[2][3]==liste[1][4]==liste[0][5]==1 or liste[4][2]==liste[3][3]==liste[2][4]==liste[1][5]==1 or liste[3][3]==liste[2][4]==liste[1][5]==liste[0][6]==1 or liste[4][3]==liste[3][4]==liste[2][5]==liste[1][6]==1 or liste[3][0]==liste[2][1]==liste[1][2]==liste[0][3]==1 or liste[1][0]==liste[2][1]==liste[3][2]==liste[4][3]==1 or liste[0][0]==liste[1][1]==liste[2][2]==liste[3][3]==1 or liste[1][1]==liste[2][2]==liste[3][3]==liste[4][4]==1 or liste[0][1]==liste[1][2]==liste[2][3]==liste[3][4]==1 or liste[1][2]==liste[2][3]==liste[3][4]==liste[4][5]==1 or liste[0][2]==liste[1][3]==liste[2][4]==liste[3][5]==1 or liste[1][3]==liste[2][4]==liste[3][5]==liste[4][6]==1 or liste[0][3]==liste[1][4]==liste[2][5]==liste[3][6]==1:
            messagebox.showinfo("Victoire", "Victoire du rouge")
            Mafenetre.destroy()
        elif not "temp" in liste[0]:
            messagebox.showinfo("Match nul", "Match nul")
            Mafenetre.destroy()

    ##défini la zone de jeu et la grille du jeu
    Mafenetre = Tk()
    Mafenetre.title('Pion')
    Canevas = Canvas(Mafenetre, width = W, height = H, bg ='white')
    Canevas.create_rectangle(0,100,700,600,fill="blue")
    for i in range(5):
        for j in range(7):
            Canevas.create_oval(c-R,tc-R,c+R,tc+R,fill="white")
            c+=100
        Canevas.create_line(0,dc,700,dc)
        c=50
        dc+=100
        tc+=100
    dc=100
    for i in range(7):
        Canevas.create_line(dc,100,dc,600)
        dc+=100

    def reset(event):
        ##pour recommencer avant la fin de la partie
        global h1,h2,h3,h4,h5,h6,h7,liste
        Canevas.delete("oui")
        h1,h2,h3,h4,h5,h6,h7=5,5,5,5,5,5,5
        liste=[["temp"]*7 for _ in range (5)]
    ##bind des touches et lancement du jeu et de la fenêtre
    Canevas.bind("<Button-1>",placer)
    Canevas.bind("<Motion>",attente)
    Canevas.bind("<space>",reset)
    Canevas.focus_set()
    Canevas.pack(padx =5, pady =5)
    Mafenetre.mainloop()



def pong():
        global lf
        if lf==1:
            Mafenetretemp.destroy()
            lf=0    
        global X,Y,DX,DY,RAYON,Largeur,Hauteur,scorej1,pastexte,scorej2,PosX,PosY,PosX2,PosY2,scoreseul,nbremort,couleur,leftside,rightside,upside,downside
        RAYON = 15
        ##score des joueurs ou du joueur selon le jeu
        scorej1=0
        scorej2=0
        scoreseul=0
        ## pour déplacer les barres selon le mode de jeu
        leftside=0
        rightside=0
        upside=0
        downside=0
        ##choisir la couleur du jeu
        msgbox=messagebox.askquestion("Sombre", "Mode sombre ?")
        if msgbox=="yes":
            texte='white'
            pastexte = 'black'
        else:
            texte="black"
            pastexte = "white"
        #choisir le nombre de joueurs et le nombre de morts ou le score max selon le mode (j'ai mis un mode de jeu avec pi joueur histoire de mettre un easter egg quand même)
        nbrejoueurs=int(input("Nombre de joueurs :"))
        nbremort=0
        if nbrejoueurs==2:
            limite=int(input("score max :"))
        if nbrejoueurs==1 or nbrejoueurs==31415926535:
                limitemort=int(input("Limite de morts :"))

        ##définir la fenêtre
        Largeur = 480
        Hauteur = 320
        X = Largeur/2
        Y = Hauteur/2

        Mafenetre = Tk()
        Mafenetre.title('Pion')
        Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg =pastexte)

        ##définir la balle (vitesse / angle)
        vitesse = random.uniform(9,10)
        angle = random.uniform(0,4*math.pi)
        DX = vitesse*math.cos(angle)
        DY = vitesse*math.sin(angle)


        ##définir le jeu selon le mode et les rebonds de la balle selon le mode de jeu également
        def jeu():
            global X,Y,DX,DY,RAYON
            ##mode de jeu
            if nbrejoueurs==1:
                rebondh()
                rebondb()
                rebondd()
                rebondj1()
                Mort()
                clavier1()
                scoresolo()
                Canevas.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
                Mafenetre.after(50,jeu)
                Y = Y+DY
                X = X+DX

            elif nbrejoueurs==2:
                rebondh()
                rebondb()
                rebondj1()
                rebondj2()
                clavier1()
                score1()
                Canevas.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
                Mafenetre.after(50,jeu)
                Y = Y+DY
                X = X+DX

            elif nbrejoueurs==31415926535:
                rebondh()
                rebondb()
                rebondj1()
                rebondj2()
                Mort()
                clavier1()
                scoresolo()
                Canevas.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
                Mafenetre.after(50,jeu)
                Y = Y+DY
                X = X+DX

        ##rebonds
        def rebondh():
            global Y,DY,RAYON,Hauteur
            if Y-RAYON+DY < 0:
                Y = 2*RAYON-Y
                DY = -DY

        def rebondb():
            global Y,DY,RAYON,Hauteur
            if Y+RAYON+DY > Hauteur:
                Y = 2*(Hauteur-RAYON)-Y
                DY = -DY

        def rebondd():
            global X,DX,RAYON,Largeur
            if X+RAYON+DX > Largeur:
                X = 2*(Largeur-RAYON)-X
                DX = -DX

        def rebondj1():
            global X,Y,DX,DY,RAYON,Largeur,scorej1,scoreseul,nbremort,PosX,PosX2,PosY,PosY2
            if X-RAYON+DX < 0 and PosY-50<=Y and PosY+50>=Y:
                X = 2*RAYON-X
                DX = -DX+2
                if nbrejoueurs==1 or nbrejoueurs==31415926535 :
                    scoreseul+=1
                    Canevas.delete("scoreseul")

            ##rebond contre la raquette
            elif X-RAYON+DX < 0 and PosY-50>Y or X-RAYON+DX < 0 and PosY+50<Y:
                scorej1+=1
                nbremort+=1
                Canevas.delete("scorej1")
                Canevas.delete("nombremortsj1")
                X = Largeur/2
                Y = Hauteur/2
                PosX = 7
                PosY = 152
                PosX2 = 477
                PosY2 = 152
                vitesse = random.uniform(9,10)
                angle = random.uniform(0,2*math.pi)
                DX = vitesse*math.cos(angle)
                DY = vitesse*math.sin(angle)

        def rebondj2():
            global X,Y,DX,RAYON,Largeur,scorej2,DY,scoreseul,nbremort,PosX,PosX2,PosY,PosY2
            if X+RAYON+DX > Largeur and PosY2-50<Y-RAYON and PosY2+50>Y+RAYON:
                X = 2*(Largeur-RAYON)-X
                DX = -DX-2
                if nbrejoueurs==31415926535 :
                    scoreseul+=1
                    Canevas.delete("scoreseul")

            ##rebond contre la raquette
            elif X+RAYON+DX > Largeur and PosY2-50>Y-RAYON or X+RAYON+DX > Largeur and PosY2+50<Y+RAYON:
                scorej2+=1
                nbremort+=1
                Canevas.delete("scorej2")
                Canevas.delete("nombremortsj1")
                X = Largeur/2
                Y = Hauteur/2
                PosX = 7
                PosY = 152
                PosX2 = 477
                PosY2 = 152
                vitesse = random.uniform(9,10)
                angle = random.uniform(0,2*math.pi)
                DX = vitesse*math.cos(angle)
                DY = vitesse*math.sin(angle)

        ##arrêt du jeu si score atteint en mode de jeu avec 2 joueurs
        def score1():
            tiret = Canevas.create_text(Largeur/2,15,font=50,text="-",fill=texte)
            Canevas.create_text(Largeur/2+20,15,font=50,text=scorej1,tag="scorej1",fill=texte)
            Canevas.create_text(Largeur/2-20,15,font=50,text=scorej2,tag="scorej2",fill=texte)
            if scorej1==limite:
                messagebox.showinfo("PERDU JOUEUR 1","Perdu joueur 1")
                Mafenetre.destroy()
            elif scorej2==limite:
                messagebox.showinfo("PERDU JOUEUR 2","Perdu joueur 2")
                Mafenetre.destroy()

        ##arrêt du jeu si nbre de mort atteint en mode de jeu seul (entre autre)
        def Mort():
            Canevas.create_text(Largeur-40, Hauteur-20,font=50,text=nbremort,tag="nombremortsj1",fill=texte)
            Canevas.create_text(Largeur-25, Hauteur-20,font=50,text="/",fill=texte)
            Canevas.create_text(Largeur-10, Hauteur-20,font=50,text=limitemort,tag="nombremortschoisi",fill=texte)
            if nbremort==limitemort:
                messagebox.showinfo("PERDU !!!", "Dommage mais t'es nul mdr")
                Mafenetre.destroy()

        ##affiche le score lorsqu'on joue en mode de jeu seul 
        def scoresolo():
            Canevas.create_text(Largeur/2,15,font=50,text=scoreseul,tag="scoreseul",fill=texte)

        def clavier1():
            global PosX,PosY, PosX2, PosY2,leftside,rightside,upside,downside
            ##défini les mouvement des raquettes
            if nbrejoueurs==1:
                if leftside and PosY>30:
                    PosY -= 7.5
                if rightside and PosY<290:
                    PosY += 7.5
                Canevas.coords(Pion,PosX -5, PosY -30, PosX +5, PosY +30)
            elif nbrejoueurs==2 or nbrejoueurs==31415926535:
                if leftside and PosY>30:
                    PosY -= 7.5
                if rightside and PosY<290:
                    PosY += 7.5
                Canevas.coords(Pion,PosX -5, PosY -30, PosX +5, PosY +30)
                if upside and PosY2>30:
                    PosY2-= 7.5
                if downside and PosY2<290:
                    PosY2 += 7.5
                Canevas.coords(Pion2,PosX2 -5, PosY2 -30, PosX2 +5, PosY2 +30)

        def clavierpress(event):
            global leftside,rightside,upside,downside
            ##défini l'appui des touches
            if nbrejoueurs==1 or nbrejoueurs==2:
                if event.keysym == 'z' or event.keysym == 'Z':
                    leftside = 1
                if event.keysym == 's' or event.keysym == 'S':
                    rightside = 1
                if event.keysym == 'p' or event.keysym == 'P':
                    upside = 1
                if event.keysym == 'm' or event.keysym == 'M':
                    downside = 1
            if nbrejoueurs==31415926535 :
                if event.keysym == 'z' or event.keysym == 'Z':
                    leftside = 1
                    upside = 1
                if event.keysym == 's' or event.keysym == 'S':
                    rightside = 1
                    downside = 1

        def clavierrelease(event):
            global leftside,rightside,upside,downside
            ##défini le relachement des touches
            if nbrejoueurs==1 or nbrejoueurs==2:
                if event.keysym == 'z' or event.keysym == 'Z':
                    leftside = 0
                if event.keysym == 's' or event.keysym == 'S':
                    rightside = 0
                if event.keysym == 'p' or event.keysym == 'P':
                    upside = 0
                if event.keysym == 'm' or event.keysym == 'M':
                    downside = 0
            if nbrejoueurs==31415926535 :
                if event.keysym == 'z' or event.keysym == 'Z':
                    leftside = 0
                    upside = 0
                if event.keysym == 's' or event.keysym == 'S':
                    rightside = 0
                    downside = 0

        def reset(event):
            ##arrêter le jeu
            Mafenetre.destroy()
            pong()

        ##position des raquettes
        PosX = 7
        PosY = 152
        PosX2 = 477
        PosY2 = 152

        ##défini et affiche les raquettes
        if nbrejoueurs==1:
            Pion = Canevas.create_rectangle(PosX-5,PosY-30,PosX+5,PosY+30,width=2,outline=texte,fill='red')
        elif nbrejoueurs==2 or nbrejoueurs==31415926535:
            Pion = Canevas.create_rectangle(PosX-5,PosY-30,PosX+5,PosY+30,width=2,outline=texte,fill='red')
            Pion2 = Canevas.create_rectangle(PosX2-5,PosY2-30,PosX2+5,PosY2+30,width=2,outline=texte,fill='red')
        ##bind des fonctions
        Canevas.focus_set()
        Canevas.bind("<space>",reset)
        Canevas.bind('<KeyPress>',clavierpress)
        Canevas.bind('<KeyRelease>',clavierrelease)
        Canevas.pack(padx =5, pady =5)

        ##affiche la balle
        Balle = Canevas.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,width=1,fill='green',tag="balle")

        jeu()
        Mafenetre.mainloop()










##game=str(input("jeux :"))
##if game=="pong":
##    pong()
##elif game=="p4":
##    p4()
##elif game=="morpion":
##    ttt()

Mafenetretemp = Tk()
Label1 = Label(Mafenetretemp, text = 'Jeux').pack(side=TOP)
Bouton1 = Button(Mafenetretemp, text = 'Morpion', command = ttt).pack(side=RIGHT,padx=5,pady=5)
Bouton2 = Button(Mafenetretemp, text = 'Puissance 4', command = p4).pack(side=RIGHT,padx=5,pady=5)
Bouton3 = Button(Mafenetretemp, text = 'Pong', command = pong).pack(side=RIGHT,padx=5,pady=5)
Bouton4 = Button(Mafenetretemp, text = 'Juste Prix', command = jp).pack(side=RIGHT,padx=5,pady=5)
Mafenetretemp.mainloop()