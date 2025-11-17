class Matiere:
    """
    Classe représentant une matière enseignée dans un collège.
    """

    def __init__(self, nom, salle, nb_places, volume_horaire):
        """
        Constructeur de la classe Matiere.
        :param nom: Nom de la matière (ex: 'Mathématiques')
        :param salle: Salle où se déroule le cours
        :param nb_places: Nombre de places disponibles dans la salle
        :param volume_horaire: Volume horaire hebdomadaire de la matière
        """
        self.nom = nom
        self.salle = salle
        self.nb_places = nb_places
        self.volume_horaire = volume_horaire
        self.enseignants = []   # liste d'objets Enseignant
        self.notes = {}         # dictionnaire : {eleve: [liste de notes]}
    
    def ajouter_enseignant(self, enseignant):
        """Associe un enseignant à cette matière."""
        if enseignant not in self.enseignants:
            self.enseignants.append(enseignant)

    def ajouter_note(self, eleve, note):
        """Ajoute une note pour un élève donné."""
        if eleve not in self.notes:
            self.notes[eleve] = []
        self.notes[eleve].append(note)
    
    def moyenne_matiere(self):
        """Calcule la moyenne de la matière sur tous les élèves notés."""
        total, count = 0, 0
        for notes in self.notes.values():
            total += sum(notes)
            count += len(notes)
        return round(total / count, 2) if count else None

    def eleves_non_notes(self, liste_eleves):
        """Retourne la liste des élèves sans note dans cette matière."""
        return [e for e in liste_eleves if e not in self.notes]
    
    def __str__(self):
        return f"Matière : {self.nom} | Salle : {self.salle} | Volume : {self.volume_horaire}h"


"test"