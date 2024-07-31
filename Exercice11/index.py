import os

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        """
        Initialise un compte bancaire avec un titulaire et un solde initial.

        Parameters:
        account_holder (str): Nom du titulaire du compte.
        balance (float): Solde initial du compte (par défaut 0.0).
        """
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        Dépose de l'argent sur le compte.

        Parameters:
        amount (float): Montant à déposer. Doit être positif.
        """
        if amount > 0:
            self.balance += amount
            print(f"Dépôt de {amount:.2f} effectué. Nouveau solde : {self.balance:.2f}")
        else:
            print("Le montant à déposer doit être positif.")

    def withdraw(self, amount):
        """
        Retire de l'argent du compte.

        Parameters:
        amount (float): Montant à retirer. Doit être positif et ne pas dépasser le solde du compte.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Retrait de {amount:.2f} effectué. Nouveau solde : {self.balance:.2f}")
            else:
                print("Fonds insuffisants pour le retrait.")
        else:
            print("Le montant à retirer doit être positif.")

    def display_balance(self):
        """
        Affiche le solde du compte et le nom du titulaire.
        """
        print(f"Titulaire du compte : {self.account_holder}")
        print(f"Solde : {self.balance:.2f}")

# Test de la classe BankAccount
while True:
    name = input("Proprietaire du compte : ").strip()
    if name != "":
        break
    else:
        print("Le nom ne peut pas être vide.")

while True:
    balance = input("Argent sur le compte : ").strip()
    try:
        balance = float(balance)
        balance = round(balance, 2)
        break
    
    except ValueError:
        print("Le compte banquaire ne peut contenir que de l'argent.")

# Création du compte bancaire
compte = BankAccount(name, balance)

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

clearscreen()

def bank_action(n, money):
    if n == 1:
        compte.deposit(money)
    elif n == 2:
        compte.withdraw(money)

while True:
    # Affichage du solde
    compte.display_balance()

    print("Que voulez vous faire ?")
    action = input("[1] Déposer de l'argent  ou [2] Retirer de l'argent : ").strip()
    if action in ["1", "2"]:
        money = input("Combien ? ").strip()
        try:
            money = float(money)
            money = round(money, 2)
            bank_action(int(action),money)

        except ValueError:
            print("L'argent ne peut contenir que des chiffres.")
