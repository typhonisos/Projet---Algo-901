
class SalleDeClasse :
    """ Représente une salle de classe dans un collège."""
    def __init__(self, id_salle : str, capacite : int):
        if not id_salle:
            raise ValueError("L'identifiant de la salle ne peut pas être vide.")
        if capacite <= 0:
            raise ValueError("La capacité doit être positive.")
        self.id_salle = id_salle
        self.capacite = capacite
        self.occupations = []
        
    def __str__(self):
        return f"Salle {self.id_salle} (capacité: {self.capacite} places)"
    
    def est_disponible(self, jour: str, heure: float, duree: float = 1.0) -> bool:
        """Vérifie si la salle est libre sur le créneau demandé."""
        for j, h, d, _ in self.occupations:
            if j == jour and not (heure + duree <= h or heure >= h + d):
                return False
        return True

    def reserver(self, jour: str, heure: float, duree: float, classe: str):
        """Réserve la salle pour un créneau si elle est disponible."""
        if self.est_disponible(jour, heure, duree):
            self.occupations.append((jour, heure, duree, classe))
        else:
            raise ValueError(f"Salle {self.id_salle} déjà occupée à {heure}h le {jour}.")

    def afficher_occupation(self):
        """Affiche les réservations de la salle."""
        if not self.occupations:
            print(f"Salle {self.id_salle} : aucune réservation.")
        else:
            print(f"Occupation de la salle {self.id_salle} :")
            for j, h, d, c in sorted(self.occupations):
                print(f"  {j} {h}h–{h + d}h : {c}")
                
              
if __name__=="__main__" :
    salle = SalleDeClasse("A101", 30)
    salle.reserver("Lundi", 9, 2, "3A")
    salle.reserver("Mardi", 10, 1, "5B")
    print(salle)
    salle.afficher_occupation()

    print(salle.est_disponible("Lundi", 11, 1)) 
    print(salle.est_disponible("Lundi", 9.5, 1))
    
