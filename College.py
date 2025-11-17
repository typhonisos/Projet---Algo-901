# -*- coding: utf-8 -*-
"""
Module : college.py
Contient UNIQUEMENT la classe College
"""

from typing import List


class College:
    def __init__(self, nom: str, siteInternet):
        """
        Initialise un collège.
        :param nom: nom du collège
        :param siteInternet: objet SiteWeb
        """
        self.aNom = nom
        self.aSiteInternet = siteInternet
        self.aListeDepartements: List = []
        self.aListeSallesDeClasse: List = []
        self.aListeClasses: List = []

    def __str__(self) -> str:
        return (
            f"Collège {self.aNom}\n"
            f"Site : {self.aSiteInternet}\n"
            f"Départements : {[d.aNom for d in self.aListeDepartements]}\n"
            f"Salles : {[s.aId_salle for s in self.aListeSallesDeClasse]}\n"
            f"Classes : {[c.aNom for c in self.aListeClasses]}"
        )
