from competences import Compétences

class Divinités:
    def __init__(self, pex_naissance, pex_par_regard):
        self.pex_naissance = pex_naissance
        self.magies_pratiqués = 0
        self.sagesses_de_magies = 0
        self.pex_comp = 0
        self.liste_comps = []
        self.pex_autre = 0
        self.enfant_cheri = False

        self.regards = None

    def maj_pex():
        pass

    def update():
        pass

    def ajout_comp(self, internal_name):
        self.liste_comps.append(internal_name)