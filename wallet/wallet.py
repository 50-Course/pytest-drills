# encoding: utf-8
# 
# wallet.py

from .exceptions import InsufficientAmountException

class Wallet:
    """
    Base class for a wallet object. 

    There are different wallet tiers, hence extends this base class.

    Attributes:
        - initial_amount (int) - Wallet Balance for a specific user wallet.
    """
    def __init__(self, initial_amount: int = 0) -> None:
        self.balance = initial_amount

    def spend_cash(self, amount: int):
        if amount > self.balance:
            raise InsufficientAmountException(
                f'Insufficient Amount! Not enough balance '
                f'to spend {amount}.'
            )
        self.balance -= amount

    def add_cash(self, amount: int):
        if amount < 0:
            raise ValueError('You can\'t add nothing to balance.')
        self.balance += amount