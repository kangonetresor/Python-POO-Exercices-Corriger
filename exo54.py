class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def perimetre(self):
        return (self.largeur + self.longueur) * 2
    
    def surface(self):
        return self.largeur * self.longueur
    
    def getLargeur(self):
        return self.largeur
    
    def getLongueur(self):
        return self.longueur
    
    def setLargeur(self, val):
        self.largeur += val

    def setLongueur(self, val):
        self.longueur += val

class Parallelepipede(Rectangle):
    def __init__(self, largeur, longueur, hauteur):
        super().__init__(largeur, longueur)
        self.hauteur = hauteur

    def Volume(self):
        return self.longueur * self.largeur * self.hauteur

para1 = Parallelepipede(3, 7, 9)
print(para1.setLongueur(-2))