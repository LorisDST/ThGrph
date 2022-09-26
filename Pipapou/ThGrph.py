from random import randint

def build_grph(p,arr):
    grph = {}
    #Demande pour un graphe orienté ou non 
    type = str(input("Entrez 'o' pour un graphe orienté ou 'no' pour un Non-Orienté : "))
    if type=="o":
        #Initialisation du graphe sous forme d'un dictionnaire vide
        print("\nJ'initialise le graphe sous forme de dictionnaire vide ....\n" )
        for i in range(1,p+1):
            grph[str(i)] = []
            pan = 0
            i=0
        print(grph)
        #Création des points avec le bon nombre d'arrêtes sur un graphe orienté
        print("\nJe rempli le dictionnaire ....\n" )
        while pan != arr:
            i = randint(1,p)
            a = randint(1,p)
            grph[str(i)].append(a)
            pan +=1
        for i in range(1,p+1):
            #Vérifier et enlever les doublons grâce à la fonction détaillée plus bas
            grph[str(i)] = clearin(grph[str(i)],p)
        print("\nJe nettoie les doublons possibles .... \n")
        return grph
    elif type == "no" :
        #Initialisation du graphe sous forme d'un dictionnaire vide
        print("\nJ'initialise le graphe sous forme de dictionnaire vide ....\n" )
        for i in range(1,p+1):
            grph[str(i)] = []
            pan = 0
            i=0
            print(grph)
        #Création des points avec le bon nombre d'arrêtes sur un graphe non-orienté
        print("\nJe rempli le dictionnaire ....\n" )
        while pan != arr:
            i = randint(1,p)
            a = randint(1,p)
            grph[str(i)].append(a)
            grph[str(a)].append(i)
            pan +=1
        for i in range(1,p+1):
            #Vérifier et enlever les doublons grâce à la fonction détaillée plus bas
            grph[str(i)] = clearin(grph[str(i)],p)
        print("\nJe nettoie les doublons possibles .... \n")
        return grph
    #Abandon de la création en cas de non choix de l'utilisateur
    elif type != "o" and "no":
        print("Ce n'est pas ce que j'ai demandé !\nAbandon !")
    exit()
#Fonction de nettoyage des doublons dans une liste avec remplacement des arrêtes nettoyée. 
def clearin(L,p):
    R = []
    
    for i in L:
        if i not in R:
            R.append(i)
        else:
            L.remove(i)
            L.append(str(randint(1,p)))
        
    return L
#Fonction de nettoyage des doublons dans une liste, utilisée à la fin 
def clearout(l):
    
    R = []
    for i in l:
        if i not in R:
            R.append(i)
        else:
            pass
    return R
#Fonction de vérification pour des tests => non utile pour le fontionnement
"""def len_all(grph):
    a = 0
    for i in grph:
        a += len(grph[i])
    return a"""

# Fonction de dominating set
def dominating_set(grph):
    #Définition de variables
    l = []
    r = []
    a = 0
    p = len(grph)
    #Lecture du graphe généré
    for i in grph:
        #Vérification pour savoir si les sommets sont marqués 
        if i not in l or r:  
            #Si oui -> récupération du sommets avec le plus d'arrêtes
            if len(grph[str(i)])>a:
                a = len(grph[str(i)])
        #Marquage du sommets avec le plus d'arrêtes et de ces liasons
        for j in grph.keys():
            if len(grph[j]) == a:
                l.append(j)
                for k in grph[j]:
                    r.append(k)
    #Enlever les doublons 
    print("\nJe nettoie les doublons possibles .... \n")
    l = clearout(l)
    #print(len(l))
    return l
            

# Éxécute le code 
grph = build_grph(1000,15000)
#Placement dans un Fichier
s = "\nDOMINATING SET : \n" + str(dominating_set(grph)) + "\n##################################################################################################################################################################################################################\n" +"GRAPHE : \n" + str(grph)
with open("./Pipapou.txt", "w") as fichier:
	fichier.write(s)
fichier.close()

#Anciens tests
"""print(build_grph(100,150))
print(len_all(build_grph(100,150)))
print("\nDOMINATING SET : \n",dominating_set(grph),"##################################################################################################################################################################################################################\n","GRAPHE : \n",grph)
print("##################################################################################################################################################################################################################\n")
print("GRAPHE : \n",grph)"""