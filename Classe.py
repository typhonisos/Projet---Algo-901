### CODE A DECOMMENTER QUAND CLASSE ELEVE CREEE ###

#from Eleve import Eleve

class Classe:
    def __init__(self, nom : str, niveau : str):
        self.nom = nom
        self.niveau = niveau
        self.effectif = 0 # initialisé à 0, sera mis à jour lors de l'ajout ou du retrait d'élèves
        self.listeEleves = [] # liste initialement vide, sera remplie avec des objets Eleve, pas de set
                              # car problèmes de hashabilité avec des objets mutables (dictionnaire bulletin)
    
    def __str__(self):
        # créé la variable eleves qui est une chaîne de caractères listant les noms et prénoms 
        # des élèves pour éviter d'avoir une liste d'objets Eleve illisible
        eleves = ', '.join([f"{e.nom} {e.prenom}" for e in self.listeEleves])
        return f"Classe: {self.nom}, Niveau: {self.niveau}, Effectif: {self.effectif}, Liste des élèves: {eleves}"

    # def ajouter_eleve(self, eleve : Eleve):
    #     if not isinstance(eleve, Eleve):
    #         raise TypeError("L'objet ajouté doit être une instance de la classe Eleve.")
    #     self.listeEleves.append(eleve)
    #     self.effectif += 1

    # def retirer_eleve(self, eleve : Eleve):
    #     if not isinstance(eleve, Eleve):
    #         raise TypeError("L'objet retiré doit être une instance de la classe Eleve.")
    #     if eleve in self.listeEleves:
    #         self.listeEleves.remove(eleve)
    #         self.effectif -= 1
    #     else:
    #         print("L'élève n'est pas dans cette classe.")

if __name__ == "__main__":
    classe1 = Classe("3A", "Troisième")
    # eleve1 = Eleve(nom="Dupont", prenom="Jean", telephone="0123456789", mail="jean.dupont@example.com", annee_entree=2021, bulletin={})
    # eleve2 = Eleve(nom="Martin", prenom="Claire", telephone="9876543210", mail="claire.martin@example.com", annee_entree=2021, bulletin={})

    # classe1.ajouter_eleve(eleve1)
    # classe1.ajouter_eleve(eleve2)

    print(classe1)