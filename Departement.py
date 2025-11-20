from typing import List,Optional
from Enseignant import Enseignant
from Matiere import Matiere

class Departement:
    def __init__(self,aNom : str, aResponsable : Optional[Enseignant] =None, aListeEnseignants : List[Enseignant]=[],aListeMatieres : List[Matiere] =[] ):
        """
        Constructeur de la classe Departement avec comme attributs :
        -nom (str) : Le nom du département
        -responsable (Enseignant) : L'enseignant responsable du  département
        -listeEnseignants (List[Enseignant]) : Liste des enseignants du département
        -listeMatiere (List[Matiere]) : Liste des matières du département 
        """
        self.nom=aNom
        self.responsable =aResponsable
        self.listeEnseignants=aListeEnseignants
        self.listeMatieres=aListeMatieres

    def __str__(self):
        return f"Département : {self.nom} avec comme responsable: {self.responsable}"
    
    def ajouterEnseignant(self,enseignant : Enseignant):
        """
        Ajoute un enseignant à la liste des enseignants du départment
        """
        self.listeEnseignants.append(enseignant)
    
    def ajouterMatiere(self,matiere : Matiere):
        """
        Ajoute une matière à la liste des matière du département
        """
        self.listeMatieres.append(matiere)
    
    def changerResponsable(self,nouveau_responsable : Enseignant):
        """
        Change le responsable du département et l'ajoute à la liste des enseignants si il n'en faisait pas partie
        """
        self.responsable = nouveau_responsable
        if not nouveau_responsable in self.listeEnseignants:
            self.listeEnseignants.append(nouveau_responsable)
    
    def enleverEnseignant(self,enseignant_partant: Enseignant):
        """
        Enlève un enseignant de la liste des enseignants en vérifiant auparavant si il faisait bien partie du département
        """
        if not enseignant_partant in self.listeEnseignants:
            return "Cet enseignant ne fait pas partie du département"
        self.listeEnseignants.remove(enseignant_partant)

    def enleverMatiere(self,matiere_partante: Matiere):
        """
        Enlève une matière de la liste des matières en vérifiant auparavant si elle faisait bien partie du département
        """
        if not matiere_partante in self.listeMatieres:
            return "Cette matière ne fait pas partie du département"
        self.listeMatieres.remove(matiere_partante)




        
