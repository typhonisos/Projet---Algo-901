
class SalleDeClasse :
    def __init__(self, id_salle : str, capacite : int):
        self.id_salle = id_salle
        self.capacite = capacite 
        
    def __str__(self):
        return f"Salle {self.id_salle} (capacité: {self.capacite} places)"
    
if __name__=="__main__" :
    salle1 = SalleDeClasse("A101", 30)
    salle2 = SalleDeClasse("B206", 25) 
    salle3 = SalleDeClasse("C304", 25)
    print(salle2)
    
