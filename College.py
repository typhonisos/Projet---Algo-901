# -*- coding: utf-8 -*-
"""
Module : college.py
Contient UNIQUEMENT la classe College
"""

from typing import List
from SiteWeb import SiteWeb
from Departement import Departement
from SalleDeClasse import SalleDeClasse
from Classe import Classe


class College:
    def __init__(self, aNom: str, aSiteInternet):
        """
        Initialise un collège.
        :param nom: nom du collège
        :param siteInternet: objet SiteWeb
        """
        self.nom = aNom
        self.siteInternet = aSiteInternet
        self.listeDepartements: List = []
        self.listeSallesDeClasse: List = []
        self.listeClasses: List = []

    def __str__(self) -> str:
        return (
            f"Collège {self.nom}\n"
            f"Site : {self.siteInternet}\n"
            f"Départements : {[d.aNom for d in self.listeDepartements]}\n"
            f"Salles : {[s.aId_salle for s in self.listeSallesDeClasse]}\n"
            f"Classes : {[c.aNom for c in self.listeClasses]}"
        )
