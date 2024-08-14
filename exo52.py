class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def perimetre(self):
        return (self.largeur + self.hauteur) * 2
    
    def surface(self):
        return self.largeur * self.hauteur

    def affichage(self):
        return f"Le perimètre est : {self.perimetre()} et la surface est : {self.surface()}"
    
    #Mutateurs trivaux
    def getLargeur(self):
        return self.largeur
    
    def getHauteur(self):
        return self.hauteur
    
    def setLargeur(self, val):
        self.largeur += val

    def setHauteur(self, val):
        self.hauteur += val

rect1 = Rectangle(5, 6)
print(rect1.affichage())
print("La hauteur est : ", rect1.getHauteur())
print("La largeur est : ", rect1.getLargeur())

rect1.setHauteur(-2)
print("La hauteur est : ", rect1.getHauteur())





