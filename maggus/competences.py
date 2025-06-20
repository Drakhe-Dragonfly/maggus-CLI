#from [file] import [things] #variables global dans lequel écrire
from dieux import Divinités


class Compétences:
  def __init__(self, names, difficulty, prérequis, bonus_dict, spé, baga, dons_regards_dict, avantage_faiblesse_dict, lunes, starting_exp, combative_stats, meta_datas):
    self.names = names
    self.diff = difficulty
    #self.prérequis = prérequis
    #self.bonus = bonus_dict
    #self.spé = spé
    self.baga = baga #(BOOL (yin), BOOL (yang))
    self.don_regards = dons_regards_dict
    for dieu in dons_regards_dict["dieux"]:
      dieu.ajout_comp(self.name["fr"])
    #avantages_faiblesses
    self.lunes_mod = lunes #BOOL
    self.pex = starting_exp
    if combative_stats != False:
      pass
    for data in meta_datas:
      pass
    if starting_exp < difficulty:
      self.niveau = -(difficulty+1)
    else:
      self.niveau = None
      self.actualise_level()
    #self.base_app
    if self.base_app <= 0:
      self.modules = 0
    else:
      self.modules = starting_exp / self.base_app

  def actualise_level(self):
    pass #faire la fonction de calcul et d'actualisation du niveau ici
