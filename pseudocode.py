#On admet la bibliothèque tkinter et toute ses fonctions
#On admet la bibliothèque random et toute ses fonctions
#On admet de la biliothèque de tkinter la fonction messagebox

#Definir la fonction morpion

    #On initialise les variables lf,c,l,j,q,w,li,co,di,dt,L,B,D,pa,ep,tr de type global
    #On assigne a H la valeur 700
    #On assigne a root le retour de l'execution de la fonction Tk
    #On assigne a canvas le retour de l'execution de la fonction Canvas de parametre root, height de valeur H, width de valeur H, et bg de valeur 'skyblue'
    #Retour de la méthode canvas de l'execution de la fonction pack

    #On assigne a tail la valeur de H // 3
    #On assigne a c le retour de l'execution de la fonction randint de parametre 0,1
    #On assigne a v la valeur de tail // 3
    #On initialise a l,j,q,w,li,co,di,dt,ep,tr la valeur 0
    #On assigne au tableau L 3 tableau ayant chacun 3 index de valeur 0
    #On assigne au tableau B 3 tableau ayant chacun 3 index de valeur 0
    #On assigne au tableau D 2 tableau ayant chacun 3 index de valeur 0
    #On assigne a pa la valeur 4

    #Retour de ca canvas.create_line de parametre ca tail+1,0,tail+1,H, fill="black",width= pa-2  
    #Retour de ca canvas.create_line de parametre ca  tail*2 +2,0, tail*2 +2,H, fill="black",width= pa-2 
    #Retour de ca canvas.create_line de parametre ca 0,tail+1,H,tail+1, fill="black",width= pa-2 
    #Retour de ca canvas.create_line de parametre ca 0, tail*2 +2,H, tail*2 +2, fill="black",width= pa-2 

    #Definir pointA prenant pour parametre event

        #On initialise les variables c,j,l,w,q,li,co,fort,ep,xc,yc de type global
        #On assigne a xc et xy les valeurs d'event.x et d'event.y
        #Si c modulo 2 est égal a 0
            #Alors
            #Retour de l'execution de la fonction easteregg  
            #Calcul de la position pour créer les ronds grace aux coordonnées de la souris et de la taille de la case
            #Si la liste L d'index co,li est égal a 0 
                #Alors
                #Retour de l'execution de la fonction liste1
                #Retour de ca canvas.create_oval de parametre  j-v,l-v,j+v,l+v, outline="black",  width=pa,tag= "b" 
                #On incremente c d'un
                #Retour de l'execution de la fonction score
        #Si sinon c modulo 2 est égal a 1 et n est égal a 2
            #Alors
            #Retour de l'execution de la fonction easteregg
            #Calcul de la position pour créer les croix grace aux coordonnées de la souris et de la taille de la case
            #Si la liste L d'index co,li est égal a 0
                #Alors
                #Retour de l'execution de la fonction liste1
                #Retour de ca canvas.create_line de paremetre w-v,q-v, w+v, q+v, fill="black", width=pa,tag= "b" 
                #Retour de ca canvas.create_line de parametre w-v, q+v, w+v, q-v, fill="black", width=pa,tag= "b" 
                #On incremente c d'un
                #Retour de l'execution de la fonction score
        #Si sinon c modulo de 2 est égal a 1 et n est égal a 1 et ft est égal a 1
            #Retour de l'execution de la fonction bot  
        #Si sinon c modulo de 2 est égal a 1 et n est égal a 1 et ft est égal a 2
            #Retour de l'execution de la fonction botfort

    #Definir la fonction easteregg
        #On initialise xc,yc,ep de type global
        #Si xc est égal a H divisé par 2 et yx est égal a H divisé par 2 ou xc est égal a tail et yc est égal a tail
            #Alors
            #On assigne a ep la valeur de ep + 20
            #Retour de l'execution de la fonction pointR
    
    #Definir la fonction bot
        #On initialise c,u,w,p,q,L,m,dt,di de type global
        #Si c modulo de 2 est égal a 1
            #Alors
            #On assigne a u le retour de la fonction randint de parametre 0,H le tout // par tail
            #On assigne a m le retour de la fonction randint de parametre 0,H le tout // par tail
            #Si la liste L d'index m,u est égal a 0
                #Alors
                #On assigne a w, u multiplié par tail + tail // 2
                #On assigne a q, m multiplié par tail + tail // 2
                #On assigne a dt la valeur de w
                #On assigne a di la valeur de q
                #Retour de l'execution de la fonction liste1
                #Retour de ca canvas.create_line de parametre w-v,q-v, w+v, q+v, fill="black", width=pa,tag= "b"  
                #Retour de ca canvas.create_line de parametre w-v, q+v, w+v, q-v, fill="black", width=pa,tag= "b"  
                #On incremente c d'un
                #Retour de l'execution de la fonction score
        #Si sinon la liste L d'index m,u n'est pa ségal a 0
            #Alors retour de l'execution de la fonction bot
        
    #Definir la fonction croix
        #On initialise q,w,di,dt,c de type global
        #On assigne a w, dt + tail // 2
        #On assogne a q, di + tail // 2
        #Retour de ca canvas.create_line de parametre w-v,q-v, w+v, q+v, fill="black", width=pa,tag= "b"
        #Retour de ca canvas.create_line de parametre w-v, q+v, w+v, q-v, fill="black", width=pa,tag= "b"  
        #On incremente c d'un

    #Definir la fonction botFort
        #On initialise c,L,cdi,dt,B,D,q,w
        #Si c modulo 2 est égal a 1
            #On assigne a dt,di,po la valeur 0
            #Si 1 n'est pas dans la liste L d'index 0 et 1 n'est pas dans la liste L d'index 2
                #Alors
                #On assigne a dt le retour de l'execution de la fonction choice de paramete 0,H-tail
                #On assigne a di le retour de l'execution de la fonction choice de paramete 0,H-tail
                #Si la liste L d'index di//tail,dt//tail est égal a 0
                    #Alors
                    #Retour de l'execution de la fonction liste1
                    #On assigne a w dt//tail multiplié par tail le tout additionné a tail//2
                    #On assigne a q di//tail multiplié par tail le tout additionné a tail//2
                    #Retour de ca canvas.create_line de parametre w-v,q-v, w+v, q+v, fill="black", width=pa,tag= "b"
                    #Retour de ca canvas.create_line de parametre w-v, q+v, w+v, q-v, fill="black", width=pa,tag= "b"  
                    #On incremente c d'un
                    #Retour de l'execution de la fonction score
            #Pour s de fonction range de parametre 3
                #Pour y de fonction range de parametre 3
                    #Si la liste L d'index s,y est égal 1
                        #Alors on incremente po d'un
            #Si po est égal a 1 et la liste L d'index 1,1 est égal a 0
                #Alors
                #On assigne a dt la valeur tail
                #On assigne a di la valeur tail
                #Retour de la l'execution des fonctions liste1, croix, et score
            #On assigne a dt la valeur 0
            #On assigne a di la valeur 0
            ## ETUDE DES POSSIBILITES ## 
            #Si la liste L d'index 0,1 est égal a 1 et la liste L d'index 0,2 est égal a 2 et c modulo 2 est égal a 1 et la liste L d'index 0,0 est égal a 0 ou la liste L d'index 1,0 est égal a 2 et la liste L d'index 2,0 est égal a 2 et c modulo 2 est égal 1 et la liste L d'index 0,0 est égal a 0 ou la liste L d'index 1,1 est égal a 2 et la liste L d'index 2,2 est égal a 2 et c modulo 2 est égal 1 et la liste L d'index 0,0 est égal a 0
                #Alors
                #Retour de l'execution des fonctions liste1, croix, score
            #On assigne a dt la valeur dt + tail
            ### Il nous faut faire ca 8 fois mais vous avez compris qu'on avait compris t'as capté le sang ###
            
            #Tant que c modulo 2 est égal 1
                #Retour de l'execution de la fonction bot
            
    #Definir la fonction liste1
        #On initialise li,c,co,L,B,D,u,p,m,dt,di de type de global
        #On initialise p a 0
        #On initialise a a 2
        #Si c modulo 2 est égal a 0
            #Alors
            #On assigne a la liste L d'index co,li de valeur 1
            #On assigne a la liste B d'index li,co de valeur 1
            #Pour f de fonction range de prametre 3
                #On assigne la liste D d'index 0,f la valeur de la liste L d'index p,p
                #On assigne la liste D d'index 1,f la valeur de la liste L d'index a,p
                #On decremente a d'un
                #On incremente p d'un
            #On assigne la valeur 0 a li,co
        #Si c modulo 2 est égal a 1 et N est égal 2
            #Alors
            #On assigne a la liste L d'index co,li de valeur 2
            #On assigne a la liste B d'index li,co de valeur 2
            #Pour f de fonction range de prametre 3
                #On assigne la liste D d'index 0,f la valeur de la liste L d'index p,p
                #On assigne la liste D d'index 1,f la valeur de la liste L d'index a,p
                #On decremente a d'un
                #On incremente p d'un
            #On assigne la valeur 0 a li,co
        #Si sinon c modulo 2 est égal 1 et N est égal a 1 et ft est égal a 1
            #Alors
            #On assigne a la liste L d'index m,u de valeur 2
            #On assigne a la liste B d'index u,m de valeur 2
            #Pour f de fonction range de prametre 3
                #On assigne la liste D d'index 0,f la valeur de la liste L d'index p,p
                #On assigne la liste D d'index 1,f la valeur de la liste L d'index a,p
                #On decremente a d'un
                #On incremente p d'un
            #On assigne la valeur 0 a li,co
        #Si sinon c modulo 2 est égal 1 et N est égal 1 et ft est égal 1
            #Alors
            #On assigne pm la valeur di // tail
            #On assigne pl la valeur dt // tail
            #On assigne a la liste L d'index pm,pl la valeur 2
            #On assigne a la liste B d'index pl,pm la valeur 2
            #Pour f de fonction range de parametre 3
                #On assigne a la liste D d'index 0,f la valeur de la liste L d'index p,p
                #On assigne a la liste D d'index 1,f la valeur de la liste L d'index a,p
                #On decremente a d'un
                #On incremenet p d'un
            #On assigne a pm et pl la valeur 0
    
    #Definir la fonction score
        #On initialise L,B,D,ep,tr de type global
        #On initialise thj a 0
        #Pour i de fonction range de parametre 3
            #Si la liste L d'index i,0 est égal a 1 et la liste L d'index i,1 est égal a 1 et la liste L d'index i,2 est égal a 2
                #Alors
                #Retour de la fonction messagebox et showinfo de parametre "Winner","le joueur 1 a gagné (rond), pour recommencer appuyer sur d"
                #On incremente thj et ep d'un
                #Retour de l'execution de la fonction de pointR
            #Si sinon la liste L d'index i,0 est égal et la liste L d'index i,1 est égal a 2 et la liste L d'index i,2 est égal 2
                #Alors
                #Retour de la fonction messagebox et showinfo de parametre "Winner","le joueur 2 a gagné (croix),pour recommencer appuyer sur d"
                #On incremente thj et tr d'un
                #Retour de l'execution de la fonction de pointC
        #Pour g de fonction range de parametre 3
            #Si la liste B d'index g,0 est égal a 1 et la liste B d'index g,1 est égal 1 et la liste B d'index g,2 est égal a 1
                #Alors
                #Retour de la fonction messagebox et showinfo de parametre "Winner","le joueur 1 a gagné (rond), pour recommencer appuyer sur d"
                #On incremente thj et ep d'un
                #Retour de l'execution de la fonction de pointR
            #Si sinon la liste B d'index g,0 est égal 2 et la liste B d'index g,1 est égal a 2 et la liste B d'index g,2 est égale a 2
                #Alors
                #Retour de la fonction messagebox et showinfo de parametre "Winner","le joueur 2 a gagné (croix),pour recommencer appuyer sur d"
                #On incremente thj et tr d'un
                #Retour de l'execution de la fonction de pointC
        #Pour o de fonction range de parametre 3
            #Si la liste D d'index o,0 est égal 1 et la liste D d'index o,1 est égal 1 et la liste D d'index o,2 est égal 1
                #Alors
                #Retour de la fonction messagebox et showinfo de parametre "Winner","le joueur 1 a gagné (rond), pour recommencer appuyer sur d"
                #On incremente thj et ep d'un
                #Retour de l'execution de la fonction de pointR
            #Si la liste D d'index o,0 est égal 2 et la liste D d'index o,1 est égal a 2 et la liste D d'index o,2 est égal a 2
                 #Alors
                #Retour de la fonction messagebox et showinfo de parametre "Winner","le joueur 2 a gagné (croix),pour recommencer appuyer sur d"
                #On incremente thj et tr d'un
                #Retour de l'execution de la fonction de pointC
        #Si 0 n'est pas dans liste L d'index 0 et 0 n'est pas dans la liste L d'index 1 et 0 n'est pas dans la liste L d'index 2 et thj est égal a 0
            #Alors retour de la fonction messagebox et showinfo de parametre "match nul ","match nul (aucun joueur a gagner), pour recommencer appuyer sur d"
    
    #Definir la fonction recommencer prenant comme parametre event
        #On initialise c,li,co,L,B,D de type global
        #Retour de la fonction canvas et delete de parametre "b"
        #On assigne au tableau L 3 tableau ayant chacun 3 index de valeur 0
        #On assigne au tableau B 3 tableau ayant chacun 3 index de valeur 0
        #On assigne au tableau D 2 tableau ayant chacun 3 index de valeur 0
        #On assigne a c le retour de la fonction randint de parametre 0,1
    
    #Definir la fonction changer
        #On initialise N,ft,tr,ep de type global
        #On assigne a demande le retour de la fonction messagebox et askquetion de parametre "Choix du nombre de joueur", "2 joueurs (oui) ou 1 joueur (non), appuyez sur d pour recommencer ?"
        #Si demande est égal a "yes"
            #Alors
            #On assigne a N la valeur 2
            #On initialise ep et tr a 0
            #Retour de l'execution des fonctions pointR et pointC
        #Si demande est égal a "no"
            #Alors
            #On assigne a N la valeur 0
            #On assigne a niveau le retour de l'execution de la fonction messagebox et askquetion de parametre "niveau du bot","difficile (oui) ou facile (non) ? appuyez sur d pour recommencer, clic gauche pour faire jouer le bot "
            #Si niveau est égal a "yes"
                #Alors 
                #On assigne a ft la valeur 2
                #On initialise ep et tr a 0
                #Retour de l'execution des fonctions pointR et pointC
            #Si niveau est égal a "no"
                #Alors 
                #On assigne a ft la valeur 1
                #On initialise ep et tr a 0
                #Retour de l'execution des fonctions pointR et pointC
    
    #Definir la fonction pointR
        #On initialise ep de type global
        #Retour de l'execution de la fonction canvs et delete de parametre "y"
        #Retour de l'execution de la fonction canvs et create_text de parametre H//6,H-10, text=" ronds:",tag="y"
        #Retour de l'execution de la fonction canvs et create_text de parametre (H//6)+25,H-10,text= str(ep), tag="y"
        #Si ep est égal a 55
            #Retour de l'execution de la fonction messagebox et showinfo de parametre "ERREUR","ERREUR, vous êtes trop bon "
            #Retour de l'execution de la fonction canvas et destroy
        
    #Definir pointC
        #On initialise tr de type global
        #Retour de l'execution de la fonction canvas et delete de parametre "p"
        #Retour de l'execution de la fonction canvas et create_text de parametre (H//6)*5,H-10, text="croix:",tag="p"
        #Retour de l'execution de la fonction canvas et create_text de parametre ((H//6)*5)+22,H-10,text= str(tr), tag="p"
    
    #Retour de l'execution de la fonction changer
    #Retour de l'execution de la fonction canvas et bind de parametre "d", recommencer
    #Retour de l'execution de la fonction canvas et bind de parametre '<Button-1>', pointA
    #Retour de l'execution de la fonction canvas et focus_set
    #On assigne a bouton la fonction Button de parametre root,text= "mode de joueur", command=changer
    #Retour de l'execution de la fonction bouton et pack de parametre padx=H/2, pady=5
    #Retour de l'exection de la fonction root et mainloop

#Retour de l'execution de la fonction morpion