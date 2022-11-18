from tkinter import *
from random import *
from tkinter import messagebox

def morpion():
    global lf,c,l,j,q,w,li,co,di,dt,L,B,D,pa,ep,tr
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
        if c%2== 1 and N==2: ## ajout dans les listes pour les croix (2 joueurs)
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

morpion()