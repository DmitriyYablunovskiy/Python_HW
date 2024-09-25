
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  
        self.balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} Kč bylo vloženo na účet. Aktuální zůstatek: {self.balance} Kč.")
        else:
            print("Částka pro vklad musí být kladná.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} Kč bylo vybráno z účtu. Aktuální zůstatek: {self.balance} Kč.")
        else:
            print("Výběr nelze provést. Zkontrolujte zůstatek nebo částku.")

    def print(self):
        print(f"Vlastník účtu: {self.owner}, Aktuální zůstatek: {self.balance} Kč.")


muj_ucet = BankAccount('Dmitriy Yablunovskiy', 1000)
muj_ucet.deposit(10000)
muj_ucet.withdraw(500)
muj_ucet.print()
