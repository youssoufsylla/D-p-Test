class CompteBancaire:
    def __init__(self, titulaire: str, solde: float = 0.0):
        self.titulaire = titulaire
        self.solde = solde
        self.historique = []

    def deposer(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif.")
        self.solde += montant
        self.historique.append(f"Dépôt de {montant:.2f}")
        print(f"{montant:.2f}€ déposés. Nouveau solde : {self.solde:.2f}€")

    def retirer(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
        if montant > self.solde:
            raise ValueError("Fonds insuffisants.")
        self.solde -= montant
        self.historique.append(f"Retrait de {montant:.2f}")
        print(f"{montant:.2f}€ retirés. Nouveau solde : {self.solde:.2f}€")

    def afficher_solde(self):
        print(f"Solde de {self.titulaire} : {self.solde:.2f}€")

    def afficher_historique(self):
        print(f"Historique de {self.titulaire} :")
        for ligne in self.historique:
            print(f" - {ligne}")


def gestionnaire():
    comptes = {
        "Alice": CompteBancaire("Alice", 150.0),
        "Bob": CompteBancaire("Bob", 75.0)
    }

    try:
        comptes["Alice"].deposer(50)
        comptes["Bob"].retirer(25)
        comptes["Alice"].retirer(300)  # va échouer
    except ValueError as e:
        print(f"Erreur : {e}")

    for compte in comptes.values():
        compte.afficher_solde()
        compte.afficher_historique()
if __name__ == "__main__":
    gestionnaire()