from Personne import Personne # importation de la classe Personne
class Eleve(Personne):
    def __init__(self, nom, prenom, tel, mail, annee_entree, niveau, classe):
        super().__init__(nom, prenom, tel, mail)  # appel du constructeur parent
        self.annee_entree = annee_entree
        self.niveau = niveau  # 6ème, 5ème, 4ème, 3ème
        self.classe = classe  # référence vers un objet Classe
        self.notes = {}  # dictionnaire {matiere: [liste de notes]}

    def ajouter_note(self, matiere, note):
        if matiere not in self.notes:
            self.notes[matiere] = []
        self.notes[matiere].append(note)

    def moyenne_par_matiere(self, matiere):
        if matiere in self.notes and self.notes[matiere]:
            return sum(self.notes[matiere]) / len(self.notes[matiere])
        return None

    def moyenne_generale(self):
        toutes_notes = [n for notes in self.notes.values() for n in notes]
        if toutes_notes:
            return sum(toutes_notes) / len(toutes_notes)
        return None
