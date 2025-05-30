class Caracteristique:
  def __init__(self, name, abbreviation, score=10):
    self.name = name
    self.abbreviation = abbreviation
    self.score = score
    self.bonus = (score//2)-5
    self.temp_mods = None
    self.car_comps = []

def update_score(self, mod=0)
  self.score += mod
  self.bonus = (self.score//2)-5

class Competences:
  def __init__(self, name, carac):
    self.name = name
    carac.car_comps.append(self)
    self.score = carac.bonus + 0 #maitrise
