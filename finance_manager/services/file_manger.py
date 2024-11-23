import json
from ..models.transactions import Transaction
from datetime import  datetime



class FileManager:
    """
    Class for working files
    """

    @staticmethod
    def save_to_file(file_name, data):
        with open(file_name, "w") as file:
            json.dump([{'amount': transaction.amount,
                        'category': transaction.category,
                        'date': datetime.strptime(transaction.date, "%Y-%m-%d %H:%M:%S")} for  transaction in data], file)

    @staticmethod
    def load_from_file(file_name):
        def parse_date(date_str: str) -> datetime:
            try:
                return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return datetime.strptime(date_str, '%Y-%m-%d')

        with open(file_name, "r") as file:
            data = json.load(file)
        if not all(isinstance(item, dict) for item in data):
            raise ValueError("All items in file must be dict")
        return [Transaction(amount=item['amount'],
                            category=item['category'],
                            date=parse_date(item['date'])) for item in data]
