from Eleve import Eleve
from EmploiDuTemps import EmploiDuTemps

class Classe:
    def __init__(self, aNom : str, aNiveau : str):
        self.nom = aNom
        self.niveau = aNiveau
        self.effectif = 0 # initialisé à 0, sera mis à jour lors de l'ajout ou du retrait d'élèves
        self.listeEleves = [] # liste initialement vide, sera remplie avec des objets Eleve, pas de set
                              # car problèmes de hashabilité avec des objets mutables (dictionnaire bulletin)
    
    def __str__(self):
        # créé la variable eleves qui est une chaîne de caractères listant les noms et prénoms 
        # des élèves pour éviter d'avoir une liste d'objets Eleve illisible
        eleves = ', '.join([f"{e.nom} {e.prenom}" for e in self.listeEleves])
        return f"Classe: {self.nom}, Niveau: {self.niveau}, Effectif: {self.effectif}, Liste des élèves: {eleves}"

    def ajouter_eleve(self, eleve : Eleve):
        if not isinstance(eleve, Eleve):
            raise TypeError("L'objet ajouté doit être une instance de la classe Eleve.")
        self.listeEleves.append(eleve)
        self.effectif += 1

    def retirer_eleve(self, eleve : Eleve):
        if not isinstance(eleve, Eleve):
            raise TypeError("L'objet retiré doit être une instance de la classe Eleve.")
        if eleve in self.listeEleves:
            self.listeEleves.remove(eleve)
            self.effectif -= 1
        else:
            print("L'élève n'est pas dans cette classe.")

if __name__ == "__main__":
    classe1 = Classe("3A", "Troisième")
    edt = EmploiDuTemps(x=None)
    eleve1 = Eleve(aNom="Dupont", aPrenom="Jean", aTel="0123456789", aMail="jean.dupont@example.com", aAnneeEntree=2021, aNiveau = "3ème", aEmploiDuTemps=edt)
    eleve2 = Eleve(aNom="Martin", aPrenom="Claire", aTel="9876543210", aMail="claire.martin@example.com", aAnneeEntree=2022, aNiveau = "4ème", aEmploiDuTemps=edt)

    classe1.ajouter_eleve(eleve1)
    classe1.ajouter_eleve(eleve2)

    print(classe1)
