import Divisibility
import pytest

@pytest.fixture()
def input():
    a = 25
    return a

def test_divby5(input):

    result = Divisibility.divby5(input)
    assert result == True
def test_divby5_1(input):

    result = Divisibility.divby5(input)
    assert result == False

def test_divby7(input):

    result = Divisibility.divby7(input)
    assert result == True
def test_divby7_1(input):

    result = Divisibility.divby7(input)
    assert result == False

def test_divby9(input):

    result = Divisibility.divby9(input)
    assert result == True
def test_divby9_1(input):

    result = Divisibility.divby9(input)
    assert result == False

def test_divby11(input):

    result = Divisibility.divby11(input)
    assert result == True
def test_divby11_1(input):

    result = Divisibility.divby11(input)
    assert result == False