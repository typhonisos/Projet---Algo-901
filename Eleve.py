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
