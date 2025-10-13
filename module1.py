"""
Classe : Enseignant
Module :
Description : Permet d'avoir une ossature pour toutes mes classes
"""
class ClassTemplate():
  """ Permet d'avoir une ossature pour toutes mes classe """
  def __init__(self, aValeurAttribut01, aValeurAttribut02):
    """Constructeur avec passage des valeurs pour les attributs"""
    self.attribut01 = aValeurAttribut01
    self.attribut02 = aValeurAttribut02

  def __str__(self):
    """ Methode pour l'affichge de la classe """
    chaine="Ma mani�re d'afficher la classe ClassTemplate" +"\n"
    chaine=chaine+ "attribut01="+ str(self.attribut01) +"\n"
    chaine=chaine+ "attribut02="+ str(self.attribut02) +"\n"
    return chaine

  def action01(self, aValeurParametrage01, aValeurParametrage02):
    """ Methode pour g�rer le message action01 """
    print(str(self.attribut01) + " action01 avec les param�tres " + str(aValeurParametrage01) +", "+ str(aValeurParametrage02))

  def action02(self, aValeurParametrage01, aValeurParametrage02):
    """ Methode pour g�rer le message action02 """
    print(str(self.attribut02) + " action02 avec les param�tres " + str(aValeurParametrage01) +", "+ str(aValeurParametrage02))

if __name__ == '__main__':
  """ Permet d'executer le code localement """
  maClasseTemplate=ClassTemplate ("tutu",2)
  print(maClasseTemplate)
  maClasseTemplate.action01("01p1","01p2")
  maClasseTemplate.action02("02p1","02p2")
    
