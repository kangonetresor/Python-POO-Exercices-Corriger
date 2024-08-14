class Temps:
    def __init__(self, heure = 0, minutes = 0, secondes = 0):
        self._heure = heure
        self._minutes = minutes
        self._secondes = secondes

    def affichage(self):
        return f"{self._heure}h {self._minutes}min {self._secondes}s"
    
    def getheurs(self):
       return f"{self._heure}h"
    
    def getMin(self):
        return f"{self._heure}min"
        
    def getSec(self):
        return f"{self._heure}s"
    
Time1 = Temps()
print(Time1.affichage())