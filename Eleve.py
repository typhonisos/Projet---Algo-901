from Personne import Personne

class Eleve(Personne):
    def __init__(self, nom, prenom, tel, mail, anneeEntree, niveau):
        super().__init__(nom, prenom, tel, mail)
        self.anneeEntree = anneeEntree
        self.niveau = niveau
        self.notes = {}  # {Matiere: [liste de notes]}

    def ajouterNote(self, Matiere, note):
        if Matiere not in self.notes:
            self.notes[Matiere] = []
        self.notes[Matiere].append(note)

    def moyenne_par_matiere(self, Matiere):
        if Matiere in self.notes and self.notes[Matiere]:
            return sum(self.notes[Matiere]) / len(self.notes[Matiere])
        return None

    def moyenne_generale(self):
        toutes_notes = [n for notes in self.notes.values() for n in notes]
        if toutes_notes:
            return sum(toutes_notes) / len(toutes_notes)
        return None

if __name__ == "__main__":
    # Création d’un élève
    e = Eleve(
        nom="Dupont",
        prenom="Jean",
        tel="0601020304",
        mail="jean.dupont@example.com",
        anneeEntree=2022,
        niveau="3ème"
    )

    # Ajout de notes
    e.ajouterNote("Maths", 15)
    e.ajouterNote("Maths", 12)
    e.ajouterNote("Français", 14)
    e.ajouterNote("Histoire", 10)
    e.ajouterNote("Histoire", 16)

    # Affichage des résultats
    print("ÉLÈVE :", e.nom, e.prenom)
    print("Année d'entrée :", e.anneeEntree)
    print("Niveau :", e.niveau)
    print("Notes :", e.notes)

    print("\nMoyenne en Maths :", e.moyenne_par_matiere("Maths"))
    print("Moyenne en Français :", e.moyenne_par_matiere("Français"))
    print("Moyenne en Histoire :", e.moyenne_par_matiere("Histoire"))
    
    print("\nMoyenne générale :", e.moyenne_generale())
