#========= EXERCICE 2

#====== Functions

def read_file(path):
    # Fonction pour lire le contenu de path
    f = open(path,'r')
    output = list()
    # Remplir output avec les données de path
    for ligne in f :
        mot = ligne[0:len(ligne)-1]
        if len(mot) <= 8:
          output.append(mot)
    f.close()
    return output

#=== creation d'une fonction qui vérrifié si un caractère est dans une liste

def est_dans(c,l):
  n = len(l)
  for i in range(0,n):
    if c == l[i] :
      return True
  return False

#==== creation de la fonction valide qui étant donné un tirage et un mot dit si il est possible d'écrire ce mot avec le tirage

def word_possible(mot,tirage):
  n = len(mot)
  copie = list(tirage) # on creer une copie de la liste puisque la méthode .remove() mute notre tirage
  for i in range(0,n) :
    if est_dans(mot[i],copie):
      copie.remove(mot[i])
    else :
      return False
  return True

#======= Script / Main

path = 'frenchssaccent.dic'
mots = list()
# charger le lexique
mots = read_file(path)

tirage = ['o','t','u','i','r','e','b','p']

# générer les mots possibles

mots_possibles = list()

for mot in mots :
  if word_possible(mot,tirage):
    mots_possibles.append(mot)

#garder les plus grand mots

mots_long_max = list()

m = 1 # longueure maximale initiale arbitraire

for mot in mots_possibles :
  if len(mot)>m :
    m = len(mot)

max = m # taille maximale des mots qu'il est possible d'écrire

# on sélectionne les mots de longueur maximale 

mots_long_max = [ mot for mot in mots_possibles if len(mot) == max ]

print(mots_long_max,mots_possibles)

#====== EXERCICE 3

# pour implémenter le nombre de points associé à chaque lettres on peut proposer un dictionnaire dont les clefs sont les lettres et les valeurs leurs nombre de points

dico_points = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':10,'l':1,'m':2,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':10,'x':10,'y':10,'z':10}

# définition de la fonction score, qui renvoie le nombre de points associés à un mot donné

def score(mot):
  s = 0
  for lettre in mot :
    s += dico_points[lettre]
  return s

# création d'une fonction qui prends en argument une liste de mots et qui renvoie le mot de plus gros score ainsi que son score

def max_score(liste_mots):
  m = 0
  mot_max = ""
  for mot in liste_mots:
    if score(mot) > m :
      m = score(mot)
      mot_max = mot
  return mot_max,m

print(max_score(["xerjof","columbus","banane"]))

#===== EXERCICE 4

#pour traiter le jocker on peut rajouter dabord la clé '?' associée au score 0 comme suit :

dico_points['?'] = 0 

# si notre tirage contient un joker ( et un seul ), on peut modifier notre algorithme "word_possible" en ajoutant un compteur
# de tolérance initialisé à 0 que l'on incrémentera si une lettre du mot choisis ne fait pas partie du tirage, et on continue la 
# routine, toutefois si ce compteur venait à être encore incrémenté, et vaudrait donc 2, on retourne False.
# on propose alors l'algorithme suivant :

def word_possible_joker(mot,tirage):
  n = len(mot)
  tolerance = 0 # compteur des lettres ne faisant pas partis du tirage
  copie = list(tirage) # on creer une copie de la liste puisque la méthode .remove() mute notre tirage
  for i in range(0,n) :
    if est_dans(mot[i],copie):
      copie.remove(mot[i])
    else if tolerance == 0 : # si la lettre n'est pas dans le tirage mais que l'on dispose encore du joker 
      tolerance += 1 # la tolerance passe à 1 et il n'y a plus de joker
    else :
        return False
  return True

#==== FIN