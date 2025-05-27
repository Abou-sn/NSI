# Exo 1, Sujet n°01

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

#Exo 2 sujet n°02

def est_un_ordre (tab):
    n = len(tab)
    vus = []
    for x in tab:
        if x < 1 or x > n or x in vus:
            return False
        vus.append(x)
    return True

def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente 
    un ordre de gÃ¨nes de chromosome
    '''
    # on vérifie que ordre est un ordre de gènes
    assert est_un_ordre(ordre)
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1 
        nb = nb + 1
    i = 0
    while i < n-1: 
        if ordre[i]-ordre[i+1] not in [-1, 1]: # l'écart n'est pas 1 
            nb = nb + 1
        i = i + 1
    if ordre[i] != n: # le dernier n'est pas n 
        nb = nb + 1
    return nb

#Exo 1 sujet n°04

def intToBin(n):
    binaire = ''
    nb = n
    
    while nb>0:
        binaire = str(nb%2)+binaire
        nb = nb//2

    return binaire

# Exo 1 sujet n°09

def multiplication(n1,n2):
    resultat = 0
    if n1 >0 or n2> 0:
        for i in range(n2):
            resultat+=n1
    elif n1<0 and n2<0:
        for i in range (abs(n2)):
            resultat += abs(n1)
    return resultat

# Exo 2 sujet n°09

def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2 
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1 
    return False 

# Exo 1 sujet n°12
def fusion (l1,l2) :

    listeA=[]
    i=0
    j=0
    n1=len(l1)
    n2=len(l2)

    while i<n1 and j<n2 :
        if l1[i]<l2[j]:
            listeA.append(l1[i])
            i+=1
        else :
            listeA.append(l2[j])
            j+=1
   
    return listeA+l1[i:]+l2[j:]

# Exo 2 sujet n°12
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre] 
    elif romains[nombre[0]] >= romains[nombre[1]] : 
        return romains[nombre[0]] + traduire_romain(nombre[1:]) 
    else:
        return traduire_romain(nombre[1:])-romains[nombre[0]] 

# Exo 1 sujet n°19

def recherche_min(tab):
    min = tab[0]
    ind_min = 0
    for i in range(len(tab)):
        if tab[i]<min:
            min = tab[i]
            ind_min = i
    return ind_min

# Exo 2 sujet n°19 

def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab)-1 
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche = gauche+1 
        else :
            tab[gauche] = tab[droite] 
            tab[droite] = 1 
            droite = droite-1 
    return tab

# Exo 1 sujet n°48

def recherche(tab,n):

    ind = 0
    for i in range(len(tab)):
        if n == tab[i]:
            ind = i
        elif n not in tab :
            return None
    return ind

# Exo 2 sujet n°48

def distance_carre(point1, point2):
    """ Calcule et renvoie la distance au carre entre 
    deux points."""
    return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 

def point_le_plus_proche(depart, tab):
    """ Renvoie les coordonnées du premier point du tableau tab se 
    trouvant à la plus courte distance du point depart."""
    min_point = tab[0]
    min_dist = ... 
    for i in range(1, len(tab)):
        if distance_carre(tab[i], depart) < ...: 
            min_point = ... 
            min_dist = ... 
    return min_point


