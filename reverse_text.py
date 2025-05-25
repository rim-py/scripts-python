#inverser une chaine de caractère
def inverseChaine(ch):
    inverse='' #créer une chaine vide
    i=1
    while i<=len(ch):
        inverse+=ch[len(ch)-i] #commencer par dernier caractère
        i+=1
    return inverse
print(inverseChaine('bonjour')) #affiche'ruojnob'
