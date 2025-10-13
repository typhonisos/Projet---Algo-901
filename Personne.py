"""
Classe : Personne
Description : Représente une personne (élève ou enseignant) avec les infos de base
"""

class Personne:
    def __init__(self, nom: str, prenom: str, telephone: str, mail: str):
        """Constructeur de la classe Personne"""
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.mail = mail

    def __str__(self):
        """Méthode pour l’affichage de la personne"""
        chaine  = f"Nom : {self.nom}\n"
        chaine += f"Prénom : {self.prenom}\n"
        chaine += f"Téléphone : {self.telephone}\n"
        chaine += f"Mail : {self.mail}\n"
        return chaine

    def fiche_signaletique(self):
        """Retourne la fiche signalétique d'une personne"""
        return {
            "Nom": self.nom,
            "Prénom": self.prenom,
            "Téléphone": self.telephone,
            "Mail": self.mail
        }


if __name__ == "__main__":
    """Test rapide en exécution directe"""
    p1 = Personne("Dupont", "Jean", "0601020304", "jean.dupont@mail.com")
    print(p1)
    print(p1.fiche_signaletique())
