#inverser une chaine de caractere
def inverseChaine(ch):
    inverse='' #creer une chaine vide
    i=1
    while i<=len(ch):
        inverse+=ch[len(ch)-i] #commencer par ernier caractere
        i+=1
    return inverse
print(inverseChaine('bonjour')) #affiche'ruojnob'
