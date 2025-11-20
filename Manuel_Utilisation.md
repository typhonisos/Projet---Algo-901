# Manuel d'utilisation

## Contexte 
On souhaite créer un logiciel pour une academie afin qu'elle puisse gérer les cours dispensés dans ses différents collèges.
Afin de répondre à cette problématique, nous avons créé différents documents:
- Un diagramme UML
- Un diagramme de Gantt
- Un dictionnaire pour regrouper le vocabulaire technique
- Un programme

## Déroulement du projet 
Grâce au diagramme de Gantt, on peut suivre le déroulement du projet. 
Il a 3 points de livraison:
- le vendredi 17 octobre 2025 (S42)
- le vendredi 21 novembre 2025 (S47)
- le vendredi 19 décembre 2025 (S51)
  
Le diagramme UML est mis à jour avant chaque livraison. On retrouve la version du diagramme UML associé sous le nom 
"DiagrammeUML_livraison_semaine_XX".

Le diagramme de Gantt est également mis à jour avant chaque livraison. 

## Contenu du programme 
Le programme contient un fichier main qui permet d'utiliser les différentes classes. Il sert d'exemple d'utilisation. 

- La classe **Collège** permet de regrouper les départements, les salles de classes, les classes d'un même collège ainsi que son site web.
```python
# Exemple d'utilisation de la classe College

```
- La classe **SiteWeb** permet d'obtenir l'URL du site web du collège.
```python
# Exemple d'utilisation de la classe SiteWeb

```
- La classe **SalleDeClasse** permet d'accèder à toutes les informations d'une classe, de savoir si elle est disponible à un créneau horaire, de la réserver et d'afficher toutes les réservations de cette salle.
```python
# Exemple d'utilisation de la classe SalleDeClasse

```
- La classe **Classe** permet de regrouper les élèves composant une même classe.
```python
# Exemple d'utilisation de la classe Classe

```
- La classe **Departement** permet de regrouper les proffesseurs. Chaque département à un responsable qui peut-être changé, une liste de matière et une liste d'ensaigant. On peut supprimer et ajouter des matières au département ainsi que des proffesseurs.
```python
# Exemple d'utilisation de la classe Departement

```
- La classe **Enseignant** regroupe les informations d'un enseigant, sa date de prise de fonction, son indice, sa matière et son responsable.
```python
# Exemple d'utilisation de la classe Enseigant

```
- La classe **Matiere** regroupe les informations de la matière, son nom, son volume horaire et les notes obtenues dans cette matière. Pour chaque matère, on peut ajouter des notes, ajouter des enseignants, faire la moyenne des notes dans cette matière et ajouter une liste d'élèves non notés dans cette matière.
```python
# Exemple d'utilisation de la classe Matiere

```
- La classe **Eleve** regroupe les informations d'un élève, son année d'entrée dans le collège, son niveau d'étude et se notes. Pour chaque élève, on peut ajouter des notes, faire sa moyenne par matière et faire sa moyenne générale.
```python
# Exemple d'utilisation de la classe Eleve

```
- La classe **Personne** sert a avoir les informations générale de chaque personne de l'établissement (élève ou enseignant). Elle regroupe leur nom, prenom, numéro de téléphone et mail et permet de créer une fiche signalitique.
```python
# Exemple d'utilisation de la classe Personne

```
