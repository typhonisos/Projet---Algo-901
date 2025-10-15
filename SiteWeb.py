from datetime import datetime

class SiteWeb:
    """
    Classe représentant le site Internet d'un collège.
    """

    def __init__(self, Url, Date_Creation, Responsable, Statut="actif", Pages=None):
        """
        Initialise un site web.
        
        : url: L’adresse du site 
        : date_creation: Date de création du site
        : responsable: Nom de la personne responsable du site 
        : statut: Statut du site 
        : pages: Liste des pages disponibles sur le site
        """
        self.url = Url
        self.date_creation = Date_Creation
        self.responsable = Responsable
        self.statut = Statut
        self.pages = Pages if Pages else []

    # --- Méthodes de gestion des pages ---
    def ajouter_page(self, Titre, Contenu):
        """
        Ajoute une nouvelle page au site web.
        """
        page = {"titre": Titre, "contenu": Contenu, "date_ajout": datetime.now()}
        self.pages.append(page)
        print(f" Page '{Titre}' ajoutée au site {self.url}.")

    def supprimer_page(self, Titre):
        """
        Supprime une page du site à partir de son titre.
        """
        for page in self.pages:
            if page["titre"] == Titre:
                self.pages.remove(page)
                print(f" Page '{Titre}' supprimée du site {self.url}.")
                return
        print(f" Aucune page nommée '{Titre}' trouvée sur le site.")

    def afficher_pages(self):
        """
        Affiche la liste des pages disponibles sur le site.
        """
        if not self.pages:
            print("Aucune page n’est disponible pour le moment.")
        else:
            print(f" Pages du site {self.url} :")
            for page in self.pages:
                print(f" - {page['titre']} (créée le {page['date_ajout'].strftime('%d/%m/%Y')})")

    # --- Méthodes d'administration ---
    def changer_statut(self, Nouveau_Statut):
        """
        Change le statut du site (actif, maintenance, fermé).
        """
        if Nouveau_Statut in ["actif", "maintenance", "fermé"]:
            self.statut = Nouveau_Statut
            print(f" Le site {self.url} est maintenant en mode '{self.statut}'.")
        else:
            print(" Statut invalide. Valeurs possibles : actif, maintenance, fermé.")

    def afficher_infos(self):
        """
        Affiche toutes les informations du site web.
        """
        print(f"\n Informations sur le site :")
        print(f" - URL : {self.url}")
        print(f" - Responsable : {self.responsable}")
        print(f" - Date de création : {self.date_creation.strftime('%d/%m/%Y')}")
        print(f" - Statut : {self.statut}")
        print(f" - Nombre de pages : {len(self.pages)}")
