class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def Versement(self, montant):
        self.solde += montant

    def Retrait(self, montant):
        if(self.solde < montant):
            print(" Impossible d'effectuer l'opération. Solde insuffisant !")
        else:
            self.solde = self.solde - montant
        
    def Agios(self):
        self.solde = self.solde * 5 / 100

