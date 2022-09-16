import pytest

def test_file_method():
    x=2
    y=3
    assert x+1 == y, 'test failed! Error x=' + str(x) + ' y=' + str(y)


def test_file2_method():
    x='a'
    assert 'a'==x