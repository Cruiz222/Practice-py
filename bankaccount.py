def BankAccount:
    def __init__(self, owner: str, initial_balance: float):
        self.owner = owner

        self._balance = (0.0, initial_balance)


    def deposit(self, amount: float):
        if amount < 0:
            return ValueError("amount must be positive")

        self._balance += amount

        return self._balance


    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("amount must be positive")

        if self._balance < amount:
            raise ValueError("Insufficent funds")

        self._balance -= amount

        return self._balance                    


    def get_balance(self):
        return self._balance    