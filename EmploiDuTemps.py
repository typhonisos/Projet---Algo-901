"""
Un emploi du temps est modélisé comme un tableau de 81 cases.
Chacune de ces cases représente une tranche d'une heure entre 8h-12h puis 13h-17h du lundi au vendredi et ce sur une période de deux semaines afin de prendre en compte les
demi-heures d'enseignement hebdomadaire.
Ainsi 


"""

class EmploiDuTemps :

    def __init__(self, x):
        self.edt = [x]*81



    

    # La fonction getCreneau prends une date au format "jourDeLaSemaine_numeroDeLaSemaine_heureDeDebut" et renvoie l'entier correspondant à cette tranche ou 0 si format non valide
    # par exemple "Lundi 4 9" renvoie au créneau de 9h à 10h du lundi en semaine paire donc 42
    def getCreneau(date):
        jourDeLaSemaine = {"Lundi": 0, "Mardi": 1, "Mercredi": 2, "Jeudi": 3, "Vendredi": 4, "lundi": 0, "mardi": 1, "mercredi": 2, "jeudi": 3, "vendredi": 4}
        horaire = {"8": 1, "9": 2, "10": 3, "11": 4, "13": 5, "14": 6, "15": 7, "16": 8}
        res = 0
        try : 
            jour, _, temp = date.partition(" ")
            pariteSemaine, _, heure = temp.partition(" ")
            pariteSemaine = (int(pariteSemaine) - 1)%2
            jour = jourDeLaSemaine[jour]
            heure = horaire[heure]
        except :
            return res
        res = 40*pariteSemaine + 8*jour + heure
        return res
        
    def test():
        listeErreur = []
        tests = ["Lundi 4 9", "Mardi 1 11", "lundi 4 9", "londi 0 8", "lundi 4 7" ]
        resTests = [42, 12, 42, 0, 0]
        for i in range(len(tests)) :
            if EmploiDuTemps.getCreneau(tests[i]) != resTests[i]:
                listeErreur += [i]
        if listeErreur == [] :
            print("Tests Réussis")
        else:
            print("Les tests n°"+str(listeErreur)+" ont échoués")

        
EmploiDuTemps.test()


        


