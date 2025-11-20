from Personne import Personne
from EmploiDuTemps import EmploiDuTemps

class Eleve(Personne):

    def __init__(self, aNom, aPrenom, aTel, aMail, aAnneeEntree, aNiveau, aEmploiDuTemps=None):
        super().__init__(aNom, aPrenom, aTel, aMail)
        self.aAnneeEntree = aAnneeEntree
        self.aNiveau = aNiveau
        self.aNotes = {}  # {Matiere: [notes]}
        self.aEmploiDuTemps = aEmploiDuTemps  # lien vers la classe EmploiDuTemps

    def ajouterNote(self, aMatiere, anote):
        if aMatiere not in self.aNotes:
            self.aNotes[aMatiere] = []
        self.aNotes[aMatiere].append(anote)

    def moyenne_par_matiere(self, aMatiere):
        if aMatiere in self.aNotes and self.aNotes[aMatiere]:
            return sum(self.aNotes[aMatiere]) / len(self.aNotes[aMatiere])
        return None

    def moyenne_generale(self):
        toutes_notes = [n for notes in self.aNotes.values() for n in notes]
        if toutes_notes:
            return sum(toutes_notes) / len(toutes_notes)
        return None
## test de la classe 
if __name__ == "__main__":

    # Création d’un emploi du temps
    edt = EmploiDuTemps(x=None)

    # Création d’un élève avec son emploi du temps
    e = Eleve(
        aNom="Dupont",
        aPrenom="Jean",
        aTel="0601020304",
        aMail="jean.dupont@example.com",
        aAnneeEntree=2022,
        aNiveau="3ème",
        aEmploiDuTemps=edt
    )

    # Ajout de notes
    e.ajouterNote("Maths", 15)
    e.ajouterNote("Maths", 12)
    e.ajouterNote("Français", 14)

    # Affichage
    print("ÉLÈVE :", e.nom, e.prenom)
    print("Année d'entrée :", e.aAnneeEntree)
    print("Niveau :", e.aNiveau)
    print("Notes :", e.aNotes)

    print("\nMoyenne Maths :", e.moyenne_par_matiere("Maths"))
    print("Moyenne générale :", e.moyenne_generale())

    #print("\nEmploi du temps initial (81 cases) :", len(e.aEmploiDuTemps.aEdt), "cases")
