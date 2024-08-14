class Account:
    def __init__(self, balance = 0):
        self.balance = balance

    def getBalance(self):
        return self.balance
    
    def deposer(self, montant):
        self.balance += montant

    def retirer(self, montant):
        self.balance -= montant

    def ajouter_Interet(self, interet):
        self.sold *= (1 + interet)

Compte1 = Account(2000)

#print(Compte1.getBalance())
Compte1.retirer(500)
#Compte1.retirer(1500)

print(Compte1.getBalance())

    