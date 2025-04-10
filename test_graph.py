class Noeuds :
  def __init__(self, voisins:[Noeuds], nom:str) : 
    """voisins est la liste de tous les noeuds adjacents
    nom le nom du noeud """
    self.voisins = voisins
    self.name = nom
    self.degre = len(voisins)

  def name_neighbor(self):
    """renvoie le nom de tous les voisins du noeud"""
    return [n.name for n in self.voisins]

  def new_nods(self, nod):
    """ nod est un Noeud
    ajoute un nouveau noeud parmi les voisins"""
    self.voisins.append(nod)
    self.degre += 1

class Graphe :
  def __init__(self, noeuds:[Noeuds]) : 
    """noeuds est une liste de Noeuds
    nb est le nombre de noeuds"""
    self.nb = len(noeuds)
    self.noeuds = noeuds

  
  def nods_degs(self) :  """
  renvoie tout les noeuds composant le graphe avec leur degré (Noeuds, int) """
    nods = []
    for n in self.noeuds :
      nods.append( (n, n.degre))
    return nods
        
  def cor_pearson(self) : #Calcule le degré de corrélation de Pearson du graphe
    
