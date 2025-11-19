from typing import List, Optional, Dict
from College import College
from Eleve import Eleve
from Enseignant import Enseignant

class Academie:
    """Classe représentant une académie composée de plusieurs collèges."""

    def __init__(self, nom: str, region: str):
        """
        Constructeur de la classe Academie.
        :param nom: Nom de l'académie
        :param region: Région géographique
        """
        self.nom = nom
        self.region = region
        self.listeColleges: List[College] = []

    def ajouter_college(self, college: College) -> None:
        """Ajoute un collège à la liste de l’académie."""
        if not isinstance(college, College):
            raise TypeError("L'objet ajouté doit être une instance de la classe College.")
        
        # Vérification basée sur aNom (attribut de la classe College fournie)
        for c in self.listeColleges:
            if c.aNom == college.aNom:
                raise ValueError(f"Le collège {college.aNom} est déjà enregistré.")
        
        self.listeColleges.append(college)

    def retirer_college(self, college: College) -> None:
        """Retire un collège existant."""
        if not isinstance(college, College):
            raise TypeError("L'objet à retirer doit être une instance de la classe College.")
        try:
            self.listeColleges.remove(college)
        except ValueError:
            raise ValueError(f"Collège '{college.aNom}' introuvable dans cette académie.")

    def rechercher_college(self, nom_college: str) -> Optional[College]:
        """Recherche un collège par son nom."""
        for c in self.listeColleges:
            # Utilisation de aNom (College)
            if c.aNom.lower() == nom_college.lower():
                return c
        return None

    def moyenne_globale_academie(self) -> Dict[str, Optional[float]]:
        """
        Calcule la moyenne globale par matière pour l'ensemble des collèges.
        Parcourt manuellement les structures car College n'a pas de méthode de calcul.
        """
        total_points = {} # {MatiereNom: somme_notes}
        total_notes_count = {} # {MatiereNom: nombre_notes}

        for college in self.listeColleges:
            # Utilisation de aListeClasses (College)
            for classe in college.aListeClasses:
                # Utilisation de listeEleves (Classe)
                for eleve in classe.listeEleves:
                    # Utilisation de aNotes (Eleve) : dictionnaire {MatiereStr: [float]}
                    for matiere_nom, notes in eleve.aNotes.items():
                        if notes:
                            if matiere_nom not in total_points:
                                total_points[matiere_nom] = 0
                                total_notes_count[matiere_nom] = 0
                            
                            total_points[matiere_nom] += sum(notes)
                            total_notes_count[matiere_nom] += len(notes)

        resultats = {}
        for mat, total in total_points.items():
            count = total_notes_count[mat]
            resultats[mat] = round(total / count, 2) if count > 0 else None
        
        return resultats

    def rechercher_eleve(self, nom_eleve: str) -> Optional[Eleve]:
        """
        Recherche un élève dans tous les collèges de l'académie par son nom.
        """
        for college in self.listeColleges:
            # Accès via aListeClasses (College)
            for classe in college.aListeClasses:
                # Accès via listeEleves (Classe)
                for eleve in classe.listeEleves:
                    # Accès via nom (Personne/Eleve)
                    if eleve.nom.lower() == nom_eleve.lower():
                        return eleve
        return None

    def rechercher_enseignant(self, nom_enseignant: str) -> Optional[Enseignant]:
        """
        Recherche un enseignant dans tous les collèges.
        """
        for college in self.listeColleges:
            # Accès via aListeDepartements (College)
            for dep in college.aListeDepartements:
                # On suppose que Departement a une liste 'enseignants' ou 'listeEnseignants'
                # (Code Département non complet fourni, mais logique standard)
                if hasattr(dep, 'listeEnseignants'):
                    liste_profs = dep.listeEnseignants
                elif hasattr(dep, 'enseignants'):
                    liste_profs = dep.enseignants
                else:
                    continue

                for ens in liste_profs:
                    if ens.nom.lower() == nom_enseignant.lower():
                        return ens
        return None

    def afficher_occupation_salles_academie(self) -> None:
        """Affiche l'occupation des salles (si l'information est disponible)."""
        print(f"\n--- Occupation des salles dans l'Académie {self.nom} ---")
        if not self.listeColleges:
            print("Aucun collège enregistré.")
            return

        for college in self.listeColleges:
            print(f"\nCollège : {college.aNom}")
            # Utilisation de aListeSallesDeClasse (College)
            if not college.aListeSallesDeClasse:
                print("  (Aucune salle enregistrée)")
                continue
            
            for salle in college.aListeSallesDeClasse:
                # Utilisation de aId_salle (indiqué dans le __str__ de College)
                # et aCapacite (supposé cohérent avec Matiere qui prend une salle)
                id_s = getattr(salle, 'aId_salle', 'Inconnu')
                cap = getattr(salle, 'aCapacite', '?')
                print(f"  Salle {id_s} (Capacité: {cap})")
                
                # Note: La classe SalleDeClasse n'est pas fournie, 
                # on vérifie si l'attribut occupations existe (comme dans le code original)
                occupations = getattr(salle, 'occupations', [])
                if occupations:
                    for j, h, d, c_nom in sorted(occupations):
                        print(f"    {j} {h}h–{h + d}h : {c_nom}")
                else:
                    print("    Aucune occupation enregistrée.")

    def afficher_salle_eleve_academie(self, eleve_nom: str, jour: str, heure: int) -> None:
        """
        Affiche où se trouve un élève à un moment donné via son emploi du temps.
        """
        eleve = self.rechercher_eleve(eleve_nom)
        if not eleve:
            print(f"L'élève '{eleve_nom}' n'a pas été trouvé dans l'académie.")
            return

        # La classe Eleve fournie n'a pas d'attribut 'classe' direct vers l'objet Classe,
        # mais possède 'aEmploiDuTemps'. Nous devons interroger l'EDT.
        if eleve.aEmploiDuTemps:
            print(f"Recherche dans l'emploi du temps de {eleve.prenom} {eleve.nom}...")
            # Le code de EmploiDuTemps n'est pas complet, on suppose une méthode d'affichage ou d'accès
            # Ici, on affiche simplement l'objet EDT comme preuve de concept cohérente avec la classe Eleve
            print(f"EDT trouvé : {eleve.aEmploiDuTemps}")
            
            # Si l'EDT a une structure type dictionnaire (cas fréquent) :
            if hasattr(eleve.aEmploiDuTemps, 'aEdt'):
                 # Logique fictive adaptée à l'attribut aEdt vu dans le main de Eleve
                 print(f"Détails : {eleve.aEmploiDuTemps.aEdt}")
        else:
            print(f"L'élève {eleve_nom} n'a pas d'emploi du temps assigné.")

    def __str__(self):
        """Affichage synthétique."""
        chaine = f"\nAcadémie : {self.nom} ({self.region})\n"
        chaine += f"Nombre de collèges : {len(self.listeColleges)}\n"
        chaine += "Liste des collèges :\n"
        if not self.listeColleges:
            chaine += "  (Aucun collège)\n"
        else:
            for c in self.listeColleges:
                # Utilisation de aNom
                chaine += f"  - {c.aNom}\n"
        return chaine
