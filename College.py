# -*- coding: utf-8 -*-
"""
Module : college.py
Contient UNIQUEMENT la classe College
"""

from typing import List, Dict, Optional


class College:
    def __init__(self, nom: str, siteInternet):
        """
        Initialise un collège.
        :param nom: nom du collège
        :param siteInternet: objet Site
        """
        self.nom = nom
        self.siteInternet = siteInternet
        self.listeDepartements: List = []
        self.listeSalleDeClasse: List = []
        self.listeClasses: List = []

    # ---------------------- Gestion des départements ---------------------- #
    def ajouter_departement(self, dep) -> None:
        if dep in self.listeDepartements:
            raise ValueError(f"Département déjà présent : {dep}")
        self.listeDepartements.append(dep)

    def retirer_departement(self, dep) -> None:
        try:
            self.listeDepartements.remove(dep)
        except ValueError:
            raise ValueError("Département introuvable")

    # ---------------------- Gestion des salles ----------------------------- #
    def ajouter_salle(self, salle) -> None:
        if salle in self.listeSalleDeClasse:
            raise ValueError(f"Salle déjà présente : {salle}")
        self.listeSalleDeClasse.append(salle)

    def retirer_salle(self, salle) -> None:
        try:
            self.listeSalleDeClasse.remove(salle)
        except ValueError:
            raise ValueError("Salle introuvable")

    # ---------------------- Gestion des classes ---------------------------- #
    def ajouter_classe(self, c) -> None:
        if c in self.listeClasses:
            raise ValueError(f"Classe déjà présente : {c}")
        self.listeClasses.append(c)

    def retirer_classe(self, c) -> None:
        try:
            self.listeClasses.remove(c)
        except ValueError:
            raise ValueError("Classe introuvable")

    # ---------------------- Méthodes de calcul ----------------------------- #
    def toutes_les_matieres(self) -> List:
        """
        Retourne la liste des matières présentes dans le collège.
        (On suppose que chaque département sait donner ses matières).
        """
        matieres = []
        for d in self.listeDepartements:
            matieres.extend(d.matieres_du_departement())
        return matieres

    def tous_les_eleves(self) -> List:
        """
        Retourne la liste de tous les élèves du collège.
        (On suppose que chaque classe contient une liste d'élèves).
        """
        return [e for c in self.listeClasses for e in c.listeEleves]

    def moyenne_par_matiere(self) -> Dict[str, Optional[float]]:
        """
        Calcule la moyenne par matière sur tous les élèves du collège.
        (On suppose que chaque élève possède un bulletin {Matiere: [notes]}).
        """
        result = {}
        matieres = self.toutes_les_matieres()
        eleves = self.tous_les_eleves()
        for m in matieres:
            notes = []
            for e in eleves:
                notes.extend(e.bulletin.get(m, []))
            result[m.nom] = sum(notes) / len(notes) if notes else None
        return result

    def moyenne_par_departement(self) -> Dict[str, Optional[float]]:
        """
        Calcule la moyenne par département (agrégation des matières de chaque département).
        """
        res = {}
        eleves = self.tous_les_eleves()
        for d in self.listeDepartements:
            notes = []
            for m in d.matieres_du_departement():
                for e in eleves:
                    notes.extend(e.bulletin.get(m, []))
            res[d.nom] = sum(notes) / len(notes) if notes else None
        return res

    def moyenne_generale_eleve(self, el) -> Optional[float]:
        """Retourne la moyenne générale d'un élève (déjà définie dans la classe Eleve)."""
        return el.moyenne_generale()

    def matieres_non_notees_eleve(self, el) -> List[str]:
        """Retourne les matières sans note pour un élève."""
        return [m.nom for m in self.toutes_les_matieres() if not el.bulletin.get(m)]

    def __str__(self) -> str:
        return (f"Collège {self.nom}\n"
                f"Site : {self.siteInternet}\n"
                f"Départements : {[d.nom for d in self.listeDepartements]}\n"
                f"Salles : {[s.Id for s in self.listeSalleDeClasse]}\n"
                f"Classes : {[c.nom for c in self.listeClasses]}")
