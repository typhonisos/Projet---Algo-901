from EmploiDuTemps import EmploiDuTemps
from Classe import Classe


class EdtSalle(EmploiDuTemps) :

    def __init__(self, classe):
        self.edt = [classe]*81


    def afficherOccupationSalle(self, date):
        creneau = self.getCreneau(date)
        if creneau == 0 :
            print("La date donnée est invalide")
        elif self.edt[creneau] == None : 
            print("La salle est inoccupé sur le créneau du :"+date)
        else : 
            print("Sur le créneau du "+date+ " , la salle est occupée par la classe :" + self.edt[creneau].nom )    




    

        
EmploiDuTemps.test()


        


