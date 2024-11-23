from collections import defaultdict
from ..models.transactions import Transaction

class BudgetManager:
    """
    Class for management of budgets.
    """

    def __init__(self):
        self.transactions = []

    def add_transactions(self, transaction: Transaction):
        self.transactions.append(transaction)

    def calculate_balance(self):
        return sum(t.amount for t in self.transactions)

    def get_by_category(self):
        result = defaultdict(list)
        for transaction in self.transactions:
            result[transaction.category].append(transaction)
        return result

    def __iter__(self):
        return iter(self.transactions)