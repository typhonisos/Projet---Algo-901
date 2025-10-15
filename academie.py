Classe : Academie
 


from typing import List, Optional, Dict
from College import College


class Academie:
    """Classe représentant une académie composée de plusieurs collèges."""

    def __init__(self, nom: str, region: str):
        """
        Constructeur de la classe Academie.
        :param nom: Nom de l'académie (ex: 'Académie de Grenoble')
        :param region: Région géographique de l'académie
        """
        self.nom = nom
        self.region = region
        self.listeColleges: List[College] = []

    def ajouter_college(self, college: College) -> None:
        """Ajoute un collège à la liste de l’académie."""
        if not isinstance(college, College):
            raise TypeError("L'objet ajouté doit être une instance de la classe College.")
        if college in self.listeColleges:
            raise ValueError(f"Le collège {college.nom} est déjà enregistré.")
        self.listeColleges.append(college)

    def retirer_college(self, college: College) -> None:
        """Retire un collège existant."""
        if not isinstance(college, College):
            raise TypeError("L'objet à retirer doit être une instance de la classe College.")
        try:
            self.listeColleges.remove(college)
        except ValueError:
            raise ValueError(f"Collège '{college.nom}' introuvable dans cette académie.")

    def rechercher_college(self, nom_college: str) -> Optional[College]:
        """Recherche un collège par son nom."""
        for c in self.listeColleges:
            if c.nom.lower() == nom_college.lower():
                return c
        return None

    def _agreger_moyennes(self, get_college_moyennes_func) -> Dict[str, Optional[float]]:
        """
        Méthode privée helper pour agréger les moyennes (par matière ou département)
        de tous les collèges.
        :param get_college_moyennes_func: Fonction à appeler sur chaque collège (ex: college.moyenne_par_matiere)
        """
        resultats = {}
        total_moyennes = {}
        nombre_sources = {}

        for college in self.listeColleges:
            moyennes_source = get_college_moyennes_func(college) # Appelle la fonction passée en paramètre
            
            for nom_element, moyenne in moyennes_source.items():
                if moyenne is not None:
                    total_moyennes.setdefault(nom_element, 0.0)
                    nombre_sources.setdefault(nom_element, 0)
                    
                    total_moyennes[nom_element] += moyenne
                    nombre_sources[nom_element] += 1

        for nom_element in total_moyennes:
            if nombre_sources[nom_element] > 0:
                resultats[nom_element] = round(
                    total_moyennes[nom_element] / nombre_sources[nom_element], 2
                )
            else:
                resultats[nom_element] = None
        return resultats

    def moyenne_globale_academie(self) -> Dict[str, Optional[float]]:
        """
        Retourne la moyenne globale par matière pour l’ensemble des collèges de l’académie.
        Ceci est une "moyenne des moyennes" des collèges, non pondérée.
        """
        # Utilise la méthode helper en lui passant la fonction college.moyenne_par_matiere
        return self._agreger_moyennes(lambda college: college.moyenne_par_matiere())

    def moyenne_globale_departement(self) -> Dict[str, Optional[float]]:
        """
        Retourne la moyenne globale par département (tous collèges confondus).
        Ceci est une "moyenne des moyennes" des départements des collèges, non pondérée.
        """
        # Utilise la méthode helper en lui passant la fonction college.moyenne_par_departement
        return self._agreger_moyennes(lambda college: college.moyenne_par_departement())

    def rechercher_eleve(self, nom_eleve: str) -> Optional[object]:
        """
        Recherche un élève dans tous les collèges de l'académie par son nom.
        Retourne le premier objet Eleve trouvé ou None.
        """
        for college in self.listeColleges:
            for eleve in college.tous_les_eleves():
                if eleve.nom.lower() == nom_eleve.lower():
                    return eleve
        return None

    def rechercher_enseignant(self, nom_enseignant: str) -> Optional[object]:
        """
        Recherche un enseignant dans tous les collèges de l'académie par son nom.
        Retourne le premier objet Enseignant trouvé ou None.
        """
        for college in self.listeColleges:
            for dep in college.listeDepartements:
                for ens in dep.listeEnseignants:
                    if ens.nom.lower() == nom_enseignant.lower():
                        return ens
        return None

    def __str__(self):
        """Affichage synthétique de l’académie et de ses collèges."""
        chaine = f"\nAcadémie : {self.nom} ({self.region})\n"
        chaine += f"Nombre de collèges : {len(self.listeColleges)}\n"
        chaine += "Liste des collèges :\n"
        if not self.listeColleges:
            chaine += "  (Aucun collège enregistré dans cette académie)\n"
        else:
            for c in self.listeColleges:
                chaine += f"  - {c.nom}\n"
        return chaine

    def afficher_occupation_salles_academie(self) -> None:
        """Affiche l'occupation de toutes les salles de tous les collèges de l'académie."""
        print(f"\n--- Occupation des salles dans l'Académie {self.nom} ---")
        if not self.listeColleges:
            print("Aucun collège dans cette académie pour afficher l'occupation des salles.")
            return

        total_salles_affiches = 0
        for college in self.listeColleges:
            print(f"\nCollège : {college.nom}")
            if not college.listeSalleDeClasse:
                print("  (Aucune salle de classe enregistrée pour ce collège)")
                continue
            
            for salle in college.listeSalleDeClasse:
                if salle.occupations:
                    print(f"  Salle {salle.id_salle} (capacité: {salle.capacite} places) :")
                    for j, h, d, c_nom in sorted(salle.occupations):
                        print(f"    {j} {h}h–{h + d}h : {c_nom}")
                    total_salles_affiches += 1
                else:
                    print(f"  Salle {salle.id_salle} : aucune réservation.")
        
        if total_salles_affiches == 0 and any(c.listeSalleDeClasse for c in self.listeColleges):
             print("\nNote : Aucune salle n'a de réservation enregistrée dans l'académie.")

    def afficher_salle_eleve_academie(self, eleve_nom: str, jour_semaine: str, numero_semaine: int, heure_debut: int) -> None:
        """
        Affiche la salle où se trouve un élève spécifique à une heure donnée
        en cherchant dans tous les collèges.
        """
        eleve = self.rechercher_eleve(eleve_nom)
        if not eleve:
            print(f"L'élève '{eleve_nom}' n'a pas été trouvé dans l'académie.")
            return

        if not hasattr(eleve, 'classe') or eleve.classe is None:
            print(f"L'élève '{eleve_nom}' n'est pas assigné à une classe.")
            return

        classe_eleve = eleve.classe
        
        if not hasattr(classe_eleve, 'get_cours_a_heure'):
             print(f"La classe {classe_eleve.nom} de l'élève {eleve_nom} n'a pas de méthode 'get_cours_a_heure'.")
             return
        
        cours_info = classe_eleve.get_cours_a_heure(jour_semaine, numero_semaine, heure_debut)

        if cours_info:
            matiere, salle = cours_info
            print(f"L'élève {eleve_nom} est en {matiere.nom} dans la salle {salle.id_salle} "
                  f"le {jour_semaine} semaine {numero_semaine} à {heure_debut}h.")
        else:
            print(f"Aucun cours trouvé pour l'élève {eleve_nom} le {jour_semaine} semaine {numero_semaine} à {heure_debut}h.")

    def imprimer_fiche_signaletique(self, nom_personne: str, type_personne: str) -> None:
        """
        Imprime la fiche signalétique d'un enseignant ou d'un élève.
        :param nom_personne: Le nom de la personne à rechercher.
        :param type_personne: 'eleve' ou 'enseignant'.
        """
        personne = None
        if type_personne.lower() == 'eleve':
            personne = self.rechercher_eleve(nom_personne)
        elif type_personne.lower() == 'enseignant':
            personne = self.rechercher_enseignant(nom_personne)
        else:
            print("Type de personne invalide. Utilisez 'eleve' ou 'enseignant'.")
            return

        if personne:
            if hasattr(personne, 'fiche_signaletique'):
                print(f"\n--- Fiche signalétique de {personne.prenom} {personne.nom} ({type_personne.capitalize()}) ---")
                fiche = personne.fiche_signaletique()
                for cle, valeur in fiche.items():
                    print(f"{cle} : {valeur}")
            else:
                print(f"L'objet {type_personne} trouvé n'a pas de méthode 'fiche_signaletique'.")
        else:
            print(f"Aucun {type_personne} nommé '{nom_personne}' n'a été trouvé.")
