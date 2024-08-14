class Forme:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

class Triangle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__(largeur, hauteur)

    def aire(self):
        return (self.hauteur * self.largeur) / 2

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__(largeur, hauteur)

    def aire(self):
        return self.hauteur * self.largeur

triangle = Triangle(4, 5)

rectangle = Rectangle(8, 2)

print("Aire du triangle", triangle.aire())

print("Aire du rectangle", rectangle.aire())

