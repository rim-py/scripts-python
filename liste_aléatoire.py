#  Initialiser une liste aléatoire
import random
def Initialiser_Liste_Aléatoire(n, borne_min, borne_max):
    liste = [] #créer une liste vide
    for i in range(n):
        liste.append(random.randint(borne_min, borne_max)) #ajouter l'entier aléatoire
    return liste
n = int(input("Combien d'entiers voulez-vous entrer ? "))
inf = int(input("inf ? "))
sup = int(input("sup ? "))
print(Initialiser_Liste_Aléatoire(n, inf, sup))
#exemple:
print(Initialiser_Liste_Aléatoire(3, 1, 10)) #affiche [9,1,4]
