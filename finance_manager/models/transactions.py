from  datetime import datetime


class PositiveValue:
    """
    Descriptor for validate positive value
    """

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f'{self.name.capitalize()} must be positive value!')
        instance.__dict__[self.name] = value


class Transaction:
    """
    Class for save transaction data
    """

    amount = PositiveValue()

    def __init__(self, amount: float, category: str, date: str = None):
        self.amount = amount
        self.category = category
        self.date = date if isinstance(date, datetime) else datetime.strptime(date, '%Y-%m-%d').date()

    def __repr__(self):
        return f'Transaction(amount.{self.amount}, category.{self.category}, date.{self.date.date()})'


