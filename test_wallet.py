# test_wallet.py

# Test sceneraios:
#    * Test default balance
#    * Test User can add cash
#    * Users can spend cash
#     * An Error is raised if the user has insufficient wallet balance

import pytest
from wallet.wallet import Wallet
from wallet.exceptions import InsufficientAmountException


def test_default_initial_balance():
    wallet = Wallet()
    assert wallet.balance == 0

def test_default_setting_initial_balance():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_user_can_add_cash():
    wallet = Wallet(100)
    wallet.add_cash(10)
    assert wallet.balance == 110

def test_wallet_spend_cash():
    wallet = Wallet(30)
    wallet.spend_cash(10)
    assert wallet.balance == 20

def test_wallet_raises_insufficient_amount_exception_on_low_balance():
    wallet = Wallet()
    with pytest.raises(InsufficientAmountException):
        wallet.spend_cash(90)