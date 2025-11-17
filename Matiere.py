class Matiere:
    """
    Classe représentant une matière enseignée dans un collège.
    Conforme au diagramme UML fourni (avec corrections logiques).
    """

    def __init__(self, nom, salle, volume_horaire):
        """
        Constructeur de la classe Matiere.
        :param nom: Nom de la matière (ex: 'Mathématiques')
        :param salle: Salle associée (objet SalleDeClasse)
        :param volume_horaire: Volume horaire hebdomadaire de la matière
        """
        self.aNom = nom
        self.aSalle = salle           # objet SalaDeClasse (avec aId_salle, aCapacite…)
        self.aVolume_horaire = volume_horaire
        self.aNotes = {}              # {eleve : [notes]}
    
    def ajouter_note(self, eleve, note):
        """Ajoute une note pour un élève donné."""
        if eleve not in self.aNotes:
            self.aNotes[eleve] = []
        self.aNotes[eleve].append(note)
    
    def moyenne_matiere(self):
        """Calcule la moyenne de la matière sur tous les élèves notés."""
        total, count = 0, 0
        for notes in self.aNotes.values():
            total += sum(notes)
            count += len(notes)
        return round(total / count, 2) if count else None

    def eleves_non_notes(self, liste_eleves):
        """Retourne la liste des élèves sans note dans cette matière."""
        return [e for e in liste_eleves if e not in self.aNotes]
    
    def __str__(self):
        return f"Matière : {self.nom} | Salle : {self.salle} | Volume : {self.volume_horaire}h"


