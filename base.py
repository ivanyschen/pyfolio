from dataclasses import dataclass


VALID_ACCOUNT_TYPE = ['REGULAR', 'PRE_TAX', 'POST_TAX']


@dataclass
class Account:

    def __init__(self, brokerage_name, account_name, account_type):
        self.brokerage_name = brokerage_name
        self.account_name = account_name
        self.account_type = account_type.upper()

        self._validate_account_type()

    def _validate_account_type(self):
        return self.account_type in VALID_ACCOUNT_TYPE


@dataclass
class Order:

    def __init__(self, order_type, symbol, shares, unit_price, account):
        self.order_type = order_type
        self.symbol = symbol
        self.shares = shares
        self.unit_price = unit_price
        self.account = account

    def total_price(self):
        return round(self.shares * self.unit_price, 2)


def add_to_yaml(obj):
