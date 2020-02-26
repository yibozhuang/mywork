from functools import total_ordering


@total_ordering
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position):
        return self._transactions[position]

    def __reversed__(self):
        return self[::-1]

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        owner = f"{self.owner} & {other.owner}"
        start_amount = self.amount + other.amount
        acc = Account(owner, start_amount)

        for t in list(self) + list(other):
            acc.add_transaction(t)

        return acc

    def __call__(self):
        print(f"Start amount: {self.amount}")
        print("Transactions")
        for t in self:
            print(t)
        print(f"Balance: {self.balance}")

    def __enter__(self):
        print("ENTER WITH: Making backup of transactions for rollback")
        self._copy_transactions = list(self._transactions)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT WITH:', end=' ')
        if exc_type:
            self._transactions = self._copy_transactions
            print("Rolling back to previous transactions")
            print(f"Transaction resulted in {exc_type.__name__} ({exc_val})")

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("amount must be int format")

        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)
