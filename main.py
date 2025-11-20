# Import de toutes les autres classes
from Classe import Classe
from College import College
from Departement import Departement
from Eleve import Eleve
from EmploiDuTemps import EmploiDuTemps
from Enseignant import Enseignant
from Matiere import Matiere
from Personne import Personne
from SalleDeClasse import SalleDeClasse
from SiteWeb import SiteWeb

matiere = Matiere("Mathématiques", "Salle 149", 30)
print(matiere)

prof = Enseignant(
        "Marchal", "Nina", "0601020304", "nina@college.fr",
        "2022-09-01", 473.5, matiere, True
    )
print(prof)

site = SiteWeb("https://www.univ-smb.fr/", 2009, prof)

departement = Departement("SCEM")
departement.ajouterEnseignant(prof)
print(departement)

college = College("SMB", site)
print(college)

classe = Classe("3A", "Troisième")
edt = EmploiDuTemps(x=None)
eleve1 = Eleve(aNom="Dupont", aPrenom="Jean", aTel="0123456789", aMail="jean.dupont@example.com", aAnneeEntree=2021, aNiveau = "3ème", aEmploiDuTemps=edt)
eleve2 = Eleve(aNom="Martin", aPrenom="Claire", aTel="9876543210", aMail="claire.martin@example.com", aAnneeEntree=2022, aNiveau = "4ème", aEmploiDuTemps=edt)

classe.ajouter_eleve(eleve1)
classe.ajouter_eleve(eleve2)
print(classe)

salle = SalleDeClasse("A101", 30)
salle.reserver("Lundi", 9, 2, "3A")
print(salle)
salle.afficher_occupation()