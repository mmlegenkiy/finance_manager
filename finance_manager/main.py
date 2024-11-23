import json
from .models.transactions import Transaction
from .services.budget_manager import BudgetManager
from .services.file_manger import FileManager
from .utils.context import FileContext


def my_func_main():
    """
    Create transaction
    """

    manager = BudgetManager()

    t1 = Transaction(amount=750, category="Salary", date='2024-10-23')
    t2 = Transaction(amount=250, category="Groceries", date='2024-11-02')
    t3 = Transaction(amount=1000, category="Vacation", date='2024-11-20')

    manager.add_transactions(t1)
    manager.add_transactions(t2)
    manager.add_transactions(t3)

    # print(t1)
    # print(t2)
    #
    # print(f"Balance: {manager.calculate_balance()}")
    # categories = manager.get_by_category()
    # for category, transaction in categories.items():
    #     print(f'Category: {category}: {transaction}')

    FileManager.save_to_file("transactions.json", manager.transactions)

    loaded_transactions = FileManager.load_from_file("transactions.json")
    print(f'loaded_transactions: {loaded_transactions}')


def save_transaction(file_name, transactions):
    with FileContext(file_name, "w") as  file:
        file.write(str(transactions))


def load_transactions(file_name):
    with FileContext(file_name, 'r') as file:
        return file.read()
