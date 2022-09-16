# test_wallet.py

# Test sceneraios:
#    * Test default balance
#    * Test User can add cash
#    * Users can spend cash
#     * An Error is raised if the user has insufficient wallet balance
#
# Test parametrization:
#    

import pytest
from wallet.wallet import Wallet
from wallet.exceptions import InsufficientAmountException


# --- FIXTURES ---
@pytest.fixture
def empty_wallet():
    """ Returns a wallet with zero balance. """
    return Wallet()

@pytest.fixture
def wallet():
    """ Returns a wallet with 20$ balance. """
    return Wallet(20)

def test_default_initial_balance(empty_wallet):
    assert empty_wallet.balance == 0


def test_default_setting_initial_balance(wallet):
    assert wallet.balance == 20

def test_user_can_add_cash(wallet):
    wallet.add_cash(10)
    assert wallet.balance == 30

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_raises_insufficient_amount_exception_on_low_balance(empty_wallet):
    with pytest.raises(InsufficientAmountException):
        empty_wallet.spend_cash(90)


@pytest.mark.parametrize(
    'earned, spent, expected',
    [
        (40, 30, 10),
        (9, 5, 4),
        (10, 3, 7)
    ]
)
def test_transactions(earned, spent, expected):
    wallet = Wallet()
    wallet.add_cash(earned)
    wallet.spend_cash(spent)
    assert wallet.balance == expected