# encoding: utf-8
# test_capitalize.py

import pytest
from typing import Union

def toCaps(word: str):
    if not isinstance(word, str):
        raise TypeError('Invalid Argument Type.')
    return word.upper()

def test_captalize():
    assert toCaps('ABcd') == 'ABCD'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError) as e:
        toCaps(9)