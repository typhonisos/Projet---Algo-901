"""
Classe : SalleDeClasse
Module :
Description : Représente une salle de classe dans un collège.
"""

class SalleDeClasse:
    """ Représente une salle de classe avec un identifiant, une capacité et ses occupations. """

    def __init__(self, aIdSalle: str, aCapacite: int):
        """
        Constructeur de la classe SalleDeClasse.

        :param aIdSalle: Identifiant unique de la salle
        :param aCapacite: Capacité maximale de la salle
        """
        if not aIdSalle:
            raise ValueError("L'identifiant de la salle ne peut pas être vide.")
        if aCapacite <= 0:
            raise ValueError("La capacité doit être positive.")

        self.idSalle = aIdSalle
        self.capacite = aCapacite
        self.occupations = []  # liste des réservations

    def __str__(self):
        """Affichage simple de la salle."""
        return f"Salle {self.idSalle} (capacité : {self.capacite} places)"

    def est_disponible(self, aJour: str, aHeure: float, aDuree: float = 1.0) -> bool:
        """
        Vérifie si la salle est libre sur un créneau donné.

        :param aJour: Jour de la réservation
        :param aHeure: Heure de début
        :param aDuree: Durée du créneau
        :return: True si la salle est libre, False sinon
        """
        for jour, heure, duree, _ in self.occupations:
            # Vérifie un chevauchement de créneaux
            if jour == aJour and not (aHeure + aDuree <= heure or aHeure >= heure + duree):
                return False
        return True

    def reserver(self, aJour: str, aHeure: float, aDuree: float, aClasse: str):
        """
        Réserve la salle pour un créneau donné si elle est disponible.

        :param aJour: Jour de réservation
        :param aHeure: Heure de début
        :param aDuree: Durée
        :param aClasse: Nom de la classe qui réserve la salle
        """
        if self.est_disponible(aJour, aHeure, aDuree):
            self.occupations.append((aJour, aHeure, aDuree, aClasse))
        else:
            raise ValueError(f"Salle {self.idSalle} déjà occupée à {aHeure}h le {aJour}.")

    def afficher_occupation(self):
        """Affiche toutes les réservations de la salle."""
        if not self.occupations:
            print(f"Salle {self.idSalle} : aucune réservation.")
        else:
            print(f"Occupation de la salle {self.idSalle} :")
            for jour, heure, duree, classe in sorted(self.occupations):
                print(f"  {jour} {heure}h–{heure + duree}h : {classe}")


# test
if __name__ == "__main__":
    salle = SalleDeClasse("A101", 30)
    salle.reserver("Lundi", 9, 2, "3A")
    salle.reserver("Mardi", 10, 1, "5B")

    print(salle)
    salle.afficher_occupation()

    print(salle.est_disponible("Lundi", 11, 1))
    print(salle.est_disponible("Lundi", 9.5, 1))
