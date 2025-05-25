# Exo 1, Sujet n°01

adj = [[1,2],[2],[0],[0]]

def voisins_entrants(adj,x):
    # On crée une liste vide pour y mettre nos resulats
    resultat=[]
    for i in range(len(adj)):
        if x in adj[i]:
            resultat.append(i)
    return resultat

# Exo 2, Sujet n°01

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1,len(s)):
        if s[i] == chiffre:
            compte += 1
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + chiffre
    resultat += lecture_chiffre
    return resultat

#Exo 1 sujet n°02

def max_et_indice(tab):
    maximum = 0
    ind_max = 0
    for i in range(len(tab)) :
        if tab[i]>maximum:
            maximum = tab[i]
            ind_max = i

    return maximum,ind_max


#Exo 1 sujet n°04

def intToBin(n):
    binaire = ''
    nb = n
    
    while nb>0:
        binaire = str(nb%2)+binaire
        nb = nb//2

    return binaire

print(intToBin(64))
