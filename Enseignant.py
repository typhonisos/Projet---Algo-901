"""
Classe : Enseignant
Module :
Description : Représente un enseignant dans un collége.
"""

from Personne import Personne
from Eleve import Eleve
from Matiere import Matiere
from EmploiDuTemps import EmploiDuTemps
# from Departement import Departement # (Faire attention à l'import circulaire par la suite!!)


class Enseignant(Personne):
    """ Représente un enseignant avec sa matiére, son indice, sa date de prise de fonction et son statut responsable """
    
    def __init__(self, aNom: str, aPrenom: str, aTel: str, aMail: str, aDatePriseFonction: str, aIndice: float, aMatiere: Matiere, aResponsable: bool = False):
        """
        Constructeur de la classe Enseignant.
        Hérite de la classe Personne

        :param aNom: Nom de l'enseignant
        :param aPrenom: Prénom de l'enseignant
        :param aTel: Numéro de téléphone
        :param aMail: Adresse mail
        :param aDatePriseFonction: Date de prise de fonction (str)
        :param aIndice: Indice de rémunération (float)
        :param aMatiere: Matière enseignée
        :param aResponsable: Booléen indiquant si l'enseignant est responsable
        """
        # Appel au constructeur de la classe mère Personne
        super().__init__(aNom, aPrenom, aTel, aMail)
        self.datePriseFonction = aDatePriseFonction
        self.indice = aIndice
        self.matiere = aMatiere
        self.responsable = aResponsable  #  ajout du booléen

        # ralation UML département 1..* Enseignants (un enseignant appartient à un département)
        # (initialisé à None, défini plus tard via definirDepartement)

        self.departement = None
    
    def definirDepartement(self, departement):
        """
        Associe l'enseignant à un département.
        La classe Département se charge d'appeler cette méthode.
        """
        self.departement = departement

    def __str__(self):
        """Affichage des détails de l'enseignant."""
        return (f"Enseignant : {self.nom} {self.prenom}\n"
                f"Téléphone : {self.telephone}\n"
                f"Mail : {self.mail}\n"
                f"Date prise de fonction : {self.datePriseFonction}\n"
                f"Indice : {self.indice}\n"
                f"Matiére enseignée : {self.matiere.aNom}"
                f"Responsable : {self.responsable}\n"
                f"Département : {self.departement.nom if self.departement else 'Aucun'}")


# main 

if __name__ == '__main__':
    from Departement import Departement   # import ici de la classe Département afin d'éviter l'import circulaire 
    edt = EmploiDuTemps(x=None)
    eleve1 = Eleve(aNom="Dupont", aPrenom="Jean", aTel="0123456789", aMail="jean.dupont@example.com", aAnneeEntree=2021, aNiveau = "3ème", aEmploiDuTemps=edt)    # Création matière
    matiere_test = Matiere("Mathématiques", "Salle 149", 30)

    # Création enseignant
    prof = Enseignant(
        "Marchal", "Nina", "0601020304", "nina@college.fr",
        "2022-09-01", 473.5, matiere_test, True
    )

    # Création département
    dep = Departement("Sciences", aResponsable=prof)

    # Association enseignant ↔ département
    prof.definirDepartement(dep)
    dep.ajouterEnseignant(prof)

    # Affichage
    print(prof)

