class Noeuds :
  def __init__(self, voisins:[], nom:str, ligne = None) : 
    """voisins est la liste de tous les noeuds adjacents
    nom le nom du noeud """
    self.voisins = voisins
    self.name = nom
    self.degre = len(voisins)
    self.ligne = ligne

  def name_neighbour(self):
    """renvoie le nom de tous les voisins du noeud"""
    return [n.name for n in self.voisins]

  def new_neighbour(self, moi, nod):
    """ nod est un Noeud
    ajoute un nouveau noeud parmi les voisins"""
    if nod.name not in moi.name_neighbour() :
        self.voisins.append(nod)
        self.degre += 1
        
    #reciprocite de la relation voisin
    if moi.name not in nod.name_neighbour() :
        nod.new_neighbour(nod, moi)
    

class Graphe :
  def __init__(self, noeuds:[Noeuds]) : 
    """noeuds est une liste de Noeuds
    nb est le nombre de noeuds"""
    self.nb = len(noeuds)
    self.noeuds = noeuds

  def app_n(self, moi : Noeuds, nod:Noeuds) :
    """Rajoute a la liste de noeuds composant le graphe noeud"""
    #Pas censé marcher comme ça, a regler
    if nod.name not in self.noeuds :
      self.noeuds.append(nod)
      self.nb += 1
      nod.new_neighbour( nod, moi)
  
  def nods_degs(self) :
    """renvoie tout les noeuds composant le graphe avec leur degré (Noeuds, int) """
    nods = []
    for n in self.noeuds :
      nods.append((n.name, n.degre))
    return nods
        
  #def cor_pearson(self) : #Calcule le degré de corrélation de Pearson du graphe


if __name__ == "__main__" :
  Ginza = Graphe([])
  Shibuya = Noeuds([], "Shibuya", Ginza)
  Omote_sando = Noeuds([Shibuya], "Omote_sando", Ginza)
  Gaiemmae = Noeuds([Omote_sando], "Gaiemmae", Ginza)
  Aoyama_itchome = Noeuds([Gaiemmae], "Aoyama_itchome", Ginza)
  Akasaka_mitsuke = Noeuds([Aoyama_itchome], "Akasaka_mitsuke", Ginza)
  ligne = [Shibuya, Omote_sando, Gaiemmae, Aoyama_itchome, Akasaka_mitsuke]
  for n in range(len(ligne) - 1) :
      Ginza.app_n(ligne[(n + 1)] , ligne[n])
  Ginza.app_n(ligne[len(ligne) - 2], ligne[len(ligne) - 1]) 
  
  print(Gaiemmae.name_neighbour())
  print(Ginza.nods_degs())
  Tameike_sanno = Noeuds([Akasaka_mitsuke], "Tameike_sanno", Ginza)
  Ginza.app_n(Akasaka_mitsuke, Tameike_sanno)
  
  print(Aoyama_itchome.name_neighbour())
  print(Akasaka_mitsuke.name_neighbour())
  print(Ginza.nods_degs())

  # ATTENTION AKASAKA MITSUKE NE S'AFFICHE PAS ,A REGLER D'URGENCE
