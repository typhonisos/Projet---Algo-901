"""
Classe : Enseignant
Module :
Description : Représente un enseignant dans un collège.
"""

from Personne import Personne
from Matiere import Matiere

class Enseignant(Personne):
    """ Représente un enseignant avec sa matière, son indice, sa date de prise de fonction. """
    
    def __init__(self, aNom: str, aPrenom: str, aTel: str, aMail: str, aDatePriseFonction: str, aIndice: float, aMatiere: Matiere):
        """Constructeur avec passage des valeurs pour les attributs."""
        super().__init__(aNom, aPrenom, aTel, aMail)
        self.datePriseFonction = aDatePriseFonction
        self.indice = aIndice
        self.matiere = aMatiere

    def __str__(self):
        """Affichage des détails de l'enseignant."""
        return (f"Enseignant : {self.nom} {self.prenom}\n"
                f"Téléphone : {self.tel}\n"
                f"Mail : {self.mail}\n"
                f"Date prise de fonction : {self.datePriseFonction}\n"
                f"Indice : {self.indice}\n"
                f"Matière enseignée : {self.matiere.nom}")

if __name__ == '__main__':
    from Matiere import Matiere
    matiere_test = Matiere("Mathématiques", "Salle 201", 30)
    prof = Enseignant("Marchal", "Nina", "0601020304", "n.marchal@college.fr", "2022-09-01", 473.5, matiere_test)
    print(prof)
