from datetime import datetime
from enum import Enum
from typing import Optional

class Page:
    """
    Classe représentant une page dans un site web
    """

    def __init__(self, titre: str="", contenu: str=""):
        """
        :url: Adresse de la page web
        :titre: Titre de la page
        :contenu: Contenu de la page
        """
        self.aContenu = contenu
        self.aTitre = titre

    def ajouterContenu(self, nouveau_contenu: str):
        self.aContenu += nouveau_contenu

    def __str__(self) -> str:
        out = f"Page {self.aTitre if self.aTitre != "" else 'sans titre'}: "
        if self.aContenu != "":
            out += f"\nContenu: \n{self.aContenu}"
        return out

class StatutPage(str, Enum):
    """
    Typage des statuts possible d'une page
    """
    ACTIF = 'ACTIF'
    EN_MAINTENANCE = 'EN_MAINTENANCE'
    FERME = 'FERME'

    def __str__(self):
        return self.name.replace('_', ' ').capitalize()


class SiteWeb:
    """
    Classe représentant le site Internet d'un collège.
    """

    def __init__(self, url:str, date_creation: datetime , statut=StatutPage.ACTIF, pages: Optional[list[Page]] = None):
        """
        Initialise un site web.
        
        : url: L’adresse du site 
        : date_creation: Date de création du site
        : statut: Statut du site 
        : pages: dictionnaire de pages indexés par leurs url présentes sur le site
        """
        self.aUrl = url
        self.aDateCreation = date_creation
        self.aPages = {}

        # Ajout un à un des pages pour avoir les bons urls
        if pages is not None:
            for page in pages:
                self.ajouterPage(page.aTitre, page.aContenu)

        if statut in StatutPage.__members__:
            self.aStatut = statut
        else:
            print(f"Attention: Statut {statut} inconnu lors de l'initialisation, valeur {StatutPage.ACTIF} utilisé")
            self.aStatut = StatutPage.ACTIF

    # --- Méthodes de gestion des pages ---
    def ajouterPage(self, titre:str, contenu: str=""):
        """
        Ajoute une nouvelle page au site web.
        :titre: titre de la page à ajouter (doit être unique sur le site)
        """
        url_nouvelle_page = f"{self.aUrl}/{titre.replace(' ', '-').lower()}"
        if url_nouvelle_page not in self.aPages:
            self.aPages.setdefault(url_nouvelle_page, Page(titre=titre, contenu=contenu))
        else:
            print(f"Attention: tentative d'ajout de page échouée, la page {url_nouvelle_page} existe déjà")


    def supprimerPage(self, titre: str):
        """
        Supprime une page du site à partir de son titre.
        """
        url_page = f"{self.aUrl}/{titre.replace(' ', '-').lower()}"
        if url_page in self.aPages:
            del(self.aPages[url_page])
        else:
            print(f"Attention: tentative de suppression échouée: page {url_page} inconnue")

    def afficherPages(self):
        """
        Affiche la liste des pages disponibles sur le site.
        """
        if len(self.aPages) > 0:
            print("Pages disponibles sur le site:".center(50, '-'))
            for url in self.aPages:
                print(url + ":")
                print(self.aPages[url])
        else:
            print("Aucune page n’est disponible pour le moment.")
        
    # --- Méthodes d'administration ---
    def changerStatut(self, nouveau_statut: str):
        """
        Change le statut du site (ACTIF, EN_MAINTENANCE, FERME).
        """
        if nouveau_statut in StatutPage.__members__:
            self.aStatut = nouveau_statut
            print(f" Le site {self.aUrl} est maintenant en mode '{self.aStatut}'.")
        else:
            print(" Statut invalide. Valeurs possibles : ACTIF, EN_MAINTENANCE, FERME")

    def afficherInfos(self):
        """
        Affiche toutes les informations du site web.
        """
        print(f"Informations sur le site :".center(50, '-'))
        print(f" - URL : {self.aUrl}")
        print(f" - Date de création : {self.aDateCreation.strftime('%d/%m/%Y')}")
        print(f" - Statut : {self.aStatut}")
        print(f" - Nombre de pages : {len(self.aPages)}")


"""
Tests
"""
if __name__ == "__main__":

    page_predefinie = Page(titre="Morphisme de Hurewicz", contenu = "Ab(pi_1(X)) = H_1(X)")
    print("Test page unique: \n" + page_predefinie.__str__())

    site = SiteWeb(
        url="https://M2MMAA.com",
        date_creation=datetime.now(),
        pages = [page_predefinie]
    )

    site.afficherInfos()

    nouveau_contenu = "Bonjour à tous.tes, je vous informe que demain vous n'avez pas cours!!"
    site.ajouterPage(titre="Annonce de la responsable", contenu=nouveau_contenu)

    site.afficherPages()

    # Suppression de page inexistante
    site.supprimerPage("une page inexistante")

    # Suppression de page existante
    site.supprimerPage("annonce de la responsable")
    site.afficherPages()

    # Ajout de page déjà existante
    site.ajouterPage(titre="Morphisme de hurewicz", contenu="pi_n(X) s'injecte dans H_n(X)")
    site.afficherPages()
