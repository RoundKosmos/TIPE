class Noeuds :
  def __init__(self, voisins:[Noeuds], nom:str) : 
    """voisins est la liste de tous les noeuds adjacents
    nom le nom du noeud """
    self.voisins = voisins
    self.name = nom
    self.degre = len(voisins)

  def name_neighbour(self):
    """renvoie le nom de tous les voisins du noeud"""
    return [n.name for n in self.voisins]

  def new_neighbour(self, nod):
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

  def app_n(self, noeud:Noeuds) :
    """Rajoute a la liste de noeuds composant le graphe noeud"""
    self.noeuds.append(noeud)
  
  def nods_degs(self) :  """
  renvoie tout les noeuds composant le graphe avec leur degré (Noeuds, int) """
    nods = []
    for n in self.noeuds :
      nods.append( (n, n.degre))
    return nods
        
  #def cor_pearson(self) : #Calcule le degré de corrélation de Pearson du graphe


if __name__ == "__main__" :
  Shibuya = Noeuds([Omote_sando], shibuya)
  Omote_sando = Noeuds([Shibuya, Gaiemmae], omote_sando)
  Gaiemmae = Noeuds([Omote_sando,Aoyama_itchome], gaiemmae)
  Aoyama_itchome = Noeuds([Gaiemmae,Akasaka_mitsuke], aoyama_itchome)
  Akasaka_mitsuke = Noeuds([Aoyama_itchome], akasaka_mitsuke)
  Ginza = Graphe([Shibuya, Omote_sando, Gaiemmae, Aoyama_itchome, Akasaka_mitsuke])
  
  print(Gaiemmae.name_neighbour())
  print(Ginza.nods_degs())
  Tameike_sanno = Noeuds([Akasaka_mitsuke], tameike_sanno)
  Akasaka_mitsuke.new_neighbour(Tameike_sanno)
  
  print(Akasaka_mistune.name_neighbour())
  print(Ginza.nods_degs())
    
